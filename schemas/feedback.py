from pydantic import BaseModel, EmailStr, validator, root_validator
from typing import Optional

class FeedbackSubmission(BaseModel):
    user_email: EmailStr
    rating: int
    comment: Optional[str] = None

    @validator('rating')
    def rating_must_be_between_1_and_5(cls, v):
        if not 1 <= v <= 5:
            raise ValueError('rating must be between 1 and 5')
        return v

    @validator('comment')
    def comment_max_length(cls, v):
        if v is not None and len(v) > 500:
            raise ValueError('comment must be 500 characters or fewer')
        return v
