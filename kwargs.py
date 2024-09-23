def facturacion(*args,**kwargs):
    total= sum(args)
    descuento= kwargs.get('descuento',0)
    impuesto=kwargs.get('impuesto',0)
    total+=total *descuento
    total-=total*impuesto
    return total 
a = facturacion(100,20,300,descuento=0.20, impuesto=0.30)

print('Total' ,a)
    
    
    

    
