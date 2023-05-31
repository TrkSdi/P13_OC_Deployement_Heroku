from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_letting_index_content(client):
    url = reverse('lettings:letting_index')
    response = client.get(url)
    data = response.content.decode()
    expected_data = "<title>Lettings</title>"

    assert response.status_code == 200
    assert expected_data in data


@pytest.mark.django_db
def test_letting_detail_content(db, client, lettings_obj):
    url = reverse('lettings:lettings_id', kwargs={'letting_id': 1})
    response = client.get(url)
    data = response.content.decode()

    assert response.status_code == 200
    assert lettings_obj.title in data
