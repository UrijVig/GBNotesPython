from model.Notes import Notes


class GBNotes:

    def __init__(self) -> None:
        self.__data = []

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

    def read(self,idx: int) -> str:
        return str(self.__data[idx])