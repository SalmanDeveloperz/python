# num=int(input('Enter the number whose table you want to print:'))
# # Simple Tables Method 1
# for j in range (1,11):
#     print(num,' x ',j,' = ',num*j)
#     # j+=1
# print('\n')

# #Simple Method 2:
# num=2
# for j in range (1,11):
#     print(f'{num} X {j} = {num*j}')


#Print Tables of 1 to 10 in one time (Very Easy and Efficient)
for i in range(1,11):
    for j in range (1,11):
        print(f'{i} X {j} = {i*j}')
    print('================')
