https://www.youtube.com/watch?v=5dmDRtMvdb4&list=PLMbRqrU_kvbRI4PgSzgbh8XPEwC1RNj8F&index=2
Primero isntalamos Django
    pip install -m django
luego creamos la app
    django-admin startprojec
luego separamos el settings en 3 archivos (settings/local.py, settings/production.py, base/local.py)
cambiamos la ruta de settings a los nuevos archivos de settings a settins.local en manage.py, ecomerce_rest/wsgi.py, ecomerce_rest/asgi.py
eliminamos settings.py
luego instalamos rest_framework
    pip install djangorestframework
#(minuto 11.10)