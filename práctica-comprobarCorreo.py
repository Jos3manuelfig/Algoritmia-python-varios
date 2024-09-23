def comprobar(email):
     if '@' in email:
          return True
     return False
     
     usuario,dominio=email.split('@',1)
    
     if not usuario or not dominio:
        return False
     return True


verificar=comprobar('jdjdjd@gmail.com')
print(verificar)