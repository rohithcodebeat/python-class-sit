a = [1,2,3,4,5]


def rotate_left(a):
    temp = a[len(a)-1]
    for i in range(len(a)-1,0,-1):
        a[i] = a[i-1]
    a[0] = temp 
    return a 

def rotate_right(a):
    temp = a[0]
    for i in range(len(a)-1):
        a[i] = a[i+1]
    a[len(a)-1] = temp 
    return  a 

def rotate(order, times, a):
    while times > 0:
        if order == 'r':
            rotate_right(a)
        elif order == 'l':
            rotate_left(a)
        times -= 1 
    return a 

order = input("Enter Order of the Rotation (r/l) : ")

times = int(input("Enter no of times array should rotate : "))

print(rotate(order, times%len(a), a))










# def rotate(a,order,t):
#     for i in range(1,t+1):
#         if order=="r":
#             c=a[0]
#             a.remove(c)
#             a.insert(len(a),c)
#         if order=="l":
#             c=a[len(a)-1]
#             a.remove(c)
#             a.insert(0,c)
#     print(a)
# order=input("Enter r or l for rotation: ")
# t=int(input("Enter the times for rotation: "))
# rotate(a,order,t)