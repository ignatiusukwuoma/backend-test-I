import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials


def authorize_account():
    """
    Generates credentials from the client_secret.json file
    :return credentials: obj. The account credentials
    """

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    except ValueError:
        raise ValueError('Please provide valid SERVICE_ACCOUNT credentials in client_secret.json file')
    except KeyError:
        raise KeyError('One of the expected keys is not present in client_secret.json file')
    return credentials


class SpreadSheet:
    """ Connects to the Google Spreadsheet API """

    def __init__(self):
        self.client = gspread.authorize(authorize_account())

    def open(self, sheet_name):
        """
        Opens a spreadsheet or creates a new one
        :param sheet_name: str. The name of the spreadsheet to open
        :return spreadsheet: obj. The opened spreadsheet
        """

        try:
            spreadsheet = self.client.open(sheet_name)
        except gspread.SpreadsheetNotFound:
            spreadsheet = self.client.create(sheet_name)
            email = os.getenv('CLIENT_EMAIL')
            if not email:
                raise ValueError('Please provide the client email as required')
            spreadsheet.share(email, perm_type='user', role='writer')
        return spreadsheet

    def write(self, sheet_name, data):
        """
        Write data to Spreadsheet
        :param sheet_name: str. The name of the Google Sheet to be written to
        :param data: obj. Data to be written to Google Sheets.
        """

        spreadsheet = self.open(sheet_name)
        worksheet = spreadsheet.sheet1
        content = worksheet.get_all_values()

        index = len(content) + 1
        if index == 1:
            worksheet.update_cell(index, 1, 'Twitter Handle')
            worksheet.update_cell(index, 2, 'Number of Followers')
            index += 1

        worksheet.update_cell(index, 1, data['screen_name'])
        worksheet.update_cell(index, 2, data['followers_count'])
