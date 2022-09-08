import csv

def csv_writer(file):
    with open(file, 'w', newline='') as csvfile:
        field_names = ['Name', 'SecondName']
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        dict_with_values = {
            'Name' : 'Jean-Luc',
            'SecondName' : 'Picard'
        }
        writer.writerow(dict_with_values)

def csv_reader(file):
    with open(file, 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i in spamreader:
            print(i)

if __name__ == '__main__':
    csv_writer('file.csv')
    csv_reader('file.csv')
    print('done')