"""Main application module."""


def greet(name: str) -> str:
    """
    Generate a greeting message.
    
    Args:
        name: The name to greet
        
    Returns:
        A greeting message
    """
    return f"Hello, {name}!"


def main():
    """Entry point for the application."""
    print(greet("World"))


if __name__ == "__main__":
    main()
