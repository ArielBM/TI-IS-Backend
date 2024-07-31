from data_fetcher import fetch_data
from data_transformer import save_data_as_json, transform_data_to_csv, create_summary_csv
from database import insert_data
from data_transfer import transfer_files
from datetime import datetime
from config import OUTPUT_DIR
import os
import sched
import time

if __name__ == "__main__":
    data = fetch_data()
    if (data):
        
        date_str = datetime.now().strftime('%Y%m%d')
        
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        
        json_file_path = os.path.join(OUTPUT_DIR, f'data_{date_str}.json')
        save_data_as_json(data, json_file_path)
        
        csv_file_path = os.path.join(OUTPUT_DIR, f'ETL_{date_str}.csv')
        transform_data_to_csv(data["users"], csv_file_path)
        
        summary_file_path = os.path.join(OUTPUT_DIR, f'summary_{date_str}.csv')
        create_summary_csv(data["users"], summary_file_path)
        
        insert_data(summary_file_path,csv_file_path)
        
        transfer_files(json_file_path, f'data_{date_str}.json')
        transfer_files(csv_file_path,f'ETL_{date_str}.csv')
        transfer_files(summary_file_path,f'summary_{date_str}.csv')