# i will write cool code!!!!!!!!!

print("Добро пожаловать в наш сервис по заказу бургеров. Пожалуйста выберите начинку для вашего бургера из списка")

toppings = ["томаты", "сыр", "огурцы", "салат", "котлета", "бекон", "соус", "кетчуп"]
condiments = ["майонез", "горчица", "кетчуп"]

for i in range(len(toppings)):
    print(f"{i+1}: {toppings[i]}")

user_burger = []

while True:
    print("Введите любое число не из списка топпингов чтобы завершить заказ")
    user_choice = int(input("Введите номер позиции топпинга, который вы хотите добавить -> "))
    try:
        user_burger.append(toppings[user_choice-1])
    except IndexError:
        print("Выберите кондимент")
        for i in range(len(condiments)):
            print(f"{i+1}: {condiments[i]}")
        condiment_choice = int(input("Введите номер позиции кондимента, который вы хотите добавить -> "))
        user_burger.append(condiments[condiment_choice-1])
        break

print(f"Ваш заказ бургер с следующим составом: {', '.join(user_burger)}")