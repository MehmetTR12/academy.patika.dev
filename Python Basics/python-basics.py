# Question-1
# 1- Write a function that flattens a list. Its elements can consist of multi-layered lists (such as [[3],2]) or non-scalar data. For example:
# sample input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# sample output: [1,'a','cat',2,3,'dog',4,5]

def flatten_list(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output_list = flatten_list(input_list)
print(output_list)


# Question-2
# 2- Write a function that reverses the elements in the given list. If the elements inside the list also contain the list, reverse their elements as well. For example:
# sample input: [[1, 2], [3, 4], [5, 6, 7]]
# sample output: [[[7, 6, 5], [4, 3], [2, 1]]

def reverse_list_elements(lst):
    reversed_elements = []
    for item in lst:
        if isinstance(item, list):
            reversed_elements.append(reverse_list_elements(item)[::-1])
        else:
            reversed_elements.append(item)
    return reversed_elements

input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_list_elements(input_list)
print(output_list)