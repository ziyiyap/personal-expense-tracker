from setup import s
import os
import expense_functions
import time
online = True

choices_dict = {
    "1" : expense_functions.add_expense,
    "2" : expense_functions.view_all_expense,
    "3" : expense_functions.v_expense_cat,
    "4" : expense_functions.v_expense_date,
    "5" : expense_functions.month_summary,
    "6" : expense_functions.top_spending_cat,
    "7" : expense_functions.export_csv,
    "8" : expense_functions.delete_expense,
    "9" : exit
}

def display_menu():
    choice = str(input((
        """========================================
    PERSONAL EXPENSE TRACKER
========================================
1. Add new expense
2. View all expenses
3. View expenses by category
4. View expenses by date range
5. Monthly summary
6. Top spending categories
7. Export to CSV
8. Delete expense
9. Exit
========================================
Enter your choice (1-9): 
"""
    )))
    for k,v in choices_dict.items():
        if choice.strip() == k:
            v()
            return
    print("Invalid choice")
    time.sleep(1)
    return
while online:
    os.system('cls')
    display_menu()