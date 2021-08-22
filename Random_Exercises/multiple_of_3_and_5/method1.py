# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for x in range(1,100):
    if x%3 == 0 and x%5 ==0 :
        print('{} : FizzBuzz is a multiple of 3 and 5'.format(x))
    elif x%5==0:
       print('{} : Buzz is a multiple of 5'.format(x))
    elif x%3==0:
        print('{} : Fizz is a multiple of 3'.format(x))
    else:
        print(x)
