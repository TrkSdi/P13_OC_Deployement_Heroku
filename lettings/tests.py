from .models import Letting, Address
from django.contrib.sites.models import Site
from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_letting_index(client):
    url = reverse('lettings:letting_index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_index_content(client):
    url = reverse('lettings:letting_index')
    response = client.get(url)
    data = response.content.decode()
    exepected_data = "<h1>Lettings</h1>"

    assert exepected_data in data

@pytest.mark.django_db
def test_letting_detail_content(client):
    url = reverse('lettings:lettings_id', kwargs={'letting_id':1})
    address = Address.objects.create(number=7217, 
                                     street='Bedford Street',
                                     city='Brunswick',
                                     state='GA',
                                     zip_code=31525,
                                     country_iso_code='USA')
    Letting.objects.create(title='Joshua Tree Green Haus /w Hot Tub', address=address)
    response = client.get(url)
    data = response.content.decode()
    expected_data = '<title>Joshua Tree Green Haus /w Hot Tub</title>'
    assert expected_data in data
