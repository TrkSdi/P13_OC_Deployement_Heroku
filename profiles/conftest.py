from profiles.models import Profile
from django.contrib.auth.models import User
import pytest


@pytest.fixture
def profiles_obj():
    user = User.objects.create(first_name="Jamie",
                               last_name='Lal',
                               email='jssssss33@acee9.live',
                               username='HeadlinesGazer'
                               )
    profile_fix = Profile.objects.create(user=user, favorite_city='Buenos Aires')
    return profile_fix
