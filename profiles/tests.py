from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_profiles_index_content(client):
    url = reverse('profiles:profile_index')
    response = client.get(url)
    data = response.content.decode()
    expected_data = "<title>Profiles</title>"

    assert response.status_code == 200
    assert expected_data in data


@pytest.mark.django_db
def test_profile_detail_content(db, client, profiles_obj):
    url = reverse('profiles:profiles_id', kwargs={'username': 'HeadlinesGazer'})
    response = client.get(url)
    data = response.content.decode()

    assert response.status_code == 200
    assert profiles_obj.user.username in data
