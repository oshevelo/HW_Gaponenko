from Calc import calc


if __name__ == '__main__':

    number_operation = input("Введіть кількість операцій: \t")

    try:
        number_operation = int(number_operation)
    except ValueError:
        print("Ви ввели не вірне значеня!")
    else:

        if number_operation > 0:
            i = 2

            first_number = input("Введіть перше число: \t")
            operation = input("Оберіть операцію: Додавння(+), Віднімання(-), Множення(*), Ділення(/) \t")
            second_number = input("Введіть друге число: \t")

            result = calc(first_number=first_number,
                          second_number=second_number,
                          operation=operation)

            if isinstance(result, str):
                print(result)
            else:
                while i < number_operation:
                    first_number = result
                    operation = input("Оберіть операцію: Додавння(+), Віднімання(-), Множення(*), Ділення(/) \t")
                    second_number = input("Введіть наступне число: \t")
                    if isinstance(result, str):
                        break
                    if operation not in ("+", "-", "*", "/"):
                        break

                    result = calc(first_number=first_number,
                                  second_number=second_number,
                                  operation=operation)

                    i += 1

                print(result)
        else:
            print("Щось не те ввів, поміркуй")
