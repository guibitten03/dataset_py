from unicodedata import numeric
from numpy import number
import pandas as pd


def db_GetUsers ():
    try:
        path = "ml-100k/u.user"

        user_database = pd.read_csv(path, delimiter="|")

        number_users = user_database.shape[0]

        print("Numbers of users: ", number_users)
    except:
        print("Could not open the file.")


def db_GetItems () :
    try:
        path = "ml-100k/u.item"

        user_database = pd.read_csv(path)
    except:
        print("Could not open the file.")
        

def main():
    print("1: Num of users \n 2: Num of items\n 3: Sparcity of datasets")
    input_option = int(input())

    if (input_option == 1) :
        db_GetUsers()
    elif (input_option == 2) :
        db_GetItems()
    #elif (input_option == 3) :
        #db_GetSparcity()


if __name__ == '__main__':
    main()

