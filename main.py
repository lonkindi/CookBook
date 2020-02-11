cook_book = dict()


def ins_dish(dish):
    cook_book[dish] = []


def ins_ingredients(dish, ingredients):
    ingr_list = ingredients.split(sep='|')
    ingr_name = ingr_list[0]
    ingr_quantity = int(ingr_list[1])
    ingr_measure = ingr_list[2].strip()
    cook_book[dish].append({'ingredient_name': ingr_name, 'quantity': ingr_quantity, 'measure': ingr_measure})


def main():
    with open('recipes.txt', encoding='utf-8') as file:
        counter = 0
        while True:
            current_dish = file.readline().strip()
            if not current_dish:
                break
            ins_dish(current_dish)
            count_ingr = int(file.readline())
            while counter < count_ingr:
                ins_ingredients(current_dish, file.readline())
                counter += 1
            file.readline()
            counter = 0
    print('Задача №1')
    print(f'cook_book = {cook_book}')
    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = dict()

main()
