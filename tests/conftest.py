"""Shared test fixtures and configuration."""
import pytest


@pytest.fixture
def sample_user_data():
    """Provide sample user data for testing."""
    return {
        "username": "testuser",
        "email": "test@example.com"
    }


@pytest.fixture
def sample_users_list():
    """Provide a list of sample users for testing."""
    return [
        {"username": "alice", "email": "alice@example.com"},
        {"username": "bob", "email": "bob@example.com"},
        {"username": "charlie", "email": "charlie@example.com"},
    ]
