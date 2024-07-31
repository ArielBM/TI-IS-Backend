import unittest
import json
import os
import pandas as pd
from datetime import datetime
from src.app.data_transformer import save_data_as_json, transform_data_to_csv, create_summary_csv

class TestDataProcessing(unittest.TestCase):
    
    def setUp(self) -> None:
        self.date_str = datetime.now().strftime('%Y%m%d')
        with open('tests/data/test_data.json', 'r') as f:
            self.test_data = json.load(f)
    
    def test_save_data_as_json(self):
        data = self.test_data
        with open(f'data_{self.date_str}.json', "w") as temp_file:
            save_data_as_json(data, temp_file.name)

        with open(temp_file.name, 'r') as f:
            saved_data = f.read()
        self.assertIsNotNone(saved_data)
        print('save_data_as_json test passed.')
        
        
    def test_transform_data_to_csv(self):
        data = self.test_data["users"]
        
        with open( f'ETL_{self.date_str}.csv', "w") as temp_file:
            transform_data_to_csv(data, temp_file.name)

        with open(temp_file.name, 'r') as f:
            saved_data = f.read()
        self.assertIn("id,firstName,lastName,maidenName,age,gender", saved_data)
        print(f'transform_data_to_csv test passed.')
        
    def test_create_summary_csv(self):
        data = self.test_data["users"]
        
        with open( f'summary_{self.date_str}.csv', "w") as temp_file:
            create_summary_csv(data, temp_file.name)
            
        with open(temp_file.name, 'r') as f:
            saved_data = f.read()
            
        self.assertIn("gender,total", saved_data)
        print(f'create_summary_csv test passed.')

if __name__ == '__main__':
    unittest.main()
