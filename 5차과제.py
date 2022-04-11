a = int(input("피자의 조각수를 입력하세요 : "))
b = [1, 1] 
for i in range(2, a+1):
    b.append(0)
    b[i] = b[i-2] + b[i-1]
print(b[a])
