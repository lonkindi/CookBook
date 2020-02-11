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
    print('Задача №1', end='')
    for dish in cook_book:
        print(f'\n{dish}:')
        for ing_list in cook_book[dish]:
            print(ing_list)
    print()
    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = dict()
    for dish in dishes:
        if cook_book.get(dish) == None:
            print(f'Блюда {dish} нет в повареной книге')
            continue
        else:
            for ingredient in cook_book.get(dish):
                ingr_measure = ingredient['measure']
                ing_quantity = ingredient['quantity'] * person_count
                if shop_list.get(ingredient['ingredient_name']) == None:
                    shop_list[ingredient['ingredient_name']] = {'measure': ingr_measure, 'quantity': ing_quantity}
                else:
                    current_quantity = shop_list[ingredient['ingredient_name']].get('quantity')
                    shop_list[ingredient['ingredient_name']] = {'measure': ingr_measure,
                                                                'quantity': current_quantity + ing_quantity}
    print('Задача №2')
    for ingredient in shop_list:
        print(f'{ingredient}: {shop_list[ingredient]}')


main()
