from newspaper import Newspaper
import sqlite3
import time
DB_NAME = "sql_post.db"
class PrintingHouse(Newspaper):
    def __init__(self,name,address) -> None:
        self.__name = name
        self.__address = address
        self.__dict_newspaper = super().get_dict_newspapers()
        self.table_name = 'printing_house'

    @property    
    def information_printinghouse(self):
        return(self.__name,self.__address,self.__dict_newspaper)
    @information_printinghouse.setter   
    def information_printinghouse(self,address):
        self.__address = address
    def get_dict_newspaper_from_prinitinghouse(self):
        return self.__dict_newspaper
    def create_table(self):
        with sqlite3.connect(DB_NAME) as sql_conn:
            sql_request = f"""CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            'Название типографий' text not null,
            'Адресс типографий' text not null,
            'Список газеты' text not null
        );"""
        sql_conn.execute(sql_request)
    def save_data(self, data):
        self.create_table()  # Создание таблицы, если её нет
        with sqlite3.connect(DB_NAME) as sql_conn:
            sql_request = f"INSERT INTO {self.table_name} VALUES(NULL,?,?,?)"
            sql_conn.execute(sql_request, data)
            sql_conn.commit()
    @staticmethod
    def show_all_table_form_printinghouse():
        with sqlite3.connect(DB_NAME) as sql_conn:
            sql_request = f"SELECT * FROM printing_house"
            for line in sql_conn.execute(sql_request):
                print(line)
    def info_printinghouse():
        list_printinghouse = []
        with sqlite3.connect(DB_NAME) as sql_conn:
            sql_request = f"SELECT * FROM printing_house"
            for line in sql_conn.execute(sql_request):
                list_printinghouse.append(line)
        return list_printinghouse
    def info_newspapers():
        list_newspapers = []
        with sqlite3.connect(DB_NAME) as sql_conn:
            sql_request = f"SELECT * FROM newspaper"
            for line in sql_conn.execute(sql_request):
                list_newspapers.append(line)
        return list_newspapers
    
    
def create_printing_house():
    house_name = input("Имя типографий: ")
    house_address = input("Адресс типографий: ")
    printinghouse = PrintingHouse(house_name,house_address)
    dict_newspapers = printinghouse.get_dict_newspaper_from_prinitinghouse()
    print(dict_newspapers)
    print()
    choose_newspapers_for_printing = int(input("Выберите номер газеты для типографий: "))
    list_of_newspapers = dict_newspapers[choose_newspapers_for_printing]
    list_of_newspapers = [str(item) for item in list_of_newspapers]
    list_of_newspapers = [house_name, house_address, ', '.join(list_of_newspapers)]  # Объединить список газет в строку
    printinghouse.save_data(list_of_newspapers)
    print("Пожалуйста подажите...")
    time.sleep(3)
    print("Данные успешно сохранено в список газеты!")
    printinghouse.show_all_table_form_printinghouse()

def find_newspapers():
    newspapers = PrintingHouse.info_newspapers()
    print("Список газетов: ".upper())
    print()
    print(newspapers)
    find_newspapers_in_list = input("Введите название газеты: ")
    printinghouses = PrintingHouse.info_printinghouse()
    found_printing_houses = []
    
    for newspaper in newspapers:
        # Проверяем, содержит ли газета искомое название
        if find_newspapers_in_list in newspaper:
            newspaper_name = newspaper[1]  # Предполагаем, что название газеты находится во втором столбце
            print(f"Газета '{newspaper_name}' найдена в следующих типографиях:")

            # Находим типографии, печатающие данную газету
            for house in printinghouses:
                newspapers_list = house[3]  # Предположим, что список газет находится в четвертом столбце
                if find_newspapers_in_list in newspapers_list:
                    found_printing_houses.append(house)
                    print(house)  # Выводим информацию о найденной типографии

    return found_printing_houses

def list_dict_printing_house():
    printinghouse_info = PrintingHouse.info_printinghouse()
    # print(printinghouse_info)
    # Преобразуем строки после четвертого элемента (индекс 3) в каждом кортеже списка
    processed_data = [tuple(data[:3]) + tuple(data[3].split(', '))for data in printinghouse_info]
    list_printing_house = ['ID','Название типографий','Адресс типографий','ID газеты', 'Название газеты','Индекс газеты','Фамилия редактора','Имя редактора','Отчества редактора','Тираж газеты','Цена газеты']
    list_processed_data_and_printing_house = []
    for i in range(len(processed_data)):
        list_processed_data_and_printing_house.append(dict(zip(list_printing_house,processed_data[i])))
    return list_processed_data_and_printing_house
def find_max():
    max_circuation = 0
    surname_max_circuation = ''
    printinghouse_info = PrintingHouse.info_printinghouse()
    print(printinghouse_info)
    # Преобразуем строки после четвертого элемента (индекс 3) в каждом кортеже списка
    processed_data = [tuple(data[:3]) + tuple(data[3].split(', '))for data in printinghouse_info]
    list_printing_house = ['ID','Название типографий','Адресс типографий','ID газеты', 'Название газеты','Индекс газеты','Фамилия редактора','Имя редактора','Отчества редактора','Тираж газеты','Цена газеты']
    list_processed_data_and_printing_house = []
    for i in range(len(processed_data)):
        list_processed_data_and_printing_house.append(dict(zip(list_printing_house,processed_data[i])))
    for i in range(len(list_processed_data_and_printing_house)):
        try:
            current_circulation = int(list_processed_data_and_printing_house[i]['Тираж газеты'])
            if current_circulation > max_circuation:
                max_circuation = current_circulation
                surname_max_circuation += list_processed_data_and_printing_house[i]['Фамилия редактора'] 
        except ValueError:  # Обработка ошибки, если преобразование в int не удалось
            print(f"Невозможно преобразовать значение '{list_processed_data_and_printing_house[i]['Тираж газеты']}' в целое число")
    print("Максимальная тираж газеты: ",max_circuation)
    print("Фамилия редактора: ",surname_max_circuation)
    
def all_price_newspapere_circuation():
    all_price_newspapers = 0
    list_dict_newspapers_printinghouse = list_dict_printing_house()
    print(list_dict_newspapers_printinghouse)
    print()
    choose_newspaper = input("Выберите название газеты для расчета общую стоимость все тиражов газеты: ")
    found_newspapers = []
    for data in list_dict_newspapers_printinghouse:
        if data['Название газеты'] == choose_newspaper:
            found_newspapers.append(data)
    for data in found_newspapers:
        all_price_newspapers = int(data['Тираж газеты'])*int(data['Цена газеты'])
    print(f"Общая стоимость газеты под названием {choose_newspaper}: ",all_price_newspapers)
