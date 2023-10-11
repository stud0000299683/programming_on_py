
#Введите товар и его стоимость
#если больше нет товаров то введите end
command = True
shops =[]
prices = []
max_economy = False

def create_shop(name):
    shops.append(name)


while command:
    print('''для завершения ввода магазинов напечатайте "end"\
    для завершения программы напечатайте "exit" ''')
    name = str(input('Введиде название магазина: '))
    if name == 'exit':
        command = False
    elif name != 'exit' and name !='end':
        if name in shops:
            print('Такой магазин уже есть введи другой')
        else:
            create_shop(name)
        # print(shops)
    elif name == 'end':
        while command:
            product = str(input('Введите название товара:'))
            if product =='exit':
                command = False
            else:
                for i in shops:
                    product_in_shops = {}
                    product_in_shops['shop_name'] = i
                    product_in_shops['product_name'] = product
                    try:
                        price = float(input(f'Введите цену в магазине {i}:'))
                        product_in_shops['product_price'] = price
                    except ValueError:
                        print('Не тот тип данных')
                        price = float(input(f'Введите цену в магазине {i}:'))
                    prices.append(product_in_shops)

print(prices)
for i in shops:
    count_summ = 0
    for j in prices:
        if j['shop_name'] == i:
            count_summ += j['product_price']
    print(i, count_summ)

    if max_economy == False:
        max_economy = count_summ
        economy_shop = i
    elif max_economy > count_summ:
        max_economy = count_summ
        economy_shop = i
print(f'Больше всего можно сэкономить в магазине {economy_shop} купив товар за {max_economy}')
