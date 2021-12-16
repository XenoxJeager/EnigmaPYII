# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
def isprime(num):
    flag = True
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = False
            break
    return flag


def multiple(end):
    a = []
    num = end
    begin = 2

    while num > begin and not isprime(num):

        for i in a:
            if num % i == 0:
                lx = False
                break
        for m in range(begin, num):
            if num == 6857:
                print(m)
            if num % m == 0:
                num = int(num / m)
                begin = m + 1
                if isprime(m):
                    a.append(m)
                if isprime(num):
                    a.append(num)
                break

    return a[len(a) - 1]


print(multiple(600851475143))
