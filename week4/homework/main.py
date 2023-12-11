from math_operations import basic_operations, power_operation,  apply_operations

result_basic = basic_operations(10,5)
print("Basic operation result: ",result_basic)

result_power = power_operation(2,3)
print("Power operation result: ", result_power)

result_power_modulo = power_operation(2,3,modulo = 5)
print("Power operation with modulo result: ",result_power_modulo)

operations = [
    (lambda x, y: x + y, (3, 4)),
    (lambda x, y: x * y, (2, 5)),
]
result_apply = apply_operations(operations)
print("Apply Operations Result:", result_apply)
