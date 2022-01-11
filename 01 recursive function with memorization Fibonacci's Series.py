dictionary = {
    1: 1,
    2: 1
}

counter = 0

def fibo(n):
    global counter
    counter += 1

    if n in dictionary:
        return dictionary[n]
    if n == 2:
        return dictionary[n]
    else:
        dictionary[n] = fibo(n - 1) + fibo(n - 2)
        return dictionary[n]

while (1):
    x = int(input("피보나치 수열의 값을 구할 인수를 입력하세요(20보다 작은 값)? : "))
    for i in range(1, x+1):
        print("fibo({})의 값= {}, 계산수 = {}".format(i, fibo(i), counter))
    retry = int(input("계속할까요? (예:1. 아니오:0) :"))
    if retry == 0:
        break

    print()
    
for i in dictionary:
    print(dictionary[i], end=" ")

print()
print(len(dictionary))