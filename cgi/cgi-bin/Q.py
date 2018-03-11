#!/usr/bin/env python3
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

c = 1004.5 
P = 1000
R = 8.31446
M = 28.98
S = 25
H = 2.5
Ss=10
Rp=1.24

#полученные значения
T2 = 28
T1 = 17
Tn = -10+273
T2=T2+273
T1=T1+273

p = 101325
t=60
Q=[]
Q.insert(0,0)

#Q потерь

Qp= Rp*(T1-Tn)*Ss*(1+0.05)
print("потери= %f" % Qp)

i=0

Qt=(c*S*H*p*M/(R*T1))*(T2-T1)/1000
QP=Qt/t
print(QP)
print(Qt)

i=0
while Q[i] < Qt:
    i=i+1
    Q.insert(i,Q[i-1]+QP)
   # print("%d %f" % (i,Q[i]))
   # print("%f" % (Q[t+1])) 

i=1
T=T1;
c1=(c*S*H*p*M/(R*1000))
c2=Rp*Ss*(1+0.05)
Qtt=Qt
SP=0
P1=Qt/600;
P=P1+Qp
while Qt>0:
    i=i+1
    T=c1*T2/(Qt+c1)
    SP=SP+Qp
    Qp= (T-Tn)*c2
    Qt=Qt+Qp-P
    #print(T)
    if(i%60==0):
        print("%d %f %f %f %f" % (i/60,T,Qt,Qp,P))
        P=Qp+P1
SP=SP/600    
        

i=1
T=T1
P1=Qtt/600;
P=P1+SP
while Qtt>0:
    i=i+1
    T=c1*T2/(Qtt+c1)
    Qp= (T-Tn)*c2
    Qtt=Qtt+Qp-P
    #print(T)
    if(i%60==0):
        print("%d %f %f %f %f" % (i/60,T,Qtt,Qp,P))
        P=P1+SP
x=np.zeros((20,20,60))
g=np.zeros((20,20,60))
u=np.zeros((20,20,60))

#print(x)
print(x.shape)
i=1


while i<20:
    x[i][i][0]=T1
    x[i][i][59]=T2
    i=i+1
    
i=0
j=0
l=0
while l<59:
    while i<20:
        while j<20:     
            u[j][i][l]=(i+1)*50
            j=j+1
        j=0
        i=i+1
    i=0    
    l=l+1  
#print(u[:][:][1])


i=0
j=0
k=0
while i<20:
    while k<20:
        while j<58:
            x[k][i][j]=c1*T2/(g[k][i][j]+c1)
            Qp= (x[k][i][j]-Tn)*c2*10
            if x[k][i][j]<T2:              
                g[k][i][j+1]=g[k][i][j]+Qp-u[k][i][j]
                u[k][i][j+1]=u[k][i][j]
                
            else:             
                g[k][i][j+1]=g[k][i][j]+Qp-u[k][i][j]
                u[k][i][j+1]=int(Qp/10)
                
            
            j=j+1
        j=0
        k=k+1
    k=0
    i=i+1
i=0
j=0
k=0

ax=axes3d.Axes3D(plt.figure())
i=np.arange(0,20,1)
X,Y = np.meshgrid(i,i)
#ax.plot_wireframe(X,Y,, rstride=10, cstride=10)
#plt.show()
print(x[1][1][:])
#print(x)
time.sleep(10000)
