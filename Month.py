NLP=((" January ", 31), ("February", 28), ("March ", 31),("April", 30), ("May", 31), (" June", 30), ("July ", 31),("August ", 31), (" September ", 30), ("October ", 31),("November",30), ("December ",31))
LP=((" January ", 31), ("February", 29), ("March ", 31),("April", 30), ("May", 31), (" June", 30), ("July ", 31),("August ", 31), (" September ", 30), ("October ", 31),("November",30), ("December ",31))

Y=int(input("Enter A Year "))
if len(str(Y))==4:
    if Y%4==0:
        print("Month No         Month Name          Days")
        for i in range(12):
            print("%d                %s                %d"%(i,(LP[i])[0],(LP[i])[1]))
    else:
        print(NLP)
else:
    print("Invalid Input")            