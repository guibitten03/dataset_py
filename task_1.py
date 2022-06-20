import pandas as pd


def dataset_initial() :
    my_data_set = {
        'studants' : ['Guilherme', 'Afonso', 'Maria'],
        'id' : [1,2,3]
    }

    first_test = pd.DataFrame(my_data_set)

    print(first_test)


def series() :
    column = [12,13,14]

    column_data = pd.Series(column) # Generally, the firts [0] item serie is a label
    column_label_data = pd.Series(column_data, index=["x","y","z"]) # Define labels 

    print(column_data)
    print(column_label_data)


def main():
    dataset_initial()
    series()


if __name__ == '__main__':
    main()