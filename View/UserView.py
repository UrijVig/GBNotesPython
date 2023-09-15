from controller.UserController import UserController
import os.path as path1


class UserView:
    def __init__(self):
        self.controller = UserController()

    def run(self) -> None:
        action = None
        print("Добро пожаловать в приложение для создания записок! ")
        print("Для начала настроим корневую папку сохранения файлов ")
        default_dir = path1.abspath(path1.dirname(__file__))
        print(f"Ваши заметки будутсохранены здесь: {default_dir}")
        self.controller.creator_file_directory(default_dir)
        flag: bool = True
        while flag:
            print("Выберите действие: ")
            print("Импортировать файл заметок - 1")
            print("Создать новую заметку - 2")
            print("Прочитать записку - 3")
            print("Изменить записку - 4")
            print("Удалить записку - 5")
            print("Показать все записки - 6")
            print("Сделать выборку по дате - 7")
            print("Экспортировать файл заметок - 8")
            print("Завершить работу программы - 0")
            action_flag: bool = True
            while action_flag:
                try:
                    action = self.controller.getInputNumber()
                    if action < 0 or action > 7:
                        print("Число не соответсвует диапозону!")
                    else:
                        action_flag = False
                except Exception:
                    print("Введены некорректные данные!")
            if action == 1:
                self.controller.importFile()
            if action == 2:
                self.controller.createNewNotes()
                print("Создана новая запись")
            if action == 3:
                print("Чтение записки под номером: ")
                print(self.controller.readNotes())
            if action == 4:
                print("Изменение записки под номером: ")
                self.controller.updateNotes()
            if action == 5:
                print("Удаление записки под номером: ")
                self.controller.deleteNotes()
            if action == 6:
                self.controller.readAll()
            if action == 7:
                self.controller.selectData()
            if action == 8:
                self.controller.exportFile()
            if action == 0:
                flag = False

    def output(self, massage: str) -> None:
        print(massage)



