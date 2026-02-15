import json
import setup
from datetime import datetime
import time
import os
import csv
from pathlib import Path

setup.s()
with open(setup.expenses_json, encoding='utf-8') as f:
    log_dic = json.load(f)



def upload_json():
    with open(setup.expenses_json,'w', encoding='utf-8') as f:
        json.dump(log_dic,f,indent=4)
    return

def export_csv():
    monthyear_data = {}
    export_dir = setup.exports
    if log_dic == []:
        print("Nothing to export")
        time.sleep(2)
        return
    else:
        for log in log_dic:
            current_date_str = log['date']
            strptime_date = datetime.strptime(current_date_str, "%Y-%m-%d")
            strftime_date = strptime_date.strftime('%b_%y').lower()
            if strftime_date not in monthyear_data:
                monthyear_data[strftime_date] = []
            monthyear_data[strftime_date].append([log['date'],log['category'],log['description'],log['amount']])
        for k,v in monthyear_data.items():
            csv_file = export_dir / f"{k}.csv"
            with open(csv_file, 'w',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date','Category','Description','Amount'])
                for data in v:
                    writer.writerow(data)
        print(f"Successfully exported {len(monthyear_data.keys())} files")
        time.sleep(2)
        return

def add_expense():
    os.system('cls')
    try:
        amount = round(float(input("Enter amount: ")),2)
    except ValueError as e:
        print(e)
        return
    else:
        category = str(input("Enter category: "))
        description = str(input("Enter description: "))
        date = str(input("Enter date (YYYY-MM-DD) or press Enter for today: "))
        if date.strip() == '':
            date = datetime.now().strftime("%Y-%m-%d")
        elif len(date) != 10:
            print("Invalid date format")
            time.sleep(1)
            return
        else:
            pass
        #eg. 26214105812
        id = datetime.now().strftime("%y%m%d%H%M%S")
        log_dic.append({"id": id, "amount":amount,"category":category,"description":description,"date":date})
        print()
        print(f"✓ Expense added successfully!\nID: {id}")
        upload_json()
        export_csv()
        time.sleep(3)
        return
    
def view_all_expense():
    os.system('cls')
    print('=' * 60, ' ALL EXPENSES ', '=' *60)
    string_format = '{:<27} {:<27} {:<27} {:<27} {:<27}'
    header = ['ID', 'Date', 'Category', 'Amount', 'Description']
    data = [[log['id'], log['date'], log['category'], f"RM{log['amount']}", log['description']] for log in log_dic]
    data_slice = [list(map(lambda x: x[:27], ls)) for ls in data]
    view_header = string_format.format(*header)
    print(view_header)
    print('-'*135)
    for elements in data_slice:
        print(string_format.format(*elements))
        
    print('=' * 135)
    _ = input('')
    return

def v_expense_cat():
    os.system('cls')
    return

def v_expense_date():
    os.system('cls')
    return

def month_summary():
    os.system('cls')
    return

def top_spending_cat():
    os.system('cls')
    return

def delete_expense():
    os.system('cls')
    return
