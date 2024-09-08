# num=int(input('Enter the number whose table you want to print:'))

# # Simple Tables
# for j in range (1,11):
#     print(num,' x ',j,' = ',num*j)
#     # j+=1
# print('\n')


#Print Tbles of 1 to 10 in one time (Very Easy and Efficient)
for i in range(1,11):
    for j in range (1,11):
        print(f'{i} X {j} = {i*j}')
    print('================')

#multiplication Table 

# num1=10
# num2=20
# ans=num1*num2
# print(ans)