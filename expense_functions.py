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
    #feb_expenses.csv
    export_dir = setup.exports
    for log in log_dic:
        current_date = log['date'] #2026-02-05
        d_month = datetime.strptime(current_date, "%Y-%m-%d")  #2026-02-05
        month_year = d_month.strftime("%b_%y").lower() #feb_26
        file_dir = export_dir / f"{month_year}_expenses.csv"
        file_exists = file_dir.exists()
        with open(file_dir,'a',newline='') as file: #feb_26_expenses.csv
            write_csv = csv.writer(file)
            if not file_exists:
                write_csv.writerow(["Date","Category","Description","Amount"])
            write_csv.writerow([log['date'], log['category'], log['description'], log['amount']])


def add_expense():
    os.system('cls')
    print(log_dic)
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
    print(
        """==================== ALL EXPENSES ====================
ID           Date         Category         Amount    Description
------------ ------------ ---------------- --------- ---------------------------"""
    )


    print(
        """======================================================"""
    )
    time.sleep(2)
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
