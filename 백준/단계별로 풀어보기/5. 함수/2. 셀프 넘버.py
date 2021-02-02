'''
non_self_number_list = []

for i in range(1, 10000) :
    ten_thousand = i // 10000
    thousand = (i % 10000) // 1000
    hundred = ((i % 10000) % 1000) // 100
    ten = (((i % 10000) % 1000) % 100) // 10
    one = (((i % 10000) % 1000) % 100) % 10

    non_self_number = i + ten_thousand + thousand + hundred + ten + one
    non_self_number_list.append(non_self_number)

non_self_number_list = list(set(non_self_number_list))

under_number_list = [x for x in non_self_number_list if x<10000 ]

numbers = list(range(1,10000))
self_numbers = set(numbers).difference(set(under_number_list))

for i in range(len(self_numbers)) :
    result = sorted(self_numbers)
    print(result[i])
'''
num_range = 10000

def non_self_num(n) :
    return n + sum([int(i) for i in str(n)])

self_numbers = [0] * num_range
for i in range(num_range) :
    if(non_self_num(i) < num_range) :
        self_numbers[non_self_num(i)] = 1

for i in range(num_range) :
    if self_numbers[i] == 0 :
        print(i)