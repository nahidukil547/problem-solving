"""
সমস্যার বিবরণ
একটি প্রোগ্রাম লিখুন যেখানে আপনাকে N আকারের একটি array[] এবং একটি পূর্ণসংখ্যা P দেওয়া হবে। অ্যারেতে ট্রিপলেটটি খুঁজুন যাদের যোগফল প্রদত্ত পূর্ণসংখ্যা P এর সমান হয়।

ইনপুট
প্রোগ্রামটি একটি অ্যারের আকার হিসাবে একটি পূর্ণসংখ্যা N নেবে। তারপর এটি arr[] অ্যারের পূর্ণসংখ্যার মান নেবে। অবশেষে, এটি P এর মান নেবে।

আউটপুট
আউটপুটে ট্রিপলেট সংখ্যা তিনটি প্রিন্ট হবে।

সীমাবদ্ধতা
0 ≤ N ≤ 100000
0 ≤ arr[] ≤ 100000
0 ≤ P ≤ 100000


Problem Statement
Write a program where you will be given an array arr[] of size N and an integer P. Find the triplet in the array which sums up to the given integer P.

Input
The program will take an integer N as the size of an array. Then it will take the integer values of the array arr[]. Finally, it will take the target value P .

Output
The output will print the triplet numbers which will generate the sum.

Constraints
0 ≤ N ≤ 100000
0 ≤ arr[] ≤ 100000
0 ≤ P ≤ 100000"""

# n = int(input('Enter Array Size: '))
# p = list(map(int, input('Enter your array: ').split()))
# sum = int(input('Enter Sum Of Number: '))

# found = False
# if len(p)<= n  :
#     for i in p:
#         for j in p:
#             for k in p:
#                 if i + j + k == sum:
#                     print(i, j, k)
#                     found = True
#                     break
#             if found:
#                 break
#         if found:
#             break
# else:
#     print('invalid array')
    
    
    # 6
# 1 5 6 7 9 6
# 16


# n = int(input().strip())
# print(n, type(n))
# arr = list(map(int, input().strip().split()))
# P = int(input().strip())

# if len(arr) != n:
#     print("Array size mismatch")
# else:
#     arr.sort() 
#     found = False

#     for i in range(n - 2):
#         left = i + 1
#         right = n - 1

#         while left < right:
#             total = arr[i] + arr[left] + arr[right]

#             if total == P:
#                 print(arr[i], arr[left], arr[right])
#                 found = True
#                 break 

#             elif total < P:
#                 left += 1
#             else:
#                 right -= 1

#         if found:
#             break

#     if not found:
#         print("No triplet found")



n = 6
print(n, type(n))
arr = [12, 3, 4, 1, 6, 9]
P = 24

if len(arr) != n:
    print("Array size mismatch")
else:
    arr.sort() 
    found = False
	
    for i in range(n - 2):
        left = i+1
        right =n-1
        print('f',i,left,'=',i, right)
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            print(total)
            
            if total < P:
                left += 1
            else:
                right -= 1