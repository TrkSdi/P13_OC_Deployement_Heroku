import pytest
from .models import Address, Letting


@pytest.fixture
def address():
    address = Address(7217,
                      'Bedford Street',
                      'Brunswick',
                      'GA',
                      31525,
                      'USA'
    )
    yield address
    
@pytest.fixture
def letting():
    letting = Letting("Joshua Tree Green Haus /w Hot Tub",
                      address)
    yield letting