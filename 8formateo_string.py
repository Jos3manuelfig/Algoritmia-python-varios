# formaterar string con 
# fubcion format
#% s ---> pars string
#%d---->para numeros


n= int(input('Ingrese un Numero:'))

nn=int('{}{}'.format(n,n))
nnn=int('%d%d%d' %(n,n,n,))
print(nn)
print(nnn)