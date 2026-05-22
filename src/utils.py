"""Utility functions for common operations."""
from typing import List, Any, Dict
import json


def validate_email(email: str) -> bool:
    """
    Validate an email address format.
    
    Args:
        email: The email address to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not email or '@' not in email:
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    local, domain = parts
    return bool(local) and bool(domain) and '.' in domain


def chunk_list(items: List[Any], chunk_size: int) -> List[List[Any]]:
    """
    Split a list into chunks of specified size.
    
    Args:
        items: The list to chunk
        chunk_size: The size of each chunk
        
    Returns:
        A list of chunks
        
    Raises:
        ValueError: If chunk_size is less than 1
    """
    if chunk_size < 1:
        raise ValueError("Chunk size must be at least 1")
    
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def safe_json_loads(json_string: str) -> Dict[str, Any]:
    """
    Safely parse JSON string, returning empty dict on error.
    
    Args:
        json_string: JSON string to parse
        
    Returns:
        Parsed dictionary or empty dict if parsing fails
    """
    try:
        return json.loads(json_string)
    except (json.JSONDecodeError, TypeError):
        return {}


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate a string to a maximum length.
    
    Args:
        text: The text to truncate
        max_length: Maximum length of the result
        suffix: Suffix to add to truncated text
        
    Returns:
        The truncated string with suffix if needed
    """
    if len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)] + suffix
