from flask import flash
from threading import Lock


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Game(metaclass=SingletonMeta):
    def __init__(self, current_row=2, current_column=0):
        self.rooms = [['', "Балкон", ''], ["Спальня", "Холл", "Кухня"], ["Подземелье", "Коридор", "Оружейная"]]
        self.current_room = self.rooms[2][0]
        self.direct = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
        self.__current_row = current_row
        self.__current_column = current_column

    def move(self, direction):
        new_row = self.__current_row + self.direct[direction][0]
        new_column = self.__current_column + self.direct[direction][1]
        if 2 >= new_row >= 0 and 2 >= new_column >= 0 and self.rooms[new_row][new_column] != '':
            self.__current_row = new_row
            self.__current_column = new_column
            self.current_room = self.rooms[new_row][new_column]
            return flash(f'Вы находитесь в комнате: {self.current_room}', category='success')
        else:
            return flash('Вы не можете попасть сюда', category='warning')



