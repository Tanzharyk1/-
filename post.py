from printing_house import PrintingHouse,list_dict_printing_house
import sqlite3
import time
DB_NAME = "sql_post.db"
class Post(PrintingHouse):
    def __init__(self,name,address) -> None:
        self.__name = name
        self.__address = address
        # self.__dict_newspaper = super().get_dict_newspapers()
        # self.__dict_printing_house = PrintingHouse.info_printinghouse()
    @property    
    def information_post(self):
        return (self.__name,self.__address)
    # @information_post.setter
    # def information_post(self):
    #     return (self.__name,self.__address,self.__dict_newspaper)

    def choose_printinghouse(self):
        dict_of_printinghouse = list_dict_printing_house()
        print(dict_of_printinghouse)
        print()
        choose_printinghouse = input("Выберите типографию: ")
        for i in range(len(dict_of_printinghouse)):
            if dict_of_printinghouse[i]['Название типографий']==choose_printinghouse:
                self.__dict_printinghouse = dict_of_printinghouse[i]
    def information_of_post_printinghouse(self):
        return self.__dict_printinghouse
Post1 = Post("NamePost1","AddressPost1")
Post2 = Post("NamePost2","AddressPost2")
print(Post1.information_post)
Post1.choose_printinghouse()
Post2.choose_printinghouse()
print(Post1.__dict__)
print(Post2.__dict__)
print()
# print(Post1.information_of_post_printinghouse())
def choose_max_circuation(post1,post2):
    if int(post1['Тираж газеты'])>int(post2['Тираж газеты']):
        print(f"{Post1.information_post} в эту почту поступает больше всего газет")
    else:
        print(f"{Post2.information_post} в эту почту поступает больше всего газет")
choose_max_circuation(Post1.information_of_post_printinghouse(),Post2.information_of_post_printinghouse())

def find_post(newspaper):
    if newspaper == Post1.information_of_post_printinghouse()['Название газеты']:
        print(f"Газета под название {newspaper} печатаеться в типографий {Post1.information_of_post_printinghouse()['Название типографий']} на почте {Post1.information_post}")
    else:
        print(f"Газета под название {newspaper} печатаеться в типографий {Post2.information_of_post_printinghouse()['Название типографий']} на почте {Post2.information_post}")
print()
newspaper_name = input("Введите название газеты: ")
print()
find_post(newspaper_name)
print()
def find_max_newspaper_post():
    newspaper_price_post1 = Post1.information_of_post_printinghouse()['Цена газеты']
    newspaper_price_post2 = Post2.information_of_post_printinghouse()['Цена газеты']
    if newspaper_price_post1>newspaper_price_post2:
        print(f"Максимальная стоимость газеты на почте {Post1.information_post} стоимость газеты {newspaper_price_post1}")
    else:
        print(f"Максимальная стоимость газеты на почте {Post2.information_post} стоимость газеты {newspaper_price_post2}")
find_max_newspaper_post()


