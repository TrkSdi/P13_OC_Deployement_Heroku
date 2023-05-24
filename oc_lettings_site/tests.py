from django.urls import reverse

# Acces to url test
def test_route_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200

# Getting content test
def test_get_data_index(client):
    url = reverse('index')
    response = client.get(url)
    assert b'Welcome to Holiday Homes' in response.content
    assert b'Profiles' in response.content
    assert b'Lettings' in response.content
