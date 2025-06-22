from clients.client_repository import MySQLClientDAO
from accounts.account_repository import MySQLAccountDAO
from transactions.transaction_repository import MySQLTransactionDAO
from services.client_service import *
from services.account_service import *
from services.transaction_service import *
from utils.menus import Menu, main_menu, customer_menu, account_menu, movements_menu
import os

def main():
    while True:
        option = main_menu.choose()
        clear_terminal()
        match option:
            case 1:
                option_customer = customer_menu.choose()
                choice_customer(option_customer)
            case 2:
                option_account = account_menu.choose()
                choice_account(option_account)
            case 3:
                option_movements = movements_menu.choose()
                choice_movements(option_movements)
            case 4:
                exit()
            
def choice_customer(option):
    mysql_customer = MySQLClientDAO()
    mysql_account = MySQLAccountDAO()
    try:
        match option:
            case 1:
                ask_client_data(mysql_customer)
            case 2:
                update_client_data(mysql_customer)
            case 3:
                ask_customer_deregister_client(mysql_customer, mysql_account)
            case 4:
                ask_customer_release_client(mysql_customer)
            case 5:
                show_clients(mysql_customer)
            case 6:
                return
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}\n")

def choice_account(option):
    mysql_customer = MySQLClientDAO()
    mysql_account = MySQLAccountDAO()
    mysql_movements = MySQLTransactionDAO()
    try:
        match option:
            case 1:
                create_current_account(mysql_account)
            case 2:
                open_current_account(mysql_account, mysql_customer)
            case 3:
                close_current_account(mysql_account)
            case 4:
                consult_balance(mysql_account)
            case 5:
                deposit_money(mysql_account)
            case 6:
                withdraw_money(mysql_account)
            case 7:
                transfer_money(mysql_account)
            case 8:
                show_all_accounts(mysql_account)
            case 9:
                return
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}\n")

def choice_movements(option):
    mysql_account = MySQLAccountDAO()
    mysql_movements = MySQLTransactionDAO()
    try:
        match option:
            case 1:
                try:
                    consult_balance(mysql_account)
                except Exception as e:
                    print(f"\n❌ Error al consultar el saldo: {e}\n")
            case 2:
                get_movements_betweeen_date(mysql_movements)
            case 3:
                deposit_money(mysql_account)
            case 4:
                withdraw_money(mysql_account)
            case 5:
                transfer_money(mysql_account)
            case 6:
                return
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}\n")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()