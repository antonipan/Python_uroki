import csv

def expotrer (some_list):
    with open('book.csv', 'a', encoding='utf-8') as person:
        writer = csv.writer(person, lineterminator = '\n')
        writer.writerow(some_list)