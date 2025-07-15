from fastapi import FastAPI
from utils.errors import error_handler, CustomValidationException
from routers import feedback

app = FastAPI()

# Register the feedback router
app.include_router(feedback.router, prefix="/api/feedback", tags=["Feedback"])

# Register the custom exception handler for validation (pydantic/errors)
app.add_exception_handler(CustomValidationException, error_handler)

# Optional: handle generic validation errors globally (e.g. from request validation)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    from utils.errors import create_error_response
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content=create_error_response(exc.errors()),
    )
