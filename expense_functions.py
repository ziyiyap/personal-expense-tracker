import json
import setup
from datetime import datetime, date
import time
import os
import csv
import statistics

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
    sum_of_amount = sum(log['amount'] for log in log_dic)
    print(f'Total: RM{sum_of_amount}')
    _ = input('')
    return 

def v_expense_cat():
    os.system('cls')
    print('=' * 60, ' ALL EXPENSES ', '=' *60)
    string_format = '{:<27} {:<27} {:<27} {:<27} {:<27}'
    header = ['ID', 'Date', 'Category', 'Amount', 'Description']
    data = [[log['id'], log['date'], log['category'], f"RM{log['amount']}", log['description']] for log in log_dic]
    dataa = sorted(data, key=lambda x: x[2])
    data_slice = [list(map(lambda x: x[:27], ls)) for ls in dataa]
    view_header = string_format.format(*header)
    print(view_header)
    print('-'*135)
    for elements in data_slice:
        print(string_format.format(*elements))
        
    print('=' * 135)
    sum_of_amount = sum(log['amount'] for log in log_dic)
    print(f'Total: RM{sum_of_amount}')
    _ = input('')
    return 

def v_expense_date():
        os.system('cls')
        print('=' * 60, ' ALL EXPENSES ', '=' *60)
        string_format = '{:<27} {:<27} {:<27} {:<27} {:<27}'
        header = ['ID', 'Date', 'Category', 'Amount', 'Description']
        data = [[log['id'], log['date'], log['category'], f"RM{log['amount']}", log['description']] for log in log_dic]
        dataa = sorted(data, key=lambda x:x[1])
        data_slice = [list(map(lambda x: x[:27], ls)) for ls in dataa]
        view_header = string_format.format(*header)
        print(view_header)
        print('-'*135)
        for elements in data_slice:
            print(string_format.format(*elements))
            
        print('=' * 135)
        sum_of_amount = sum(log['amount'] for log in log_dic)
        print(f'Total: RM{sum_of_amount}')
        _ = input('')
        return 

def month_summary():
    no_row = 0
    sum_ls = []
    category = {}
    os.system('cls')
    ask_user = str(input("Enter the month and the year:\n Ex. 02/26\n")) #03/26
    convert_text = datetime.strptime(ask_user, '%m/%y').strftime('%b_%y').lower()
    for csv_files in setup.exports.iterdir():
        if csv_files.name == f"{convert_text}.csv":
            with open(csv_files) as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    if no_row == 0:
                        no_row +=1
                        continue
                    if row[1] not in category:
                        category[row[1]] = float(row[3])
                    else:
                        category[row[1]] += float(row[3])
                    sum_ls.append(float(row[3]))
                    no_row +=1
    sum_of_amount = sum(sum_ls)
    os.system('cls')
    print(f"{'-' * 75}\n{'MONTHLY SUMMARY'.center(75)}\n{'-'*75}")
    print(f"Total spending: RM{sum_of_amount}\nAverage expense: RM{round(statistics.mean(category.values()),2)}")
    print()
    print(f'Breakdown by category:\n{'-' * 75}')
    str_format = '{:<25} {:<25} {:<25}'
    for k,v in category.items():
        ls = [k,f"RM{v}",f"({round(v/sum_of_amount * 100, 2)}%)"]
        print(str_format.format(*ls))
    print('-'*75)

    _ = input('')
    return

def top_spending_cat():
    os.system('cls')   
    print('=' * 78)
    string_format = '{:<23} {:<25} {:<25}'
    print(string_format.format(*['Category','Amount','Percentage']))
    print('=' * 78)
    category_json = {}
    for e in log_dic:
        if e['category'] not in category_json:
            category_json[e['category']] = e['amount']
        else:
            category_json[e['category']] += e['amount']
    sum_of_category = sum(category_json.values())
    ls = [[f"{category}",f'RM{v}',f'{round(v/sum_of_category * 100,2)}%'] for category,v in category_json.items()]
    sorted_ls = sorted(ls, key=lambda x: float(x[2].rstrip('%')), reverse=True)
    for i,l in enumerate(sorted_ls):
        l[0] = f"{i+1}. {l[0]}"
    for category in sorted_ls:
        print(string_format.format(*category))
    _ = input('')     
    return

def delete_expense():
    os.system('cls')
    ask_id = str(input("Enter ID: "))
    for i, dict in enumerate(log_dic):
        if dict['id'] == ask_id.strip():
            log_dic.pop(i)
            upload_json()
            export_csv()
            print(f'✓ Expense removed successfully!')
            time.sleep(3)
            return
    print("ID not found")
    time.sleep(1)
    return
