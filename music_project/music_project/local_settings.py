DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT':'3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}

SECRET_KEY = 'django-insecure-4g)cug!+0zf2lhd9f!w+5+iw@2pss7_u-2#3859%##66k3!9m-'