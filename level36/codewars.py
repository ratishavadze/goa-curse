#1
def remove_every_other(my_list):
    del my_list[1::2]
    return my_list

#2
def xor(a, b):
    return (a and not b) or (not a and b)

#3
def square_sum(numbers):
    sum = 0
    for num in numbers:
        squared = num * num
        sum += squared
    return sum

#4

def count_bits(n: int) -> int:
    return bin(n).count('1')

#5
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
        
    elif boolean == False:
        return "No"