def basic_operations(n1, n2):
    answer = {}
    try:
        answer["Addition"] = n1 + n2
        answer["Substraction"] = n1 - n2
        answer["Multiplication"] = n1 * n2
        if n2 != 0:
            answer["Division"] = n1 / n2
        else:
            raise ZeroDivisionError("Error: Cannot divide by Zero.")
    except TypeError:
        print("Error: Invalid input type. Both inputs should be numbers.")
    finally:
        return answer
    pass

def power_operation(base, ex, **kwargs):
    try:
        power = base ** ex

        if 'modulo' in kwargs:
            power %= kwargs['modulo']
        
        return power
    except TypeError:
        print("Error: Invalid input type. Both inputs should be numbers.")
    except ValueError:
        print("Error: Invalid values. Both inputs must not be negative numbers.")
    pass

def apply_operations(operation_list):
    return list(map(lambda op: op0, operation_list))




