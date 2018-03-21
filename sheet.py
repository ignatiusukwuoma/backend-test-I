import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']


def authorize_account():
    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    except ValueError as error:
        raise error
    except KeyError as err:
        raise err
    return credentials


class SpreadSheet:
    """ Connects to the Google Spreadsheet API """

    def __init__(self):
        self.gc = gspread.authorize(authorize_account())

    def open(self, sheet_name):
        """ Opens a spreadsheet or creates a new one"""

        try:
            spreadsheet = self.gc.open(sheet_name)
        except gspread.SpreadsheetNotFound:
            spreadsheet = self.gc.create(sheet_name)
            email = os.getenv('CLIENT_EMAIL')
            if not email:
                raise ValueError('Please provide the client email as required')
            spreadsheet.share(email, perm_type='user', role='writer')
        return spreadsheet

    def write(self, sheet_name=None, data=None):
        """ Write data to Spreadsheet """

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
