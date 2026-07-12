import pytest
from main import assistant_role, generate_response

def test_assistant_role_mentions_world_cup():
    """Verify the AI prompt is tailored specifically for the 2026 World Cup."""
    assert "FIFA World Cup 2026" in assistant_role
    assert "Stadium navigation" in assistant_role

def test_assistant_role_defines_fallback():
    """Verify the AI knows how to politely decline out-of-scope questions."""
    fallback_text = "I don't have reliable information about that topic"
    assert fallback_text in assistant_role

def test_generate_response_exists():
    """Verify that the primary core execution function is properly defined."""
    assert callable(generate_response)
