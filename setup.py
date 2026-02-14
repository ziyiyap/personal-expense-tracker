from pathlib import Path
import os
import time
import json

data_dir = Path(r"./personal-expense-tracker/data")
exports = data_dir / "exports"
expenses_json = data_dir / 'expenses.json'

def s():
    if data_dir.exists():
        return
    else:
        data_dir.mkdir()
        exports.mkdir(parents=True, exist_ok=True)
        expenses_json.touch()
        print("Folder created!")
        with open(expenses_json, 'w', encoding='utf-8') as f:
            json.dump([],f,indent=4)
            print('JSON created')
        time.sleep(1)
        os.system('cls')
        return