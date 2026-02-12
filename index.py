from database import create_tables
from services import insert_launch, launch_list, balance_calc, typeDef, valueDef, categoryDef, dateDef, descriptionDef, clear, delete_launch_ui
import time


op = ""
last_op = ""
create_tables()
print("Welcome to MY FINANCE CONTROL!!\n")

while op != "exit" or last_op != "exit":
    print("\nMY FINANCE CONTROL!!\n")
    print("Choose one of this options")
    time.sleep(1)
    print("\n-------- MENU --------\n\n" \
    "- INSERT NEW LAUNCH (type: insert)\n" \
    "- VIEW FINANCIAL SUMMARY (type: summary)\n" \
    "- VIEW LAUNCHS LIST(type: list)\n" \
    "- DELETE LAUNCH (type: delete)\n" \
    "- EXIT (type: exit)\n")
    time.sleep(1)
    op = input("Type the function that you wanna make: ").strip().lower()
    match op:
        case "insert":
            print("\n-------- NEW LAUNCH --------\n")
            type = typeDef()
            value = valueDef()
            category = categoryDef()
            date = dateDef()
            description = descriptionDef()

            insert_launch(type, value, category, str(date), description)
            print("Launch succesfully registered")
            time.sleep(4)
            clear()

        case "summary":
            print("\n-------- FINANCIAL SUMMARY --------\n")
            balance = float(balance_calc())

            print("Current balance", f"R$ {balance:.2f}")
            time.sleep(4)
            clear()

        case "list":
            print("\n-------- LAUNCHS --------\n")
            df = launch_list()
            print(f"Your launch list: \n{df}")
            time.sleep(4)

        case "delete":
            print("\n-------- DELETING LAUNCHS --------\n")
            delete_launch_ui()

        case "exit":
            print("Thanks for access MY FINANCE CONTROL")
            time.sleep(4)
            clear()
            break

        case _:
            print("Invalid option!\nTry again")
            time.sleep(4)
            clear()











