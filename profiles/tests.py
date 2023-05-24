from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_profiles_index(client):
    url = reverse('profiles:profile_index')
    response = client.get(url)
    assert response.status_code == 200
        

@pytest.mark.django_db
def test_profiles_index_content(client):
    url = reverse('profiles:profile_index')
    response = client.get(url)
    data = response.content.decode()
    exepected_data = "<h1>Profiles</h1>"
    
    assert exepected_data in data
