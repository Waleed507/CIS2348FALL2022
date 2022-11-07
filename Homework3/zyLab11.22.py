# Waleed Yusuf
# 2104654

words = input()
temp_list = words.split()

for each_word in temp_list:
    count = temp_list.count(each_word)
    print(each_word, count)
