import pandas as pd
from psutil import users


def pie_plot():
    


def main() :
    print("User demographic information")
    x = int(input("1 : Graphic by age \n 2 : Graphic by gender"))

    try:
        if (x == 1) :
            pie_plot()

    except:
        print("Could not open the file or use dataset.")

if __name__ == '__main__' :
    main() 