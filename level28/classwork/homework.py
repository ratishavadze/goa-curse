#code wars

#1
def count_bits(n: int) -> int:
    return bin(n).count('1')


#2
def each_cons(lst, n):
    return [lst[i:i+n] for i in range(len(lst) - n + 1)]

#3
def remove_char(s):
    return s[1 : -1]

#4
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

#5
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
        
    elif boolean == False:
        return "No"
    
