import pytest
from main import assistant_role,generate_response

def test_assistant_role_mentions_world_cup():
    assert "FIFA World Cup 2026" in assistant_role

def test_assistant_role_mentions_navigation():
    assert "Stadium navigation" in assistant_role

def test_assistant_role_mentions_ticket_support():
    assert "Ticket support" in assistant_role

def test_assistant_role_mentions_accessibility():
    assert "Accessibility support" in assistant_role

def test_generate_response_exists():
    assert callable(generate_response)
