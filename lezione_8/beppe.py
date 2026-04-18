import numpy as np
import matplotlib.pyplot as plt 

f_complex= lambda z: (z**2+1)*(z**2-1)
f_complex_prime=lambda z:4*z**3
#NOW THE MATRIX Z MAPS ALL THE UNITARY CIRCLE IN THE COMPLEX SPACE, TO ACCELERARATE THE ALGHORITM WE USE IT ON THE FULL MATRIX AT ONCE
#AND AS OUTPUT CONDITION WE ASSUME THE ABS OF THE MAXIMUM ENTRY OF THE MARTRIX TO BE SMALLER OF THE TOLLERANCE VALUE
###############
def newton_roots2(f,f_prime,x0,tol,N):  #where history collects the values of x during the iteration
    x=x0-f(x0)/f_prime(x0)
    
    for i in range(N):
        x=x-f(x)/f_prime(x)
        #History.append(x)(for every cicle i would append a Matrrix of 10**6 size)
        #print(np.max(abs(f(x))), f(x[0,0]))
        if np.max( np.abs(f(x)))<tol:
            print('the alghortim converges after',i,'iteration')
            return x
    print('alloraaa',np.mean(np.abs(x)))
    raise ValueError('ciao')
##############
N = 1024
x = np.linspace(-1,1,N).astype(np.float64)
X, Y = np.meshgrid(x, x)
Z = newton_roots2(f_complex,f_complex_prime,X + 1j*Y,1e-8,300)
print(Z)
fig = plt.figure()
plt.imshow(np.angle(Z), cmap="viridis")