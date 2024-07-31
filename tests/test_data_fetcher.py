import unittest
from unittest.mock import patch, MagicMock
from src.app.data_fetcher import fetch_data
from src.app.config import API_URL
import json

class TestDataFetcher(unittest.TestCase):
    
    def setUp(self) -> None:
        with open('tests/data/test_data.json', 'r') as f:
            self.test_data = json.load(f)
    
    @patch('app.data_fetcher.requests.get') 
    def test_fetch_data_success(self, mock_get):
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.test_data
        mock_get.return_value = mock_response

        data = fetch_data()

        mock_get.assert_called_once_with(API_URL)

        self.assertEqual(data, self.test_data)

    @patch('app.data_fetcher.requests.get')
    def test_fetch_data_failure(self, mock_get):

        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        data = fetch_data()

        mock_get.assert_called_once_with(API_URL)

        self.assertIsNone(data)

if __name__ == '__main__':
    unittest.main()
