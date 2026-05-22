"""User management module demonstrating class-based design."""
from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    """
    Represents a user in the system.
    
    Attributes:
        id: Unique user identifier
        username: User's username
        email: User's email address
        created_at: Timestamp when user was created
        is_active: Whether the user account is active
    """
    id: int
    username: str
    email: str
    created_at: datetime
    is_active: bool = True
    
    def deactivate(self) -> None:
        """Deactivate the user account."""
        self.is_active = False
    
    def activate(self) -> None:
        """Activate the user account."""
        self.is_active = True


class UserRepository:
    """
    Repository for managing user data.
    
    This class demonstrates the repository pattern for data access.
    """
    
    def __init__(self):
        """Initialize the user repository with an empty user list."""
        self._users: List[User] = []
        self._next_id: int = 1
    
    def create(self, username: str, email: str) -> User:
        """
        Create a new user.
        
        Args:
            username: The user's username
            email: The user's email address
            
        Returns:
            The newly created User object
            
        Raises:
            ValueError: If username or email is empty
        """
        if not username or not email:
            raise ValueError("Username and email are required")
        
        user = User(
            id=self._next_id,
            username=username,
            email=email,
            created_at=datetime.now()
        )
        self._users.append(user)
        self._next_id += 1
        return user
    
    def find_by_id(self, user_id: int) -> Optional[User]:
        """
        Find a user by ID.
        
        Args:
            user_id: The user's ID
            
        Returns:
            The User object if found, None otherwise
        """
        for user in self._users:
            if user.id == user_id:
                return user
        return None
    
    def find_by_username(self, username: str) -> Optional[User]:
        """
        Find a user by username.
        
        Args:
            username: The username to search for
            
        Returns:
            The User object if found, None otherwise
        """
        for user in self._users:
            if user.username == username:
                return user
        return None
    
    def get_all_active(self) -> List[User]:
        """
        Get all active users.
        
        Returns:
            A list of active User objects
        """
        return [user for user in self._users if user.is_active]
    
    def count(self) -> int:
        """
        Get the total number of users.
        
        Returns:
            The count of users in the repository
        """
        return len(self._users)
