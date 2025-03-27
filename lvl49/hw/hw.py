# def calculator(equation):
#     # Find the index of the operator
#     operator_index = equation.index(" ") + 1
#     operator = equation[operator_index]
    
#     # Split the equation into two parts
#     left_dots = equation[:operator_index - 1]
#     right_dots = equation[operator_index + 2:]
    
#     # Convert dots to numbers
#     left_number = len(left_dots)
#     right_number = len(right_dots)
    
#     # Perform the operation
#     if operator == '+':
#         result_number = left_number + right_number
#     elif operator == '-':
#         result_number = left_number - right_number
#     elif operator == '*':
#         result_number = left_number * right_number
#     elif operator == '/':
#         result_number = left_number // right_number 
#     result_dots = '.' * result_number
#     return result_dots


# def solution(text, ending):
#     test=text[::-1]
#     test2=ending[::-1]
#     if test[:len(test2)]==test2:
#         return True
#     else:
#         return False

# def solution(text, ending):
#     if text[-len(ending):]==ending:
#         return True
#     else:
#         return False


# def find_smallest_int(arr):
#     answer =arr[0]
#     for i in range(0,len(arr)):
#         if arr[i] < answer:
#             answer = arr[i]
#     return answer

# we are trying to pop every element that occurs in list b from list a, even if it is repeated
def remove_elements(a, b):
    list=[]
    for i in range(0,len(a)):
        if a[i] not in b:
            list.append(a[i])
            b.remove(a[i])