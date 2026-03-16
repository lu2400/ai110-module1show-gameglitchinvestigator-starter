from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Bug fix: backwards hint messages ---

def test_too_high_message_says_go_lower():
    # Bug: message used to say "Go HIGHER!" when guess was too high
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message, got: {message}"

def test_too_low_message_says_go_higher():
    # Bug: message used to say "Go LOWER!" when guess was too low
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message, got: {message}"

def test_too_high_message_does_not_say_go_higher():
    # Regression: confirm the wrong message is no longer returned
    outcome, message = check_guess(80, 50)
    assert "HIGHER" not in message, f"Message should not say 'HIGHER' when guess is too high, got: {message}"

def test_too_low_message_does_not_say_go_lower():
    # Regression: confirm the wrong message is no longer returned
    outcome, message = check_guess(20, 50)
    assert "LOWER" not in message, f"Message should not say 'LOWER' when guess is too low, got: {message}"


# --- Bug fix: invalid guesses should not count as attempts ---

def test_invalid_guess_returns_not_ok():
    # parse_guess should reject non-numeric input
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err is not None

def test_empty_guess_returns_not_ok():
    # parse_guess should reject empty input
    ok, value, err = parse_guess("")
    assert ok is False

def test_valid_guess_returns_ok():
    # parse_guess should accept a valid integer string
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None
