Name=()
Pan=()
A_Sal=()
Tax=()
Cess=()
SurC=()
T_Tax=() 

def Input(N,Pan,A_Sal):
    for i in range(3):
        N=N+(input("Enter Your Name "),)
        Pan=Pan+(int(input("Enter Your Pan Number ")),)
        A_Sal=A_Sal+(int(input("Enter Your Annual Salary")),)
    return [N,Pan,A_Sal]

def tax(A_Sal,Tax,Cess,SurC,T):
    for i in range(len(A_Sal)):
        if A_Sal[i]<250000:
            SurC=SurC+(0,)
            Tax=Tax+(0,)
        elif A_Sal[i]>=250000 and A_Sal[i]<500000:
            k=5/100*A_Sal[i]
            SurC=SurC+(0,)
            Tax=Tax+(k,)
        elif A_Sal[i]>=500000 and A_Sal[i]<1000000:
            k=20/100*A_Sal[i]
            SurC=SurC+(10/100*k,)
            Tax=Tax+(k,)
        elif A_Sal[i]>=1000000:
            k=30/100*A_Sal[i]
            SurC=SurC+(15/100*k,)
            Tax=Tax+(k,)
        Cess=Cess+(4/100*Tax[i],)
        T=T+(Tax[i]+SurC[i]+Cess[i],)
          
    
    return [Tax,Cess,SurC,T]      

Name,Pan,A_Sal=Input(Name,Pan,A_Sal)
tax(A_Sal,Tax,Cess,SurC,T_Tax)[2]

for i in range(3):
    print(Name[i],Pan[i],A_Sal[i],Tax[i],Cess[i],T_Tax[i],SurC[i])
