def calc():
    first_number = input("Введіть перше число: \t")
    operation = input("Оберіть операцію: Додавння(+), Віднімання(-), Множення(*), Ділення(/) \t")
    second_number = input("Введіть друге число: \t")
    try:
        first_number = float(first_number)
        second_number = float(second_number)
    except ValueError:
        print("Вви ввели не вірне значеня!")
        calc()
    else:
        if operation == "+":
            result = first_number + second_number
            print(f"Результат:   {result}")
        elif operation == "-":
            result = first_number - second_number
            print(f"Результат:   {result}")
        elif operation == "*":
            result = first_number * second_number
            print(f"Результат:   {result}")
        else:
            if second_number != 0 and operation == "/":
                result = first_number / second_number
                print(f"Результат:   {result}")
            else:
                if second_number == 0:
                    print("Ділення на 0, трошки поміркуй!")
                else:
                    print("Щось не те ввів, поміркуй")
                    calc()
calc()
