# Import Libraries
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Credentials - Preparing to make a delegated API call
from google.oauth2 import service_account

# SCOPES = ['https://www.googleapis.com/auth/sqlservice.admin']
SERVICE_ACCOUNT_FILE = "keys.json.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Create credentials using the service account file and specified scopes
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID of the spreadsheet.
SAMPLE_SPREADSHEET_ID = "1qwmISXtmGDHctx1MVizaKAdkS0W2sfvJOZpNlGiAdPw"

# Build the Sheets API service
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API to get data from the spreadsheet
sheet = service.spreadsheets()
result = sheet.values().get(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Merged_File!a1:bk73477").execute()

# Get the values from the result
values = result.get("values", [])

print(values)