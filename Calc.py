def calc(first_number, second_number, operation='+'):
    try:
        first_number, second_number = float(first_number), float(second_number)
    except ValueError:
        return "Ви ввели не вірне значеня!"
    else:
        if operation == '+':
            return first_number + second_number
        elif operation == '-':
            return first_number - second_number
        elif operation == '*':
            return first_number * second_number
        elif operation == '/':
            if second_number == 0:
                return "Ділення на 0, трошки поміркуй!"
            else:
                return first_number / second_number
        else:
            if operation in ('+', '-', '*', '/'):
                return operation#What for?
            else:
                return "Щось не те ввів, поміркуй"



