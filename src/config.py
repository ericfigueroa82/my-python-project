"""Configuration management for the application."""
import os
from typing import Optional
from dataclasses import dataclass


@dataclass
class Config:
    """
    Application configuration.
    
    Loads configuration from environment variables with sensible defaults.
    """
    
    # Application settings
    app_name: str = "My Python Project"
    debug: bool = False
    
    # Database settings
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "myapp"
    
    # API settings
    api_timeout: int = 30
    api_max_retries: int = 3
    
    @classmethod
    def from_env(cls) -> "Config":
        """
        Create a Config instance from environment variables.
        
        Returns:
            A Config object populated from environment variables
        """
        return cls(
            app_name=os.getenv("APP_NAME", "My Python Project"),
            debug=os.getenv("DEBUG", "false").lower() == "true",
            db_host=os.getenv("DB_HOST", "localhost"),
            db_port=int(os.getenv("DB_PORT", "5432")),
            db_name=os.getenv("DB_NAME", "myapp"),
            api_timeout=int(os.getenv("API_TIMEOUT", "30")),
            api_max_retries=int(os.getenv("API_MAX_RETRIES", "3")),
        )
    
    def get_db_url(self) -> str:
        """
        Get the database connection URL.
        
        Returns:
            The database connection string
        """
        return f"postgresql://{self.db_host}:{self.db_port}/{self.db_name}"


# Global config instance
config = Config.from_env()
