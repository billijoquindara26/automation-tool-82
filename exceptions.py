class AutomationError(Exception):
    """Base exception for automation-tool-82."""
    pass

class ConfigurationError(AutomationError):
    """Raised when configuration is invalid."""
    pass

class ProcessingError(AutomationError):
    """Raised when data processing fails."""
    pass

class ValidationError(AutomationError):
    """Raised when input validation fails."""
    pass

def handle_exception(e: Exception) -> None:
    if isinstance(e, AutomationError):
        print(f"Application error: {e}")
    else:
        print(f"Unexpected system error: {e}")

class ErrorHandler:
    def __init__(self, logger):
        self.logger = logger

    def execute(self, func, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AutomationError as e:
            self.logger.error(f"Custom error encountered: {e}")
            raise
        except Exception as e:
            self.logger.critical(f"Unhandled exception: {e}")
            raise AutomationError("Internal operation failure") from e