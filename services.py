import sqlite3
import pandas as pd
from database import connect
from datetime import datetime
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typeDef():
    while True:
        try:
            type = input("Select the type: Revenue or Expense: ").strip().lower()

            if type not in ["revenue", "expense"]:
                raise ValueError("Wrong type or incomplete")

            return type
        
        except:
            print("Error! \nEnter the right type: 'Revenue' or 'Expense'")

def valueDef():
    while True:
        try:
            value = float(input("Insert the value: "))

            if value <= 0:
                raise ValueError("Value incorrect!")
            
            return value
        
        except:
            print("Error!\nEnter a valid value: ")

def categoryDef():
    category = input("Enter the category of the launch: ").lower()

    return category

def dateDef():
    while True:
        try:
            userAnswer = input("Enter the date (MM/DD/YYYY): ")
            date = datetime.strptime(userAnswer, "%m/%d/%Y").date()

            return date

        except ValueError:
            print("Invalid date! Try again.")

def descriptionDef():
    description = input("Enter the description of launch: ")

    return description

def insert_launch(type, value, category, date, description):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO launch (type, value, category, date, description)
        VALUES (?, ?, ?, ?, ?)
    """, (type.lower(), value, category, date, description))

    conn.commit()
    conn.close()

def launch_list():
    conn = connect()
    df = pd.read_sql("SELECT * FROM launch", conn)
    conn.close()

    return df

def balance_calc():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            SUM(CASE WHEN LOWER(type) = 'revenue' THEN value ELSE 0 END) -
            SUM(CASE WHEN LOWER(type) = 'expense' THEN value ELSE 0 END)
        FROM launch
    """)

    balance = cursor.fetchone()[0] or 0
    conn.close()

    return balance

def delete_launch_sql(launch_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM launch WHERE idLaunch = ?", (launch_id,))

    conn.commit()
    conn.close()

    return cursor.rowcount  # retorna quantas linhas foram apagadas

def delete_launch_ui():
    df = launch_list()

    if df.empty:
        print("Não há lançamentos cadastrados.")
        return
    
    print("\nLançamentos:\n")
    print(df)

    while True:
        try:
            row = int(input("How many rows you wanna delete: "))

            if row > len(df) or row < 1:
                print("The number of rows typed is bigger than rows in launch list or invalid")

            else:
                i = 0
                while i < row:
                    try:
                        launch_id = int(input("\nDigite o ID do lançamento que deseja deletar: ").strip())

                    except ValueError:
                        print("ID inválido. Digite um número.")
                        continue

                    result = delete_launch_sql(launch_id)

                    if result > 0:
                        print("Lançamento deletado com sucesso!\n")

                    else:
                        print("Nenhum lançamento encontrado com esse ID.")
                    i += 1
            
            break
                    
        except ValueError:
            print("Type a valid number")
            continue

        

        

        
    
