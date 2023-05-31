import pytest
from lettings.models import Address, Letting


@pytest.fixture
def lettings_obj():
    address_fix = Address.objects.create(number=7217,
                                         street='Bedford Street',
                                         city='Brunswick',
                                         state='GA',
                                         zip_code=31525,
                                         country_iso_code='USA')
    letting_fix = Letting.objects.create(title='Joshua Tree Green Haus /w Hot Tub',
                                         address=address_fix)
    return letting_fix
