a = 809
for i in range(10,100):
    b = i * a
    if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
      
        print("%d=800*%d+9*%d"%(b,i,i))
