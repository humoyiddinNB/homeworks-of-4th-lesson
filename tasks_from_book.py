import os
os.system("cls")



#####       14-masala
# def ask_number():
#     list_ = []
#     a = 1
#     while True:
#         number = int(input(f"{a} - sonni kiriting: "))   
#         list_.append(number)
#         if number == 0:
#             break
#         a += 1
#     k = int(input("k ning qiymatini kiriting: "))
#     return list_ , k

# def finder(list_, k):
#     result = [i for i in list_ if i < k]
#     return len(result) if result else 0

# list_, k = ask_number()
# print(finder(list_, k))     










######      15-masala
# def ask_num():
#     list_ = []
#     count = 1
#     while True:
#         number  = int(input(f"{count} - sonni kiriting: "))
#         list_.append(number)
#         if number == 0:
#             break
#         count += 1
#     k = int(input("K soni qiymatini kiriting: "))
#     return list_, k

# def finder(list_ , k):
#     return next((i for i in list_ if i > k), 0)

# list_, k = ask_num()
# print(finder(list_, k)) 









#####       16-masala
# def ask_num():
#     list_ = []
#     count = 1
#     while True:
#         number = int(input(f"{count} - sonni kiririting: "))
#         list_.append(number)
#         if number == 0:
#             break
#         count += 1
#     k = int(input("K sonini qiymatini kiriting: "))
#     return list_ , k

# def finder(list_, k):
#     return next((i for i in list_[::-1] if i > k), 0)

# list_ , k  = ask_num()
# print(finder(list_, k))










#####       17-masala
# def ask_num():
#     n = int(input("N soni qiymatini kiriting: "))
#     print(f"{n} ta son kiritishni boshlaymiz: ")
#     return [int(input(f"{i + 1} - son qiymatini kiriting: ")) for i in range(n)]

# def finder(list_):    
#     b = int(input("B soni qiymatini kiriting: "))
#     for i in list_:
#         print(str(b) + str(i))
        
# nums = ask_num()
# finder(nums)











######      18-masala
# def ask_nums():
#     n = int(input("N sonini kiritinng: "))
#     print(f"{n} ta sonni o'sish tartibida kiritshni boshlang:")
#     return [int(input(f"{i + 1} - sonni kiriting: ")) for i in range(n)]

# def finder(list_):
#     return sorted(list(set(list_)))

# list_ = ask_nums()
# print(finder(list_))








####        19-masala
# def ask_nums():
#     n = int(input("N sonini kiritinng: "))
#     print(f"{n} ta son kiritamiz:")
#     return [int(input(f"{i + 1} - sonni kiriting: ")) for i in range(n)]

# def finder(list_):
#     result_list =[list_[i] for i in range(1, len(list_)) if list_[i] < list_[i - 1]]
#     return result_list, len(result_list)

# nums = ask_nums()
# list_ , len_list = finder(nums)

# for i in list_:
#     print(i)
# print(f"bunday sonlar {len_list} ta")