import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Define el alcance de acceso requerido por tu aplicación.
scopes = [                
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/drive.readonly',
        'https://www.googleapis.com/auth/drive.metadata.readonly',
        'https://www.googleapis.com/auth/drive.appdata',
        'https://www.googleapis.com/auth/drive.metadata',
        'https://www.googleapis.com/auth/drive.photos.readonly',
    ]


basedir = os.path.abspath(os.path.dirname(__file__))
# Opening JSON file
key_path =  os.path.join(basedir, "credentials.json")

# Define los parámetros de configuración del flujo de autorización de OAuth2.
flow = InstalledAppFlow.from_client_secrets_file(key_path, scopes=scopes)

# Inicia el flujo de autorización de OAuth2 para obtener el token de acceso del usuario.
creds = flow.run_local_server(port=0)

# Almacenar de manera segura el token de acceso del usuario para su uso posterior.
# Por ejemplo, puedes guardar el token en una base de datos o en un archivo protegido.
print(f"refresh_token: {creds.refresh_token}, token: {creds.token}")