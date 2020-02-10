cook_book = dict()


def ins_dish(dish):
    cook_book[dish] = []

def ins_ingredients(dish, ingredients):
    ingr_list = list(map(str, ingredients.split(sep='|')))
    cook_book[dish.strip()] = ingr_list

with open('recipes.txt', encoding='utf-8') as file:
    counter = 0
    count_ingr = 0
    current_dish = ''
    for string in file:
        if counter == 0:
            ins_dish(string.strip())
            current_dish = string
            counter += 1
        elif counter == 1:
            count_ingr =  int(string)
            counter += 1
        elif counter >= 2:
            if not count_ingr <= 0:
                ins_ingredients(current_dish, string)
                count_ingr -=1
                counter +=1
            else:
                counter = 0
                count_ingr = 0
                current_dish = ''

print(f'{counter}_{cook_book}_')
