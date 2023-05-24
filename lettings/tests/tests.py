from django.urls import reverse
import pytest


#@pytest.mark.django_db
#def test_letting_index(client):
#    url = reverse('oc_lettings_site:lettings_url')
#    response = client.get(url)
#    assert response.status_code == 200
    
    
#@pytest.mark.django_db
#def test_letting_index_content(client, addresses):
#    response = client.get('/lettings/')
#    data = response.content
#    
#    print("DATA", data)
#    
#    assert addresses[0]['title'] in data.decode()