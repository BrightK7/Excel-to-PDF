from Google import Create_Service
CLIENT_SCRETS_FILE = "credentials.json"
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
servive = Create_Service(CLIENT_SCRETS_FILE,API_NAME,API_VERSION,SCOPES)
filed_ids = ['1cvPOLzItJU939fl8nu8gBgdhVYdeheME3J-bOHlfxoI','1N9CmfA_O8K4E8s7V0K10hAFIMp-EDd4D']
servive.file()
print(dir(servive)) 
