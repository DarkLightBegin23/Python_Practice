# 223 - 300제 문제
even_list = []

def print_even(number_list):
    for i in range(len(number_list)):
        if number_list[i] % 2 == 0:
            even_list.append(number_list[i])
            print(even_list.pop())
        else:
            pass

print_even([1, 2, 3, 10])

'''
(solve)

def print_even(number_list):
    for v in number_list:
        if v % 2 == 0:
            print(v)
'''
