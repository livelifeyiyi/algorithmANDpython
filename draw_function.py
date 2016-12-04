import math

import numpy as np
import matplotlib.pyplot as plt
R_L=9.6
V_in = 400.0
V_o = 24.0
L_r=13.2e-6
C_r=213e-12
L_M=66e-6;
f_r=1.0/(2*math.pi*math.pow((C_r*L_r),-2))
C_oss = 17e-9
f_s = 3e6
a=1.0/8.0
f_n=f_s/f_r
k=L_M/L_r
Q=math.pow(math.pi,2.0)/(8.0*a*a*R_L)*math.pow((L_r/C_r),0.5)
M = 1.0/(2.0*a*math.pow((math.pow((1.0+1.0/k*(1.0-1.0/math.pow(f_n,2))),2.0) + math.pow(Q*(f_n-1/f_n),2.0)),0.5))

print Q
#print 24.0/400.0
print M
'''
x = np.linspace(0,10,1000)
y = np.M
plt.figure(figsize=(8,4))  

plt.plot(x,y,label='$M$',color='red',linewidth=2)  
plt.ylim(-1.2,1.2) 
plt.legend() 
plt.show()  
'''