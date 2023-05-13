import pytest
from .something import Something

def test_something():
    assert Something().hi() == "hi there"

def test_answer():
    assert str(42) == "42"

# see https://docs.pytest.org/en/7.3.x/reference/reference.html#pytest-skip

@pytest.mark.skip("reason to skip")
def test_skipped():
    assert "antwort" == 42

# see https://docs.pytest.org/en/7.3.x/reference/reference.html#pytest.mark.xfail

@pytest.mark.xfail(reason = "this can be used to mark a bug in a characterization test")
def test_characterize_bug():
    assert "antwort" == 42

@pytest.mark.xfail(reason = "see doc for more options")
def test_characterize_bug_that_succeeds_unexpectedly():
    assert True