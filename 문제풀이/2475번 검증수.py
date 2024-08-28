number_list = list(map(int, input().split()))
double = 0

for i in number_list:
    double += (i ** 2)
    
double = double % 10
print(double)