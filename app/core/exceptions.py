from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class ApplicationException(Exception):
    """
    Base exception for application-specific errors.
    """

    def __init__(
        self,
        message: str,
        status_code: int = 400,
    ) -> None:
        self.message = message
        self.status_code = status_code
        super().__init__(message)


async def application_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    """
    Handle application exceptions.
    """

    if not isinstance(exc, ApplicationException):
        raise exc

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "message": exc.message,
                "status": exc.status_code,
            }
        },
    )


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register custom exception handlers.
    """

    app.add_exception_handler(
        ApplicationException,
        application_exception_handler,
    )
