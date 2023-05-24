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
    
#@pytest.mark.django_db
#def test_letting_detail_content(client, address, letting ):
#    url = reverse('lettings:lettings_id', kwargs={'letting_id':1})
#    response = client.get(url)
#    data = response.content.decode()
#    print("DATA", data)
#    expected_data = letting
#    
#    assert expected_data in letting