def transform_list(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num // 2)
        else:
            new_list.append(num * 2)
    return new_list

print(transform_list([1, 2, 3, 4]))
print(transform_list([5, 10, 3, 5]))

#codewars
#1
def even_or_odd(number):
   if number % 2 == 0:
       return "Even"
   else:
       return "Odd"
   
#2
def number_to_string(num):
    return str(num)

#3
def solution(str):
  return str[::-1]

#4
def opposite(number):
    return -number

#5
def make_negative( number ):
    if number > 0:
        return -number
    else:
        return number
    