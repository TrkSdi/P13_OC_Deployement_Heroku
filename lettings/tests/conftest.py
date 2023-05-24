import pytest


@pytest.fixture
def addresses():
    addresses = [
        {
            "title": "Test",
        }]
    yield addresses