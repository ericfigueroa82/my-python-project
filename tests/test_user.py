"""Tests for the user module."""
import pytest
from datetime import datetime
from src.user import User, UserRepository


class TestUser:
    """Tests for the User dataclass."""
    
    def test_user_creation(self):
        """Test creating a user instance."""
        user = User(
            id=1,
            username="johndoe",
            email="john@example.com",
            created_at=datetime.now()
        )
        assert user.id == 1
        assert user.username == "johndoe"
        assert user.email == "john@example.com"
        assert user.is_active is True
    
    def test_user_deactivate(self):
        """Test deactivating a user."""
        user = User(
            id=1,
            username="johndoe",
            email="john@example.com",
            created_at=datetime.now()
        )
        user.deactivate()
        assert user.is_active is False
    
    def test_user_activate(self):
        """Test activating a deactivated user."""
        user = User(
            id=1,
            username="johndoe",
            email="john@example.com",
            created_at=datetime.now(),
            is_active=False
        )
        user.activate()
        assert user.is_active is True


class TestUserRepository:
    """Tests for the UserRepository class."""
    
    @pytest.fixture
    def repo(self):
        """Create a fresh UserRepository for each test."""
        return UserRepository()
    
    def test_create_user(self, repo):
        """Test creating a user through the repository."""
        user = repo.create("alice", "alice@example.com")
        assert user.id == 1
        assert user.username == "alice"
        assert user.email == "alice@example.com"
        assert user.is_active is True
    
    def test_create_user_increments_id(self, repo):
        """Test that user IDs increment correctly."""
        user1 = repo.create("alice", "alice@example.com")
        user2 = repo.create("bob", "bob@example.com")
        assert user1.id == 1
        assert user2.id == 2
    
    def test_create_user_invalid_data(self, repo):
        """Test that creating a user with invalid data raises ValueError."""
        with pytest.raises(ValueError):
            repo.create("", "email@example.com")
        
        with pytest.raises(ValueError):
            repo.create("username", "")
    
    def test_find_by_id_success(self, repo):
        """Test finding a user by ID."""
        created_user = repo.create("charlie", "charlie@example.com")
        found_user = repo.find_by_id(created_user.id)
        assert found_user == created_user
    
    def test_find_by_id_not_found(self, repo):
        """Test that finding a non-existent user returns None."""
        result = repo.find_by_id(999)
        assert result is None
    
    def test_find_by_username_success(self, repo):
        """Test finding a user by username."""
        created_user = repo.create("david", "david@example.com")
        found_user = repo.find_by_username("david")
        assert found_user == created_user
    
    def test_find_by_username_not_found(self, repo):
        """Test that finding a non-existent username returns None."""
        result = repo.find_by_username("nonexistent")
        assert result is None
    
    def test_get_all_active(self, repo):
        """Test getting all active users."""
        user1 = repo.create("alice", "alice@example.com")
        user2 = repo.create("bob", "bob@example.com")
        user3 = repo.create("charlie", "charlie@example.com")
        
        user2.deactivate()
        
        active_users = repo.get_all_active()
        assert len(active_users) == 2
        assert user1 in active_users
        assert user3 in active_users
        assert user2 not in active_users
    
    def test_count(self, repo):
        """Test counting users in the repository."""
        assert repo.count() == 0
        
        repo.create("user1", "user1@example.com")
        assert repo.count() == 1
        
        repo.create("user2", "user2@example.com")
        assert repo.count() == 2
