# arr=[2,3,5,7,7,3]
# # emp=[]
# # for i in range(len(arr)):
# #     last="xaina"
# #     for j in range(i+1,len(arr)):
# #         if arr[i]>arr[j]:
# #             last=arr[j]
# #             break
# #     emp.append(last)
# # print(emp)

# res = []

# for i in range(len(arr)):
#     next_greater = -1
#     for j in range(i+1, len(arr)):
#         if arr[j] > arr[i]:
#             next_greater = arr[j]
#             break
#     res.append(next_greater)

# print(res)

# arr.sort(reverse=True)
# print(arr)
# sentence="abi abi abi khadka khadka khadka ha ha ha"
# words=sentence.split()
# fre={}
# for w in words:
#     if w in fre:
#         fre[w]+=1
#     else:
#         fre[w]=1
# print(fre)
a=[1,2,4,5,5,6,7,6,8]
b=[]
c={}

for i in a:
    if i in b:
        continue 
    else:
        b.append(i)
print(b)
for i in a:
        c[i]=c.get(i,0)+1
print(c)
most=max(c,key=c.get)
print(most)
ll={"abi":1,"khadka":2,"hehe":4}
oo=max(ll.values())
print(oo)