x=["{} is fizzbuzz".format(x) if x%3==0 and x%5==0 else "{} is fizz".format(x) if x%3==0 else "{} is buzz".format(x) if x%5==0 else "not applicable" for x in range(1,100)]
print(x)
