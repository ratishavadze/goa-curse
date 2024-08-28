#1
# სიის შექმნა
my_list = [10, 20, 30, 40, 50]

# სლაისინგი 1-დან 3-ის ჩათვლით (ინდექსები: 1, 2, 3)
sliced_list = my_list[1:4]

print(sliced_list)  # [20, 30, 40]

#2
# სიის შექმნა
my_list = [5, 10, 15, 20, 25, 30]

# სიის სლაისინგი ნახევრამდე
half_sliced = my_list[:len(my_list)//2]

# ახალი სიის შექმნა და სლაისინგის შედეგის დამატება
new_list = []
new_list.extend(half_sliced)

print(new_list)  # [5, 10, 15]


#3
# სიის შექმნა
my_list = [11, 22, 33, 44, 55, 66]

# პირველი სამი ელემენტის ინდექსების პოვნა
indices = [my_list.index(my_list[i]) for i in range(3)]

print(indices)  # [0, 1, 2]


#4
# სიის შექმნა
my_list = [7, 3, 5, 1, 9, 2]

# უდიდესი და უმცირესი მნიშვნელობების პოვნა
min_value = min(my_list)
max_value = max(my_list)

# ამოგდება სიიდან
my_list.remove(min_value)
my_list.remove(max_value)

print(my_list)  # [7, 3, 5, 2]


#5
# წინა დავალებიდან მიღებული რიცხვები
removed_numbers = [min_value, max_value]

# ახალი სია
new_list = []
new_list.extend(removed_numbers)

print(new_list)  # [1, 9]


#6
# ორი სიის შექმნა
list1 = [1, 5, 9, 3]
list2 = [2, 4, 6, 8]

# მინიმალური და მაქსიმალური წევრების პოვნა
min1, max1 = min(list1), max(list1)
min2, max2 = min(list2), max(list2)

# მაქსიმალურებიდან მინიმალურების გამოკლება
result1 = max1 - min2
result2 = max2 - min1

# შედეგის ახალი სიაში დამატება
result_list = [result1, result2]

print(result_list)  # [7, 7]
