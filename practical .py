#rectangle pattern
# for r in range(1,5):
#     for j in range(1,7):
#         print("*",end="")
#     print()    
       
#increasing triangle

# for a in range(1,8):
#     for b in range(1,a+1):
#         print("*",end="")
#     print()    


#number square
# for j in range(4):
#     for r in range(1,5):
#         print(r,end="")
#     print()    

#table 1to 10
# for f in range(1,11):
#     print("Table of",f)
#     for j in range(1,11):
#         print(f,"*",j,"=",f*j)
#     print()    

#Classroom Setting
# for i in range(1, 6):
#     for j in range(1, 9):
#         print(f"A{i}B{j}", end=" ")
#     print()


#prime number
for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)


