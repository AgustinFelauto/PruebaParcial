from datetime import datetime

class producto:
    def __init__(self):
        self.descripcion:str = ""
        self.id:int = 0
        self.fechaexp:datetime = None
        self.info:str =""
         
    def set_descripcion (self,texto):
        self.descripcion = texto
 
    def set_id (self, numero):
        self.id = numero
        
    def set_fechaexp (self, fecha:datetime):
        self.fechaexp = fecha
       
    def set_info (self, info):
        self.info = info     
    
    def calcular_vencimiento (self):
        if self.fechaexp < datetime.now():
            print(f"El producto esta vencido, expiro el {self.fechaexp}")
        else:
            print(f"El producto expira en {self.fechaexp - datetime.now()}")
            
                
                         
producto1 = producto ()           
producto1.set_descripcion ("soy el producto1")            
producto1.set_id (1)            
producto1.set_fechaexp (datetime(2023,1,1))
producto1.set_info ("info producto1")
producto1.calcular_vencimiento ()    
    
producto2 = producto ()           
producto2.set_descripcion ("soy el prodcuto2")            
producto2.set_id (2)            
producto2.set_fechaexp (datetime(2023,7,7))
producto2.set_info ("info producto2")
producto2.calcular_vencimiento ()


