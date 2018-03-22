import unittest

import gspread
from dotenv import load_dotenv, find_dotenv

from sheet import SpreadSheet

load_dotenv(find_dotenv())


class TestSpreadsheet(unittest.TestCase):
    """ Tests for Spreadsheet """

    def setUp(self):
        self.sheet = SpreadSheet()
        self.sheet_name = 'Test spreadsheet'

    def test_spreadsheet_can_be_opened(self):
        spreadsheet = self.sheet.open(self.sheet_name)
        self.assertIsNotNone(spreadsheet)
        self.assertIsInstance(spreadsheet, gspread.v4.models.Spreadsheet)

    def test_spreadsheet_can_be_written_to(self):
        screen_name = 'income'
        followers_count = 1000003
        data = {'screen_name': screen_name, 'followers_count': followers_count}

        self.sheet.write(self.sheet_name, data)
        spreadsheet = self.sheet.open(self.sheet_name)
        worksheet = spreadsheet.sheet1
        content = worksheet.get_all_values()
        index = len(content)

        username_header = worksheet.cell(1, 1).value
        username = worksheet.cell(index, 1).value
        followers = worksheet.cell(index, 2).value

        self.assertEqual(username_header, 'Twitter Handle')
        self.assertEqual(username, screen_name)
        self.assertEqual(followers, str(followers_count))

