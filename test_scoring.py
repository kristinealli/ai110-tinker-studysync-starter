import pytest

from scoring import session_rating


def test_session_rating_boundary_90_is_great():
    assert session_rating(90) == "Great"


def test_session_rating_boundary_80_is_good():
    assert session_rating(80) == "Good"


@pytest.mark.parametrize(
    "score, expected",
    [
        (0, "Skip"),
        (59, "Skip"),
        (60, "Meh"),
        (69, "Meh"),
        (70, "OK"),
        (79, "OK"),
        (80, "Good"),
        (89, "Good"),
        (90, "Great"),
        (100, "Great"),
    ],
)
def test_session_rating_thresholds(score, expected):
    assert session_rating(score) == expected


@pytest.mark.parametrize("bad_value", [-1, 120, 87.5, "90", None])
def test_session_rating_invalid_inputs_raise_error(bad_value):
    with pytest.raises((TypeError, ValueError)):
        session_rating(bad_value)
