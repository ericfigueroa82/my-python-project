"""Tests for the main module."""
import pytest
from src.main import greet


def test_greet():
    """Test the greet function."""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_greet_empty_string():
    """Test greet with empty string."""
    assert greet("") == "Hello, !"
