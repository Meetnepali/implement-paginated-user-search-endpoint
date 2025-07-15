from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.encoders import jsonable_encoder

class CustomValidationException(Exception):
    def __init__(self, detail, status_code=400):
        self.detail = detail
        self.status_code = status_code

def create_error_response(errors, code=400):
    """
    Converts pydantic or custom error details into a uniform JSON error structure
    e.g. { "error": { "code": 400, "message": "Validation error", "details": [{ ... }] } }
    """
    if isinstance(errors, Exception):
        # If errors is an exception, extract message
        details = [{"msg": str(errors)}]
    else:
        details = errors
    return {
        "error": {
            "code": code,
            "message": "Validation error",
            "details": details,
        }
    }

def error_handler(request: Request, exc: CustomValidationException):
    return JSONResponse(
        status_code=exc.status_code,
        content=create_error_response(exc.detail, code=exc.status_code)
    )
