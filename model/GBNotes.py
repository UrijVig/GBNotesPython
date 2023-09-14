from typing import Type

from model.FileHandler import FileHandler
from model.Notes import Notes


class GBNotes:

    def __init__(self) -> None:
        self.__data = []
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num

    def __str__(self) -> str:
        result = ""
        for item in self.__data:
            result += str(item)
        return result

    def add(self, item: Notes) -> None:
        self.__data.append(item)

    def delete(self, item: Notes) -> None:
        self.__data.remove(Notes)

    def pop(self, idx: int) -> None:
        self.__data.pop(idx)

    def insert(self, idx: int, item: Notes) -> None:
        self.__data.insert(idx, item)

    def read(self, idx: int) -> str:
        return str(self.__data[idx])

    def getLen(self) -> int:
        return len(self.__data)

    def update(self, idx, item: Notes) -> None:
        self.__data[idx] = item


import os.path as path1
gblist: Type[GBNotes] = GBNotes
fil = FileHandler(path1.abspath(path1.dirname(__file__)))
gblist = fil.import_file("test.txt")
gblist[1].read