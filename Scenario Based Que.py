# Q. Count the elements from the string without using inbuilt function.

# str_ = "hhahihfoh efhljek"
# res = {}
# for i in str_:
#     if i in res:
#         res[i] += 1
#     else:
#         res[i] = 1
# print(res)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Q.
# sample_data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# str_ = "AD4EG2H2J"
# lst1 = []
# digit_string = ""
# latest_char = None
#
# for ele in str_:
#     if ele.isalpha():
#         if digit_string:
#             def next_char(latest_character, int_string):
#                 ord_latest = ord(latest_character)
#                 ord_sum = ord_latest + int(int_string)
#                 if ord_sum > ord('Z'):
#                     ord_diff = ord_sum - ord('Z')
#                     ord_reminder = ord_diff % 26
#                     next_character = chr((ord('A') - 1) + ord_reminder)
#
#                     return next_character
#                 else:
#                     ord_latest = ord(latest_character)
#                     ord_sum = ord_latest + int(int_string)
#                     next_character = chr(ord_sum)
#                     return next_character
#             next_char = next_char(latest_char, digit_string)
#             lst1.append(latest_char)
#             digit_string = ""
#         latest_char = ele
#         lst1.append(latest_char)
#
#     elif ele.isdigit():
#         digit_string += ele
#
# output = "".join(lst1)
# print(output)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # Without using inbuilt method.
#
# s1 = "mohanmanofmangal"
# dict_ = {}
# for i in s1:
#     if i in dict_:
#         dict_[i] = dict_[i] + 1
#     else:
#         dict_[i] = 1
# result_ = max(dict_, key=dict_.get)
# print(result_, "=", dict_[result_])
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # By Using count() method

# s = "omomomomom"
#
# my = {}
# flg = True
# for letter in s:
#     while flg:
#         prev = letter
#         my[prev] = s.count(prev)
#
#         flg = False
#
#     if s.count(letter) > my[prev]:
#         my = {letter: s.count(letter)}
#         prev = letter
# print(my)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# def high_count_ele(str_):
#     d = {}
#     for i in str_:
#         cnt = str_.count(i)
#         if cnt > 1:
#             d[i] = cnt
#             res = max(d, key=d.get)
#     return res
#
#
# str_ = "mohanmanofmangal"
# print(high_count_ele(str_))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# str_ = "mohanmanofmangal"
# dict_ = {i: str_.count(i) for i in str_}
# result_ = max(dict_, key=dict_.get)
# print(result_, "=", dict_[result_])
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Sort the list of dict using students I'd without using sort function


# def sort_list(students):
#     new_list = []
#     while students:
#         min_student = min(students, key=lambda x: x['student_id'])
#         new_list.append(min_student)
#         students.remove(min_student)
#     return new_list
#
#
# students = [{"student_name": "s4", "student_id": 24}, {"student_name": "s1", "student_id": 13},
#             {"student_name": "s2", "student_id": 19}, {"student_name": "s3", "student_id": 10}]
# print(sort_list(students))


# By using lambda function.
students = [{"student_name": "s4", "student_id": 24}, {"student_name": "s1", "student_id": 13},
            {"student_name": "s2", "student_id": 19}, {"student_name": "s3", "student_id": 10}]
students = list(map(lambda x: x, sorted(students, key=lambda x: x['student_id'])))
print(students)

print({i*i: i**3 for i in range(1, 11)})


lst = [0, 1, 2, [], [3, 4], (), ('a', 'b'), [], [5, 6, 7], 8]
lst_op = list(filter(lambda x: x or x != [], lst))
print(lst_op)

list_op = [i for i in lst if i or i != []]
print(list_op)

