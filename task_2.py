import pandas as pd
from psutil import users


def main() :
    print("User demographic information")

    try:
        path = "ml-100k/u.user"

        dataset = pd.read_csv(path, delimiter="|")

        dataset = dataset[dataset.columns[1:2]]

        dataset.plot(kind="bar" ,x="user", y="age")
    except:
        print("Could not open the file or use dataset.")

if __name__ == '__main__' :
    main() 