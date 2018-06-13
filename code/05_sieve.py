limit = 10000000
maybe_prime = list(range(0, limit))

for x in maybe_prime:
    if x > 1:
       check = range(x, len(maybe_prime))
       for checking in check:
           print("iterating at:", x, "checking: ", checking, "list size: ", len(maybe_prime))
           try:
               if(maybe_prime[checking] % x) == 0:
                   del(maybe_prime[checking])
           except:
               None

print("Is prime", maybe_prime)
