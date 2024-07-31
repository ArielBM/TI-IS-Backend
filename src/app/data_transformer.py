import json
import pandas as pd

def save_data_as_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f)
    print(f'Data saved as {file_path}')
    
def transform_data_to_csv(data,file_path):
    df = pd.json_normalize(data)
    df.to_csv(file_path, index=False)
    print(f'Data transformed to CSV at {file_path}')

def create_summary_csv(data, file_path):
    df = pd.DataFrame(data)

    df['gender'] = df['gender'].apply(lambda x: x if x in ['male', 'female'] else 'other')

    total_records = len(df)

    gender_summary = df.groupby('gender').size().reset_index(name='total')
    gender_summary.columns = ['gender', 'total']
    total_row = pd.DataFrame({'gender': ['registre'], 'total': [total_records]})
    summary_df = pd.concat([total_row, gender_summary], ignore_index=True)

    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, float('inf')]
    labels = ["00-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90", "91+"]
    df['age'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
    age_gender_summary = df.pivot_table(index='age', columns='gender', aggfunc='size', fill_value=0)
    age_gender_summary = age_gender_summary.reset_index()

    df['city'] = df['address'].apply(lambda x: x.get('city') if isinstance(x, dict) else None)

    city_gender_summary = df.pivot_table(index='city', columns='gender', aggfunc='size', fill_value=0)
    city_gender_summary = city_gender_summary.reset_index()

    df['os'] = df['userAgent'].apply(detect_os)
    os_summary = df.groupby('os').size().reset_index(name='total')

    with open(file_path, 'w', newline='') as f:

        f.write(f'registre,{total_records}\n')
        f.write('gender,total\n')
        summary_df.iloc[1:].to_csv(f, index=False, header=False)

        f.write('\n')

        age_gender_summary.to_csv(f, index=False)

        f.write('\n')

        city_gender_summary.to_csv(f, index=False)

        f.write('\n')

        os_summary.to_csv(f, index=False)
    
    print(f'Summary CSV created at {file_path}')
    
def detect_os(user_agent):
    if 'Windows' in user_agent:
        return 'Windows'
    elif 'Macintosh' in user_agent or 'Mac OS' in user_agent:
        return 'MacOS'
    elif 'Linux' in user_agent:
        return 'Linux'
    elif 'Android' in user_agent:
        return 'Android'
    elif 'iPhone' in user_agent or 'iPad' in user_agent:
        return 'iOS'
    else:
        return 'Other'