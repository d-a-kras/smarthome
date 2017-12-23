#!/usr/bin/env python3
c = 1004.5 
P = 1000
R = 8.31446
M = 28.98
S = 25
H = 2.5
Ss=10
Rp=1.24

#полученные значения
T2 = 22
T1 = 17
Tn = -10
T2=T2+273
T1=T1+273

p = 101325
t=60
Q=[]
Q.insert(0,0)

#Q потерь

Qp= Rp*(T1-Tn-273)*Ss*(1+0.05)
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
    T=c1*T2/(Qt+c1)-273
    SP=SP+Qp
    Qp= (T-Tn)*c2
    Qt=Qt+Qp-P
    #print(T)
    if(i%60==0):
        print("%d %f %f %f %f" % (i/60,T,Qt,Qp,P))
        P=Qp+P1
SP=SP/600    
        

i=1
T=T1;
c1=(c*S*H*p*M/(R*1000))
c2=Rp*Ss*(1+0.05)
P1=Qtt/600;
P=P1+SP
while Qtt>0:
    i=i+1
    T=c1*T2/(Qtt+c1)-273
    Qp= (T-Tn)*c2
    Qtt=Qtt+Qp-P
    #print(T)
    if(i%60==0):
        print("%d %f %f %f %f" % (i/60,T,Qtt,Qp,P))
        P=P1+SP
