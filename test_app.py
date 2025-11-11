from app import greet

def test_greet():
    result = greet("Pranay")
    assert result == "Hello, Pranay! Welcome to Python CI/CD Demo."
