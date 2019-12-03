

def fizzbuzz_convert(number):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(str(number))

fizzbuzz_convert(1)
fizzbuzz_convert(3)
fizzbuzz_convert(34)
fizzbuzz_convert(67)
fizzbuzz_convert(8)
fizzbuzz_convert(68)
fizzbuzz_convert(90)
fizzbuzz_convert(100)
fizzbuzz_convert(34)