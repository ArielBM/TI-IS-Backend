import sqlite3
import csv
from datetime import datetime

try:
    from src.app.config import DB_PATH
except ModuleNotFoundError:
    from config import DB_PATH

def insert_data(summary_file_path, etl_file_path):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
                   INSERT INTO Header (date_insertion)
                   VALUES (?)
                   ''', (datetime.now().strftime('%Y-%m-%d'),))
    header_id = cursor.lastrowid
    
    with open(summary_file_path, newline='', encoding='utf-8') as summaryfile:
        csvreader = csv.reader(summaryfile, delimiter=',')
        
        current_category = None
        for row in csvreader:
            if not row:
                continue
            if row[0].strip().lower() in ['gender', 'age', 'city', 'os']:
                current_category = row[0].capitalize()
            elif current_category:
                if current_category == 'Gender' or current_category == 'Os':
                    subcategory, count = row
                    cursor.execute('''
                                   INSERT INTO Summary (header_id, category, subcategory, count)
                                   VALUES(?,?,?,?)
                                   ''', (header_id, current_category, subcategory, int(count)))
                    
                elif current_category == 'Age' or current_category == 'City':
                    subcategory, female, male = row
                    cursor.execute('''
                                   INSERT INTO Summary (header_id, category, subcategory, count)
                                   VALUES(?,?,?,?)
                                   ''', (header_id, current_category, f'Female {subcategory}', int(female)))
                    cursor.execute('''
                                   INSERT INTO Summary (header_id, category, subcategory, count)
                                   VALUES(?,?,?,?)
                                   ''', (header_id, current_category, f'Male {subcategory}', int(male)))
                    
    with open(etl_file_path, newline='', encoding='utf-8') as etlfile:
        reader = csv.reader(etlfile, delimiter=',')
        
        columns = next(reader)
        columns = [col.replace('.', '_') for col in columns]
        
        columns_str = ', '.join(columns)
        placeholders = ', '.join(['?'] * (len(columns) + 1))
        sql = f'INSERT INTO Detail (header_id, {columns_str}) VALUES ({placeholders})'
        
        for row in reader:
            values = [header_id] + row
            cursor.execute(sql, values)
                    
    conn.commit()
    conn.close()
    print('data inserted')
