with open('file.txt','r',encoding='utf-8') as f:
    i = 0
    cook_book = {}
    lines = f.readlines()
    lines = [value for value in lines if value != '\n']
    while i < len(lines):
        cook_book[lines[i].strip()] = []
        for j in range(int((lines[i+1].strip()))):
            cook_book[lines[i].strip()].append({'ingredient_name': lines[i+j+2].split('|')[0].strip(), 'quantity': lines[i+j+2].split('|')[1].strip(), 'measure': lines[i+j+2].split('|')[2].strip()})
        i += j + 3
def get_shop_list_by_dishes(dishes, person_count,cook_book):
    receipt = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in receipt.keys():
                receipt[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity'])*person_count}
            else:
                receipt[ingredient['ingredient_name']]['quantity']+= int(ingredient['quantity'])*person_count
    return receipt
print(cook_book)
print(get_shop_list_by_dishes(['Омлет','Фахитос'],2,cook_book))







