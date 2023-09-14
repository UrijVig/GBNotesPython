from controller.UserController import UserController
import os.path as path1


class UserView:
    def __init__(self):
        self.controller = UserController()

    def run(self) -> None:
        print("Добро пожаловать в приложение для создания записок! ")
        print("Для начала настроим корневую папку сохранения файлов ")
        default_dir = path1.abspath(path1.dirname(__file__))
        print(f"{default_dir} - папка по умолчанию!")
        print("Введите новый путь, чтобы изменить папку для сохранения, чтобы продолжить нажмите Enter! ")
        temp = input()
        if temp != '':
            print("Введите новый путь")
            self.controller.creator_file_directory(temp)

        else:
            self.controller.creator_file_directory(default_dir)

    def output(self, massage: str) -> None:
        print(massage)


user = UserView()
user.run()
