import json
import setup

def add_expense():
    return

def load_expenses():
    with open(setup.expenses_json, encoding='utf-8') as f:
        expenses_dic = json.load(f)
    return expenses_dic
