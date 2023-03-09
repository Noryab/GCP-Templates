# From Drive to Storage

This code was written to automate the ingestion of data from Drive to Google Cloud Storage and uses the Google API to automate the ingestion of data from Google Drive to Google Cloud Storage.

With generate_token, you can get the refresh_token for any credentials that you've created in ID de clientes OAuth 2.0.

You can use it with oauth2 credentials for Drive API, then you need to get token, client_secret and client_id. For ease, the credentials are read locally to obtain client_id, client_secret, token, but it is recommended to modify to consult these fields of a table in some db, example:

´select client_id, client_secret, token, refresh_token from credentials order by update desc limit 1´


