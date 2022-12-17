import csv

def impoter (find_str):
    with open('book.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for el in row:
                if el == find_str:
                    return row
        else:
            print('В справочнике этого нет')