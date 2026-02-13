from setup import s
import expense_functions
s()

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

display_menu()