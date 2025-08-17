"""
Problem Statement
Write a program to check if an array contains more positivity than negativity.An array has more positivity if it contains strictly more unique positive values than unique negative values. If the number of positive and negative values are equal then it is also taken as negativity.

Input
The program will take an integer N as the size of an array. Then it will take the integer values of the array M[].

Output
The output will print either "Positivity" or "Negativity"

Constraints
0 ≤ |N| ≤ 10000
-10000 ≤ |M[]| ≤ 10000

সমস্যার বিবরণ
এমন একটি প্রোগ্রাম লিখ যা নির্ণয় করবে একটি অ্যারেতে পজিটিভিটি নাকি নেগেটিভিটির পরিমাণ বেশি। একটি অ্যারেতে পজিটিভিটি বেশি থাকবে যদি তাতে পজিটিভ ভ্যালুর সংখ্যা সর্বদা নেগেটিভ ভ্যালুর সংখ্যার চেয়ে বেশি থাকে। যদি সমান সংখ্যক পজিটিভ এবং নেগেটিভ সংখ্যা থাকে তাহলে তা নেগেটিভিটি বলে বিবেচিত হবে।

ইনপুট
প্রোগ্রামটি প্রথমে অ্যারেটির সাইজ N নিবে, তারপর অ্যারে M[] এর সংখ্যাগুলো নিবে।

আউটপুট
আউটপুটে হয় "Positivity" অথবা "Negativity" প্রিন্ট হবে।

সীমাবদ্ধতা
0 ≤ |N| ≤ 10000
-10000 ≤ |M[]| ≤ 10000

"""

n=int(input('Enter array size: '))
array = list(map(int,input('Enter array: ').split()))
positive =[]
negative =[]
if len(array) == n:
    for i in array:
        if i<0 :
            negative.append(i)
        if i>0:
            positive.append(i)

    if len(positive)>len(negative):
        print("Positivity")
    else:
        print('Negativity')
else:
    print("Array size mismatch")
