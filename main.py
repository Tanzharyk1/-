from newspaper import Newspaper
from printing_house import PrintingHouse,create_printing_house,find_newspapers,find_max,all_price_newspapere_circuation
print("*************************************************************************************")
print("* 1.CОЗДАТЬ ГАЗЕТУ                                                                  *")
print("* 2.СВЕДЕНИЯ О ГАЗЕТАХ                                                              *")
print("* 3.ИЗМЕНИТЬ СУЩЕСТВУЮЩИХ ДАННЫХ ИЗ ГАЗЕТЫ                                          *")
print("* 4.СОЗДАТЬ ТИПОГРАФИЮ                                                              *")
print("* 5.СВЕДЕНИЯ О ТИПОГРАФИЯХ                                                          *")
print("* 6.НАЙТИ ТИПОГРАФИЮ ПО НАЗВАНИЮ ГАЗЕТЫ                                             *")
print("* 7.ФАМИЛИЯ РЕДАКТОРА ГАЗЕТЫ,КОТОРАЯ ПЕЧАТАЕТЬСЯ В ТИПОГРАФИЙ САМЫМ БОЛЬШИМ ТИРАЖОМ *")
print("* 8.Общая стоимость цены  *")
print("*************************************************************************************")
print()


while True:
    choose_services = int(input("Выберите тип услуги: "))
    if choose_services==1:
        #Информация о газеты.
        newspaper_name = input("Название газеты: ")
        newspaper_index = int(input("Индекс газеты: "))
        newspaper_author_first_name = input("Фамилия редактора: ")
        newspaper_author_last_name = input("Имя редактора: ")
        newspaper_author_third_name = input("Отчества редактора: ")
        newspaper_edition = int(input("Сколько тиражов: "))
        newspaper_price = int(input("Цена одного газеты: "))

        newspaper_data = Newspaper(newspaper_name,newspaper_index,newspaper_author_first_name,newspaper_author_last_name,newspaper_author_third_name,newspaper_edition,newspaper_price)
        newspaper_data.create_table()
        data = [newspaper_data.information]
        newspaper_data.save_data(data)
    
    if choose_services==2:
        Newspaper.show_all_newspapers()
    if choose_services==3:
        Newspaper.update_newspaper_data()
    if choose_services==4:
        create_printing_house()
    if choose_services==5:
        PrintingHouse.show_all_table_form_printinghouse()
    if choose_services==6:
        # Пример использования функции find_newspapers():
        found_houses = find_newspapers()
        if not found_houses:
            print("Газета не найдена ни в одной типографии.")
    if choose_services==7:
        find_max()
    if choose_services==8:
        all_price_newspapere_circuation()
    if choose_services==0:
        break

    

