


def solver (a,b,c,d,x):
    result = []
    for i in range (0,len(a)):
        for j in range (0,len(x)):
            iter = a[i]*x[j]*x[j]*x[j]+b[i]*x[j]*x[j]+c[i]*x[j]+d[i]
            result.append(iter)
    print (result)
    print ("%.4f" % max(result),"%.4f" % min(result))


A = [3.1,2.1,1.6]
B = [10.3,8.8,0.2]
C = [-2.8,-11.4,-20.8]
D = [10.3,-5.6,38.5]
X = [-4,-3,-2,-1,0,1]
solver (A,B,C,D,X)
    