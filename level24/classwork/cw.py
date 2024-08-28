# თავდაპირველი სტრინგი
text = "hello world"

# capitalize() - პირველ ასოს აქცევს დიდ, დანარჩენებს კი პატარა
capitalized_text = text.capitalize()
print(capitalized_text)  # "Hello world"

# upper() - ყველა ასოს აქცევს დიდ
upper_text = text.upper()
print(upper_text)  # "HELLO WORLD"

# lower() - ყველა ასოს აქცევს პატარა
lower_text = text.lower()
print(lower_text)  # "hello world"

# count(substring) - კითხულობს რამდენჯერ არის გამოყოფილი ქვეწერა (substring) სტრინგში
count_o = text.count("o")
print(count_o)  # 2

# title() - ყოველი სიტყვის პირველი ასო აქცევს დიდ
title_text = text.title()
print(title_text)  # "Hello World"

# ახალი სტრინგი
new_text = "python is awesome"

# capitalize() ახალი სტრინგისთვის
new_capitalized = new_text.capitalize()
print(new_capitalized)  # "Python is awesome"

# upper() ახალი სტრინგისთვის
new_upper = new_text.upper()
print(new_upper)  # "PYTHON IS AWESOME"

# lower() ახალი სტრინგისთვის
new_lower = new_text.lower()
print(new_lower)  # "python is awesome"

# count() ახალი სტრინგისთვის
count_i = new_text.count("i")
print(count_i)  # 2

# title() ახალი სტრინგისთვის
new_title = new_text.title()
print(new_title)  # "Python Is Awesome"
