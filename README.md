# Dèmè-Cours Open Learning Toolkit

[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/Content-CC%20BY%204.0-green.svg)](LICENSE-CONTENT.md)

An independent, open-source learning, assessment and privacy-preserving education data toolkit developed by **Dèmè-Cours** in Mali.

> **Status:** early-stage working prototype. This repository provides a small demonstrator dataset and API. It does not claim production readiness or measured impact.

## Why this project exists

Learners in Mali face unequal access to structured revision materials, timely feedback and affordable learning support. Dèmè-Cours currently uses Glide as a user interface. This toolkit separates reusable education infrastructure from that proprietary interface so that schools, nonprofits, developers and learning platforms can run, study, adapt and improve the core services independently.

## Current capabilities

- Filter sample learning questions by grade and subject.
- Deliver quiz questions without exposing correct answers.
- Score submitted answers through an API.
- Publish anonymous aggregate activity metrics.
- Run locally or in Docker.
- Explore interactive OpenAPI documentation.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://localhost:8000/docs` for interactive documentation.

### Docker

```bash
docker build -t demecours-open-learning-toolkit .
docker run --rm -p 8000:8000 demecours-open-learning-toolkit
```

## Open-source boundary

The API, tests, sample data and documentation function without Glide. Glide can consume the API as one possible client. No proprietary Dèmè-Cours database, learner record or credential is included.

## Documentation

- [Architecture and Glide integration](docs/architecture.md)
- [12-month open-source roadmap](docs/open-source-roadmap.md)
- [Contribution guidelines](CONTRIBUTING.md)
- [Responsible data and security](SECURITY.md)

Software is licensed under MIT. Original sample educational content is licensed under CC BY 4.0.
