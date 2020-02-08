number = int(input())
for i in range(number):
    name_in = input()
    name_out = ''
    for j in name_in:
        if j.isupper():
            name_out += j
    print(name_out)
