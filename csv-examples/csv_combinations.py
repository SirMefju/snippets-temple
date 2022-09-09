import csv
import os
import time
import datetime


class CsvCombinations:
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
            results = []
            for i in spamreader:
                dict_with_results = {
                    'Name' : i[0],
                    'SecondName' : i[1]
                }
                results.append(dict_with_results)
            for i in results:
                print(i)
                print(i['Name'])

    def modify_date(path):
        file_date = time.ctime(os.path.getmtime(path))
        file_date = datetime.datetime.strptime(file_date, "%a %b %d %H:%M:%S %Y")
        return file_date.strftime("%d-%m-%Y %H:%M:%S")


if __name__ == '__main__':
    CsvCombinations.csv_writer('csv-examples/file.csv')
    CsvCombinations.csv_reader('csv-examples/file.csv')
    file_modify_time = CsvCombinations.modify_date('csv-examples/file.csv')
    file_size = os.path.getsize('csv-examples/file.csv')
    print("File modify time: " + str(file_modify_time))
    print("File size: " + str(file_size) + " B")