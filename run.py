import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

def get_sales_data():
    """
    Get sales figures from the user
    """
    while True:
        print("Enter sales from last market.")
        print("We need six number, int as the number of sandwiches we got!\n as in the example: 10,20,30,40,50,60\n")
        
        data_str = input("Now enter the data please: ")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid")
            break

    return sales_data

        

def validate_data(values):
    """COnvert string in int.
    Raises ValueError if string cannot be converted into int, or if there arent't exaclty 6 value"""
    
    try:
        [int(value) for value in values]
        # could also be a for loop
        # for value in values:
        #    value = int(value)
        #    list_needed.append(value)
        if len(values) != 6:
            raise ValueError(
                f"Exaclty 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True

    
data = get_sales_data()

