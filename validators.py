import pathlib
import re
from urllib.parse import urlparse

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')


def is_valid_email(email: str) -> bool:
    """Check if the provided string is a syntactically valid email address.

    Args:
        email: The email string to validate.

    Returns:
        True if valid, False otherwise.
    """
    if not email:
        return False
    return bool(EMAIL_REGEX.match(email))


def is_valid_url(url: str) -> bool:
    """Verify that a string is a valid HTTP or HTTPS URL.

    Args:
        url: The URL string to validate.

    Returns:
        True if valid, False otherwise.
    """
    try:
        parsed = urlparse(url)
        return all([parsed.scheme in ('http', 'https'), parsed.netloc])
    except ValueError:
        return False


def is_valid_filepath(path_str: str, must_exist: bool = False) -> bool:
    """Validate a filepath and optionally check if it exists on disk.

    Args:
        path_str: The filesystem path string to validate.
        must_exist: If True, the file must physically exist.

    Returns:
        True if the path is valid and matches the criteria, False otherwise.
    """
    if not path_str:
        return False
    try:
        path = pathlib.Path(path_str)
        if must_exist:
            return path.is_file()
        return True
    except (TypeError, ValueError):
        return False
