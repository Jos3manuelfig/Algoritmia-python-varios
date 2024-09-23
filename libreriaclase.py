class libria:
   def __init__(self,libros,usuarios,prestamos)->None:
        self.libros=[]
        self.usuarios=[]
        self.prestamos=[]
   def add_libros(self,titulo,autor,copias):
    self.libros.append({'libros':libros, 'Tirulo' : titulo, 'Copias': copias})
    def add_usuarios(self,id,name):
    self.usuarios.append({'ID':id, 'Nombre' : name})
    
    