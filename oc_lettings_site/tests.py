from django.urls import reverse


# Getting content test
def test_get_data_index(client):
    url = reverse('index')
    response = client.get(url)
    data = response.content.decode()
    expected_data = '<title>Holiday Homes</title>'

    assert response.status_code == 200
    assert expected_data in data
