import sqlite3
import time
DB_NAME = "sql_post.db"
class Newspaper:
    def __init__(self,name,index,author_first_name,author_last_name,author_third_name,edition,price) -> None:

        self.__name = name
        self.__index = index
        self.__author_first_name = author_first_name        
        self.__author_last_name = author_last_name        
        self.__author_third_name = author_third_name
        self.__edition = edition
        self.__price = price
        self.table_name = 'newspaper'
    
    @property
    def information(self):
        return (self.__name,self.__index,self.__author_first_name,self.__author_last_name,self.__author_third_name,self.__edition,self.__price)
    @information.setter        
    def information(self,price) -> None:
        self.__price = price 
    def create_table(self):
        with sqlite3.connect(DB_NAME) as sql_conn:
            sql_request = f"""CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            'Название газеты' text not null,
            'Индекс газеты' integer,
            'Фамилия редактора' text not null,
            'Имя редактора' text not null,
            'Отчества редактора' text not null,
            'Тираж газеты'  integer,
            'Цена газеты' integer
        );"""
        sql_conn.execute(sql_request)
    def save_data(self, data):
        self.create_table()  # Создание таблицы, если её нет
        with sqlite3.connect(DB_NAME) as sql_conn:
            sql_request = f"INSERT INTO {self.table_name} VALUES(NULL,?,?,?,?,?,?,?)"
            sql_conn.executemany(sql_request, data)
            sql_conn.commit()
    @staticmethod
    def show_all_newspapers():
        with sqlite3.connect(DB_NAME) as sql_conn:
            sql_request = "SELECT * FROM newspaper"
            for line in sql_conn.execute(sql_request):
                print(line)
    @staticmethod
    def get_dict_newspapers():
        count_newspapers = 0
        newspapers_list = []
        with sqlite3.connect(DB_NAME) as sql_conn:
            sql_request = "SELECT * FROM newspaper"
            for line in sql_conn.execute(sql_request):
                count_newspapers = len(list(line))
                newspapers_list.append(line)
        count_newspapers_list = []
        for i in range(count_newspapers):
            count_newspapers_list.append(i+1)
        dict_newspaper = dict(zip(count_newspapers_list,newspapers_list))
        return dict_newspaper
    @staticmethod
    def update_newspaper_data():
        dict_newspaper = Newspaper.get_dict_newspapers()
        print(dict_newspaper)
        print()
        choose_number_newspapers = int(input("Выберите номер газеты для изменения данных: "))
        selected = list(dict_newspaper[choose_number_newspapers])
        print()
        print("*******************************************************************")
        print("Данные выбранного таблицы".upper())
        print()
        newspapers_table_columns_name = ["ID","Название газеты","Индекс газеты","Фамилия редактора","Имя редактора","Отчества редактора","Тираж газеты","Цена газеты"]   
        for i in range(len(list(zip(newspapers_table_columns_name,selected)))):
            for j in range(len(list(zip(newspapers_table_columns_name,selected))[i])):

                print(list(zip(newspapers_table_columns_name,selected))[i][j],end = " ")
            print()
        print("*******************************************************************")
        
        print()
        for i in range(len(newspapers_table_columns_name)):
            print(i+1,newspapers_table_columns_name[i])
        print()
        
        update_number = int(input("Выберите номер столбца таблицы для изменения данного таблицы: "))
        
        # Ввод новых данных
        update_columns = input(f"Введите новые данные для {newspapers_table_columns_name[update_number-1]}: ")
        # Определяем имя столбца, который нужно обновить
        columns_to_update = newspapers_table_columns_name[update_number-1]
        with sqlite3.connect(DB_NAME) as sql_conn:
            # Обновление конкретного столбца в таблице
            sql_request = f"UPDATE newspaper SET '{columns_to_update}' = '{update_columns}' WHERE id = '{choose_number_newspapers}'"
            # Предполагая, что выбранное значение строки имеет id = update_number
            sql_conn.execute(sql_request)
            sql_conn.commit()
        print("Пожалуйста подождите...")
        time.sleep(3)
        print("Данные успешно сохранены!")
        Newspaper.show_all_newspapers()
    
