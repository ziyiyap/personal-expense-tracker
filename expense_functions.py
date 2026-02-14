import json
import setup
from datetime import datetime

log = []

def upload_json():
    with open(setup.expenses_json,'w', encoding='utf-8') as f:
        json.dump(log,f,indent=4)
    return

def add_expense():
    try:
        amount = float(input("Enter amount: "))
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
            return
        else:
            pass
        #eg. 26214105812
        id = datetime.now().strftime("%y%m%d%H%M%S")
        log.append({"id": id, "amount":amount,"category":category,"description":description,"date":date})
        print(log)
        upload_json()
        return
    
def view_all_expense():
    return

def v_expense_cat():
    return

def v_expense_date():
    return

def month_summary():
    return

def top_spending_cat():
    return

def export_csv():
    return

def delete_expense():
    return

def load_expenses():
    with open(setup.expenses_json, encoding='utf-8') as f:
        expenses_dic = json.load(f)
    return expenses_dic
