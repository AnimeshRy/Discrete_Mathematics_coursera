x = [0, 3, 2, 4, 5, 6, 7, 1, 9, 8]


# def is_even(p):  # O(n^2)
#     i = 0
#     count = 0
#     while(i < len(p)):
#         k = i + 1
#         while(k < len(p)):
#             if(p[i] > p[k]):
#                 count += 1
#             k += 1
#         i += 1
#     if(count == 0):
#         return True, count
#     if(count % 2 == 0):
#         return True, count
#     else:
#         return False, count

# if true added to the my_count
def is_even(sequence):  # O(Logn)
    count = 0
    my_count = 0
    for i, num in enumerate(sequence, start=1):
        print([num > num2 for num2 in sequence[i:]])
        my_count += sum(num > num2 for num2 in sequence[i:])
        count += 1
        print(my_count)
    print(count)
    return my_count % 2 == 0


print(is_even(x))
