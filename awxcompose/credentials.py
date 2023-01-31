DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "awx",
        'USER': "awx",
        'PASSWORD': "awxpass",
        'HOST': "postgres",
        'PORT': "5432",
    }
}

BROADCAST_WEBSOCKET_SECRET = "cTVIS2owR082UnA1WmszRmlpTGE3dHJNYkpDVE9lcy1iLDMzNG1jMGt6c2gxdFd0Ym1ud1h2VTlrOXcyd3FZbVE6WENiMHhYc1dKclFmVi1WTmxkLjhJVk1ZeEFSSUswTjEtcFhDRzRNUzN3RGhyYldlSWlOZmZBbjpad21CZUo="
