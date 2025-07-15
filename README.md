# Guidance for Task

This project is a FastAPI-based backend service intended for structured user feedback submission in an internal business environment.

## Requirements
- Implement a POST endpoint at `/api/feedback/submit` using a dedicated feedback router.
- Input should be strictly validated: `user_email` must be a valid email, `rating` must be an integer between 1 and 5, and `comment` (optional) must be no longer than 500 characters. All validation uses Pydantic models with custom constraints as appropriate.
- On success, a 201 response and the submitted feedback data is returned.
- On validation failure or error, a structured JSON error is returned via a custom error handler, following a uniform format for all errors and validation issues.
- The codebase is modular, with separate directories for routers, schemas, and error utilities.
- There is no database, frontend, authentication, or external integrations required.

## Verifying Your Solution
- Ensure the `/api/feedback/submit` endpoint responds with a 201 status and echoes the submitted payload (after validation) on valid data.
- Try submitting invalid data (such as out-of-range ratings, invalid emails, or comments that are too long) and confirm structured, consistent JSON error payloads are returned.
- The project should be startable in a Docker container or via local virtual environment, with minimal setup required for dependency installation and service start.
- The code should be clear, modular, and match the organizational structure described.

You are expected to focus only on the backend endpoint logic. Storage, authentication, UI, or persistence are not part of this exercise.