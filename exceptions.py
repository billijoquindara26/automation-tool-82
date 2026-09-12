class AutomationError(Exception):
    """Base exception for automation-tool-82."""


class ValidationError(AutomationError):
    """Raised when input validation fails."""


class ConfigurationError(AutomationError):
    """Raised for invalid tool configuration."""


class ExecutionError(AutomationError):
    """Raised during automation process failures."""


def handle_exception(e: Exception) -> None:
    if isinstance(e, (ValidationError, ConfigurationError)):
        print(f"User input or config error: {e}")
    elif isinstance(e, ExecutionError):
        print(f"Critical runtime failure: {e}")
    else:
        print(f"Unexpected system error: {e}")


def validate_input(data: dict, required_keys: list) -> None:
    for key in required_keys:
        if key not in data:
            raise ValidationError(f"Missing required field: {key}")


def execute_task(task_func, *args, **kwargs):
    try:
        return task_func(*args, **kwargs)
    except Exception as e:
        handle_exception(e)
        raise ExecutionError(f"Task execution failed: {e}") from e