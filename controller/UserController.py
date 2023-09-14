from model.FileHandler import FileHandler
from model.GBNotes import GBNotes
from model.Notes import Notes

class UserController:
    def __init__(self):
        self.__file_handler = None
        self.__note_list = GBNotes()

    def creator_file_directory(self, path: str) -> None:
        self.__file_handler = FileHandler(path)
