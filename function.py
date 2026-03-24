# l1=[12,13,14,15,16,28,38,46,50]
# # def show_elements(lst):
# #     for i in lst:
# #         print(i)

# # l1 = [12,13,14,15,16,28,38,46,50]
# # show_elements(l1)

# def fetch_list(l):
#     for i in l:
#         print(i)
#         fetch_list([12,13,14,15,16,28,38,46,50])

# # s1='aaabbcdd' output-{'a':3,'b':2,'c':1,'d':2}
# def count_chars(s):
#     result = {}
    
#     for ch in s:
#         if ch in result:
#             result[ch] += 1
#         else:
#             result[ch] = 1
            
#     return result

# s1 = 'aaabbcdd'
# print(count_chars(s1))
# # s1='aaabbcdd' first non repecting character o/p='c'
# def first_non_repeating(s):
#     freq = {}
    
#     # Step 1: Count frequency
#     for ch in s:
#         if ch in freq:
#             freq[ch] += 1
#         else:
#             freq[ch] = 1

#     # Step 2: Find first non-repeating
#     for ch in s:
#         if freq[ch] == 1:
#             return ch

# s1 = 'aaabbcdd'
# print(first_non_repeating(s1))

# 
names=['ram','tree','deepika','amir']
result=list(map(lambda x:x.upper(),names))
print(result) 

l1=[2,35,21,8,10,15,20,1,29,42]
result1=filter(lambda y:y>15,l1)
print(list(result1))
