"""Tests for configuration management."""
import os
import pytest
from src.config import Config


class TestConfig:
    """Tests for the Config class."""
    
    def test_config_defaults(self):
        """Test that config has sensible defaults."""
        config = Config()
        assert config.app_name == "My Python Project"
        assert config.debug is False
        assert config.db_host == "localhost"
        assert config.db_port == 5432
        assert config.api_timeout == 30
    
    def test_config_from_env(self, monkeypatch):
        """Test loading config from environment variables."""
        # Set environment variables
        monkeypatch.setenv("APP_NAME", "Test App")
        monkeypatch.setenv("DEBUG", "true")
        monkeypatch.setenv("DB_HOST", "db.example.com")
        monkeypatch.setenv("DB_PORT", "3306")
        monkeypatch.setenv("API_TIMEOUT", "60")
        
        config = Config.from_env()
        assert config.app_name == "Test App"
        assert config.debug is True
        assert config.db_host == "db.example.com"
        assert config.db_port == 3306
        assert config.api_timeout == 60
    
    def test_config_debug_false_variations(self, monkeypatch):
        """Test that debug is False for various non-true values."""
        test_values = ["false", "False", "FALSE", "0", "no", ""]
        
        for value in test_values:
            monkeypatch.setenv("DEBUG", value)
            config = Config.from_env()
            assert config.debug is False, f"Failed for DEBUG={value}"
    
    def test_get_db_url(self):
        """Test getting database URL."""
        config = Config(db_host="localhost", db_port=5432, db_name="testdb")
        url = config.get_db_url()
        assert url == "postgresql://localhost:5432/testdb"
    
    def test_get_db_url_custom_host(self):
        """Test database URL with custom host."""
        config = Config(db_host="db.prod.com", db_port=3306, db_name="proddb")
        url = config.get_db_url()
        assert url == "postgresql://db.prod.com:3306/proddb"
