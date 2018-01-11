# bobby-unknowns-battle-cards-api
BobbyUnknown's BattleCards Python API

# Decription

# Installation
## Dependencies
Run the following command :
    
```
pip install -r requirements.txt --no-index
```
    
## Settings.py

Make sure, you have add the following lines into your settings.py

### Installed Apps
```
    INSTALLED_APPS = [
        ...,
        'app',
        'rest_framework',
        'rest_framework.authtoken',
        'corsheaders',
        'django_filters',
        'channels',
    ]
```

### Django Rest Framework
```
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAdminUser',
            'rest_framework.permissions.IsAuthenticated',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        ),
        'DEFAULT_FILTER_BACKENDS': (
            'django_filters.rest_framework.DjangoFilterBackend',
        )
    }
```

### Cors headers
```
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'token-type'
)
```

### Django Channels
```
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgiref.inmemory.ChannelLayer",
        "ROUTING": "app.routing.channel_routing",
    },
}
```

### Authentication
```
AUTH_USER_MODEL = 'app.User
```

# Documentation

## Run the server
```
    python manage.py runserver
```

## Migrations
```
    python manage.py makemigrations
    python manage.py migrate
```