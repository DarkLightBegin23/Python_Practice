num_list_1 = [1, 2, 3, 4, 5]
num_list_2 = [10, 20, 30, 40, 50]
num_list_3 = [11, 12, 13, 14, 15]
nested_list =[num_list_1, num_list_2, num_list_3]

even_nums_total = [0, 0, 0]

for list_index in range(len(nested_list)):  # len(nested_list) == 3 그러므로 list_index == [0, 1, 2]
    current_list = nested_list[list_index]  # nested_list[0] == num_list_1, nested_list[1] == num_list_2, nested_list[2] == num_list_3
    for item in current_list:  # 각각의 요소들에 대해 접근
        if item % 2 == 0:
            even_nums_total[list_index] += item  # 리스트 각각의 요소 중 짝수가 나오면 even_nums_total 각각의 요소에 가산하여 대입
            
print(even_nums_total)  # [6, 150, 26]