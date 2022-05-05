 # 1. NUMERE PARE DE LA 1 LA 10
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f'Avem {count} numere pare')

 # 2. NUMERE IMPARE DE LA 1 LA 30
count = 0
for number in range(1, 30):
    if number %2 == 1:
        count +=1
        print(number)
print(f'Avem {count} numere impare')

