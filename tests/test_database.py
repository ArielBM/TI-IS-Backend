import unittest
from unittest.mock import patch, MagicMock
import sqlite3
import os
from datetime import datetime
from src.app.database import insert_data

class TestDatabaseInsertion(unittest.TestCase):

    @patch('src.app.database.sqlite3.connect')
    @patch('src.app.database.datetime', wraps=datetime)
    def test_insert_data(self, mock_datetime, mock_connect):
        test_date = '2024-07-31'
        mock_datetime.now.return_value = datetime.strptime(test_date, '%Y-%m-%d')

        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_connect.return_value = mock_conn

        mock_cursor.lastrowid = 1

        summary_file_path = os.path.join('tests', 'data', 'summary_test.csv')
        etl_file_path = os.path.join('tests', 'data', 'etl_test.csv')

        insert_data(summary_file_path, etl_file_path)

        mock_cursor.execute.assert_any_call(
            'INSERT INTO Header (date_insertion) VALUES (?)',
            (test_date,)
        )

        mock_cursor.execute.assert_any_call(
            'INSERT INTO Summary (header_id, category, subcategory, count) VALUES (?, ?, ?, ?)',
            (mock_cursor.lastrowid, 'Gender', 'female', 17)
        )

        mock_cursor.execute.assert_any_call(
            'INSERT INTO Detail (header_id, id, firstName, lastName, maidenName, age, gender, email, phone, username, password, birthDate, image, bloodGroup, height, weight, eyeColor, hair_color, hair_type, ip, address_address, address_city, address_state, address_stateCode, address_postalCode, address_coordinates_lat, address_coordinates_lng, address_country, macAddress, university, bank_cardExpire, bank_cardNumber, bank_cardType, bank_currency, bank_iban, company_department, company_name, company_title, company_address_address, company_address_city, company_address_state, company_address_stateCode, company_address_postalCode, company_address_coordinates_lat, company_address_coordinates_lng, company_address_country, crypto_coin, crypto_wallet, crypto_network, role) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            [mock_cursor.lastrowid, '1', 'Emily', 'Johnson', 'Smith', '28', 'female', 'emily.johnson@x.dummyjson.com', '+81 965-431-3024', 'emilys', 'emilyspass', '1996-5-30', 'https://dummyjson.com/icon/emilys/128', 'O-', '193.24', '63.16', 'Green', 'Brown', 'Curly', '42.48.100.32', '626 Main Street', 'Phoenix', 'Mississippi', 'MS', '29112', '-77.16213', '-92.084824', 'United States', '47:fa:41:18:ec:eb', 'University of Wisconsin--Madison', '03/26', '9289760655481815', 'Elo', 'CNY', 'YPUXISOBI7TTHPK2BR3HAIXL', 'Engineering', 'Dooley, Kozey and Cronin', 'Sales Manager', '263 Tenth Street', 'San Francisco', 'Wisconsin', 'WI', '37657', '71.814525', '-161.150263', 'United States', 'Bitcoin', '0xb9fc2fe63b2a6c003f1c324c3bfa53259162181a', 'Ethereum (ERC20)', 'admin']
        )

if __name__ == '__main__':
    unittest.main()
