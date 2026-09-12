from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    assert client.get("/health").json() == {"status": "ok"}


def test_questions_hide_answers() -> None:
    response = client.get("/v1/questions", params={"subject": "Mathématiques"})
    assert response.status_code == 200
    assert response.json()
    assert all("correct_answer" not in item for item in response.json())


def test_quiz_scoring() -> None:
    response = client.post("/v1/quiz/submit", json={"attempts": [
        {"question_id": "ml-9-math-001", "answer": "x = 6"},
        {"question_id": "ml-def-geo-001", "answer": "Niger"}
    ]})
    assert response.status_code == 200
    assert response.json()["percentage"] == 100.0
