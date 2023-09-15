from datetime import date


class Notes:
    __id = 0

    def __init__(self) -> None:
        Notes.__id += 1
        self.__id = Notes.__id
        self.__title = "title"
        self.__body = "body"
        self.__date = date.today()
        self.i = 0

    def __str__(self) -> str:
        return "\nid: {}\n\t{}\n{}\n\t{}\n".format(self.__id, self.__title, self.__body, self.__date)

    @property
    def getId(self) -> int:
        return self.__id

    @property
    def getTitle(self) -> str:
        return self.__title

    @property
    def getBody(self) -> str:
        return self.__body

    @property
    def getDate(self) -> date:
        return self.__date

    def setId(self, id: int):
        self.__id = id
        return self

    def setTitle(self, title: str):
        self.__title = title
        return self

    def setBody(self, body: str):
        self.__body = body
        return self

    def setDate(self, data):
        self.__date = data
        return self
