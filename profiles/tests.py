from django.urls import reverse
import pytest
from django.contrib.auth.models import User
from .models import Profile

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

@pytest.mark.django_db
def test_profile_detail_content(client):
    url = reverse('profiles:profiles_id', kwargs={'username':'HeadlinesGazer'})
    user = User.objects.create(first_name="Jamie", 
                               last_name='Lal',
                               email='jssssss33@acee9.live',
                               username='HeadlinesGazer'
                               )
    Profile.objects.create(user=user, favorite_city='Buenos Aires')
    response = client.get(url)
    data = response.content.decode()
    expected_data = 'HeadlinesGazer'
    assert expected_data in data