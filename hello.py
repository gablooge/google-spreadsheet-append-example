import httplib2
import os

from googleapiclient import discovery
from google.oauth2 import service_account

try:
	scopes = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.file' ,"https://www.googleapis.com/auth/spreadsheets",]
	secret_file = os.path.join(os.getcwd(), 'rsvp-credentials.json')
	credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
	service = discovery.build('sheets', 'v4', credentials=credentials)
	spreadsheet_id = '1EVjM0wMYWmmz33HbxXh5MpUqQPWlCTQR0cde7QN1o7I'
	range_name = 'RSVP!A2:G'
	data = [
		['1', 'Achmad Mustakim', '085850062823', '1', 'Unduh Mantu', '', '']
	]
	body = {
		'values': data
	}
	result = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_name,valueInputOption='USER_ENTERED',body=body).execute()

	print('{0} cells appended.'.format(result.get('updates').get('updatedCells')))
except OSError as e:
	print(e)