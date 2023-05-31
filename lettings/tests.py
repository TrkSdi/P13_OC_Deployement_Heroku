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
    domain = "localhost:8000" #Site.objects.get_current().domain
    print("Domain", domain)
    url = reverse('lettings:lettings_id', kwargs={'letting_id':1})
    url_absolute = f'{domain}{url}'
    print("URL", url_absolute)
    response = client.get(url)
    data = response.content.decode()
    print("DATA", data)
    expected_data = "<title>Joshua Tree Green Haus /w Hot Tub</title>"
    assert expected_data in data
