import time
import os
import datetime


class SpecialDate:
    def modify_date(path):
        file_date = time.ctime(os.path.getmtime(path))
        file_date = datetime.datetime.strptime(file_date, "%a %b %d %H:%M:%S %Y")
        return file_date.strftime("%d-%m-%Y %H:%M:%S")