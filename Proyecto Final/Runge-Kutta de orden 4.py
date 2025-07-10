"""
Proyecto de Implementacion 
Runge-Kutta de orden 4
"""
def funcionF(x,y):  #esta funcion representa la E.D. dada por el problema
    return y*(1-0.001*y)

def kutta1(h,x,y): #esta funcion calcula el valor de K1 para Runge-Kutta de orden 4
    return (h*funcionF(x,y))
    
def kutta2(h,x,y,k): #esta funcion calcula el valor de K2 para Runge-Kutta de orden 4
    return ( h*funcionF( x+(h/2) , y+(k)/2 ) )

def kutta3(h,x,y,k): #esta funcion calcula el valor de K3 para Runge-Kutta de orden 4
    return ( h*funcionF( x+h , y+k ) )
      
def kutta4(h,x,y,k): #esta funcion calcula el valor de K4 para Runge-Kutta de orden 4
    return ( h*funcionF( x+h , y+k ) )


def imprimirFuncion(A,B):
    print("\n")
    print("  X    |   Y")
    print("--------------------------")
    for i in range(0,len(A)):
        print (" {0:.2f}".format(A[i])," |  {}".format(B[i]))
        
def runge_Kutta4(H,A,B):
    X=[]
    Y=[]
    X.append(A) #colocamos el valor inicial de la variable X
    Y.append(B) #colocamos el valor inicial de la variable Y
    for n in range(0,500): 

        k1=kutta1(H, X[n], Y[n])
        k2=kutta2(H, X[n], Y[n], k1)
        k3=kutta3(H, X[n], Y[n], k2)
        k4=kutta4(H, X[n], Y[n], k3)

        yN= Y[n]+(1/6)*(k1+2*k2+2*k3+k4) #calcula el valor de y(n+1) 
        
        X.append(X[n]+H) #colocamos el valor x(n+1)
        Y.append(yN) #colocamos el valor y(n+1)
        
    imprimirFuncion(X,Y) #despues de hacer todos los calculos, primimimos el resultado 

#con esta funcion llamamos a la funcion runge_Kutta4
#que recibe como parametros el valor de h y la condicion inicial     
runge_Kutta4(0.01, 0.0, 800) 