from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse
from schemas.feedback import FeedbackSubmission
from utils.errors import CustomValidationException

router = APIRouter()

@router.post("/submit", status_code=status.HTTP_201_CREATED)
async def submit_feedback(feedback: FeedbackSubmission, request: Request):
    # On success, return feedback submitted
    return {"feedback": feedback.dict()}
