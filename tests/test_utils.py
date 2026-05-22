"""Tests for utility functions."""
import pytest
from src.utils import (
    validate_email,
    chunk_list,
    safe_json_loads,
    truncate_string
)


class TestValidateEmail:
    """Tests for email validation."""
    
    @pytest.mark.parametrize("email,expected", [
        ("user@example.com", True),
        ("test.user@domain.co.uk", True),
        ("invalid", False),
        ("@example.com", False),
        ("user@", False),
        ("", False),
        ("no-at-sign.com", False),
    ])
    def test_validate_email(self, email, expected):
        """Test email validation with various inputs."""
        assert validate_email(email) == expected


class TestChunkList:
    """Tests for list chunking."""
    
    def test_chunk_list_even_split(self):
        """Test chunking a list with even division."""
        items = [1, 2, 3, 4, 5, 6]
        result = chunk_list(items, 2)
        assert result == [[1, 2], [3, 4], [5, 6]]
    
    def test_chunk_list_uneven_split(self):
        """Test chunking a list with uneven division."""
        items = [1, 2, 3, 4, 5]
        result = chunk_list(items, 2)
        assert result == [[1, 2], [3, 4], [5]]
    
    def test_chunk_list_larger_chunk_size(self):
        """Test chunking with chunk size larger than list."""
        items = [1, 2, 3]
        result = chunk_list(items, 10)
        assert result == [[1, 2, 3]]
    
    def test_chunk_list_empty(self):
        """Test chunking an empty list."""
        result = chunk_list([], 2)
        assert result == []
    
    def test_chunk_list_invalid_size(self):
        """Test that invalid chunk size raises ValueError."""
        with pytest.raises(ValueError):
            chunk_list([1, 2, 3], 0)
        
        with pytest.raises(ValueError):
            chunk_list([1, 2, 3], -1)


class TestSafeJsonLoads:
    """Tests for safe JSON parsing."""
    
    def test_safe_json_loads_valid(self):
        """Test parsing valid JSON."""
        result = safe_json_loads('{"key": "value"}')
        assert result == {"key": "value"}
    
    def test_safe_json_loads_invalid(self):
        """Test parsing invalid JSON returns empty dict."""
        result = safe_json_loads("not json")
        assert result == {}
    
    def test_safe_json_loads_none(self):
        """Test parsing None returns empty dict."""
        result = safe_json_loads(None)
        assert result == {}
    
    def test_safe_json_loads_empty_string(self):
        """Test parsing empty string returns empty dict."""
        result = safe_json_loads("")
        assert result == {}


class TestTruncateString:
    """Tests for string truncation."""
    
    def test_truncate_string_no_truncation_needed(self):
        """Test that short strings are not truncated."""
        result = truncate_string("Hello", 10)
        assert result == "Hello"
    
    def test_truncate_string_exact_length(self):
        """Test string at exact max length is not truncated."""
        result = truncate_string("Hello", 5)
        assert result == "Hello"
    
    def test_truncate_string_with_default_suffix(self):
        """Test truncating with default suffix."""
        result = truncate_string("Hello World", 8)
        assert result == "Hello..."
    
    def test_truncate_string_with_custom_suffix(self):
        """Test truncating with custom suffix."""
        result = truncate_string("Hello World", 8, suffix="~")
        assert result == "Hello W~"
    
    def test_truncate_string_very_short_max_length(self):
        """Test truncating to very short length."""
        result = truncate_string("Hello World", 3)
        assert result == "..."
