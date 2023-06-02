import os
from django.conf import settings
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application_default = get_wsgi_application()
application = WhiteNoise(application_default, root=settings.STATIC_ROOT)
#application.add_files("/path/to/more/static/files", prefix="more-files/")


