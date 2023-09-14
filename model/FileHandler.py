import os.path as path1

from model.GBNotes import GBNotes
from model.Notes import Notes
import csv


class FileHandler:
    __counter = 0

    def __init__(self, directory: str) -> None:
        self.__directory = directory

    def export_file(self, notes_list: list, file_name: str) -> None:
        result = []
        full_name = path1.join(self.__directory, file_name + ".txt")
        try:
            with open(full_name, mode='w', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                for item in notes_list:
                    result = [item.getId, item.getTitle, item.getBody, item.getDate]
                    writer.writerow(result)
            file.close()
        except: raise

    def import_file(self, file_name: str) -> GBNotes:
        """

        :rtype: object
        """
        result = GBNotes()
        full_name = path1.join(self.__directory, file_name)
        try:
            with open(full_name) as file:
                reader = csv.reader(file)
                for row in reader:
                    temp = str(row).replace('[', '').replace(']', '').replace('\'', '').split(';')
                    if temp != ['']:
                        print(temp)
                        bufer: Notes = Notes()
                        bufer.setId(temp[0]).setTitle(temp[1]).setBody(temp[2]).setDate(temp[3])
                        result.add(bufer)
            file.close()
            return result
        except: raise

    def __str__(self) -> str:
        return self.__directory

# FileHandler(path1.abspath(path1.dirname(__file__)))
