numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = 0
for i in range(len(numbers)):
    for j in range(numbers[i]):
        if numbers[j] == 1 or numbers[i] == 1:
            continue
        elif numbers[i] == 2 or numbers[i] == 3:
            is_prime = numbers[i]
            primes.append(is_prime)
            break
        elif numbers[i] % 3 == 0:
            is_prime = numbers[i]
            not_primes.append(is_prime)
            break
        elif numbers[i] % numbers[j] == 0:
            is_prime = numbers[i]
            not_primes.append(is_prime)
            break
        else:
            is_prime = numbers[i]
            primes.append(is_prime)
            break
print (primes)
print (not_primes)

# решена для данного списка, но если его расширить,
# то все числа, являющиеся произведением простых делителей больше 3 (5*7=35, 7*7=49 и т.п.)
# попадают в простые пока непонятно, почему.