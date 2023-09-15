from datetime import date
from time import mktime

from model.FileHandler import FileHandler
from model.InputData import *
from model.Notes import Notes


class UserController:
    def __init__(self):
        self.__file_handler = None
        self.__note_list = []

    def creator_file_directory(self, path: str) -> None:
        self.__file_handler = FileHandler(path)

    def getInputNumber(self) -> int:
        try:
            return inputNumber()
        except:
            raise

    def importFile(self) -> None:
        flag = True
        while flag:
            file_name = inputFileName()
            try:
                self.__note_list = self.__file_handler.import_file(file_name)
                self.__reID()
            except FileNotFoundError:
                print("Не удалось найти файл! ")
            else:
                print("Импортирование прошло успешно! ")
                flag = False

    def exportFile(self):
        flag = True
        while flag:
            file_name = inputFileName()
            try:
                self.__file_handler.export_file(self.__note_list, file_name)
            except Exception:
                print("Что-то пошло не так!  ")
            else:
                print("Экспортирование прошло успешно! ")
                flag = False

    def createNewNotes(self) -> None:
        newNotes = Notes()
        newNotes.setTitle(getInputTitle())
        newNotes.setBody(getInputBody())
        self.__note_list.append(newNotes)
        self.__reID()

    def readNotes(self) -> str:
        flag = True
        while flag:
            idx = inputNumber()
            if 0 < idx < len(self.__note_list):
                return self.__note_list.__getitem__(idx)
            else:
                print("Выход за пределы списка записок! ")


    def updateNotes(self) -> None:
        flag = True
        while flag:
            idx = inputNumber()
            if 0 < idx < len(self.__note_list):
                print(self.__note_list[idx].getTitle)
                print("Изменить на: ")
                self.__note_list[idx].setTitle(getInputTitle())
                print(self.__note_list[idx].getBody)
                print("Изменить на: ")
                self.__note_list[idx].setBody(getInputBody())
                self.__note_list[idx].setDate(date.today())
                flag = False
            else:
                print("Выход за пределы списка записок! ")

    def deleteNotes(self) -> None:
        flag = True
        while flag:
            idx = inputNumber()
            if 0 < idx < len(self.__note_list):
                self.__note_list.pop(idx)
                self.__reID()
                flag = False
            else:
                print("Выход за пределы списка записок! ")

    def readAll(self) -> None:
        for notes in self.__note_list:
            print(notes)

    def __reID(self) -> None:
        for idx in range(len(self.__note_list)):
            self.__note_list[idx].setId(idx)

    def selectDate(self) -> None:
        day = inputDate()
        result = []
        for notes in self.__note_list:
            if date.fromisoformat(notes.getDate) >= date.fromtimestamp(mktime(day)):
                result.append(notes)
        for notes in result:
            print(notes)
