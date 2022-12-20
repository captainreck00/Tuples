X=() 

def Input(M):
    print("Enter 0 when you want to exit")
    x=int(input("Enter a number ")) 
    while(x!=0):
        M=M+(x,)
        x=int(input("Enter a number "))
        print(M)
    return M
       
X=Input(X)
