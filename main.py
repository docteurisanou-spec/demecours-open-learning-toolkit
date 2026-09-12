"""Independent Dèmè-Cours learning and assessment API."""

import json
from collections import Counter
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

DATA_FILE = Path(__file__).resolve().parent / "sample_questions.json"
QUESTIONS = json.loads(DATA_FILE.read_text(encoding="utf-8"))
QUESTION_INDEX = {item["id"]: item for item in QUESTIONS}
METRICS = Counter({"quiz_submissions": 0, "answers_submitted": 0, "correct_answers": 0})

app = FastAPI(
    title="Dèmè-Cours Open Learning Toolkit",
    description="Reusable learning content, assessment and anonymous aggregate metrics.",
    version="0.1.0",
    license_info={"name": "MIT", "url": "https://opensource.org/license/mit/"},
)


class Attempt(BaseModel):
    question_id: str
    answer: str = Field(min_length=1, max_length=200)


class QuizSubmission(BaseModel):
    attempts: list[Attempt] = Field(min_length=1, max_length=50)


@app.get("/")
def root() -> dict:
    return {"name": "Dèmè-Cours Open Learning Toolkit", "version": "0.1.0", "docs": "/docs"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/v1/questions")
def list_questions(
    grade: str | None = None,
    subject: str | None = None,
    limit: int = Query(default=10, ge=1, le=100),
) -> list[dict]:
    selected = QUESTIONS
    if grade:
        selected = [q for q in selected if q["grade"].casefold() == grade.casefold()]
    if subject:
        selected = [q for q in selected if q["subject"].casefold() == subject.casefold()]
    return [{k: v for k, v in q.items() if k != "correct_answer"} for q in selected[:limit]]


@app.post("/v1/quiz/submit")
def submit_quiz(submission: QuizSubmission) -> dict:
    results = []
    correct = 0
    for attempt in submission.attempts:
        question = QUESTION_INDEX.get(attempt.question_id)
        if question is None:
            raise HTTPException(status_code=404, detail=f"Unknown question_id: {attempt.question_id}")
        is_correct = attempt.answer.strip().casefold() == question["correct_answer"].strip().casefold()
        results.append({"question_id": attempt.question_id, "correct": is_correct})
        correct += int(is_correct)
    total = len(results)
    METRICS["quiz_submissions"] += 1
    METRICS["answers_submitted"] += total
    METRICS["correct_answers"] += correct
    return {"score": correct, "total": total, "percentage": round(correct / total * 100, 2), "results": results}


@app.get("/v1/metrics")
def public_metrics() -> dict:
    answers = METRICS["answers_submitted"]
    accuracy = round(METRICS["correct_answers"] / answers * 100, 2) if answers else 0.0
    return {
        "privacy": "Aggregate counters only; no names, emails or device identifiers.",
        "quiz_submissions": METRICS["quiz_submissions"],
        "answers_submitted": answers,
        "correct_answers": METRICS["correct_answers"],
        "accuracy_percentage": accuracy,
        "persistence": "Prototype metrics reset when the service restarts.",
    }
