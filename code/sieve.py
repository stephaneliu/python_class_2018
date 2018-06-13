limit = 10000000
maybe_prime = list(range(0, limit))

for x in maybe_prime:
    if x > 1:
       check = range(x, limit)
       for checking in check:
           try:
               if(maybe_prime[checking] % x) == 0:
                   del(maybe_prime[checking])
           except:
               None

print("Is prime", maybe_prime)
