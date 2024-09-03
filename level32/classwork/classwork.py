#codewars

#1 
def square_sum(numbers):
    sum = 0
    for num in numbers:
        squared = num * num
        sum += squared
    return sum

#2
def repeat_str(repeat, string):
    result = ""
    for _ in range(repeat):
        result += string
    return result
