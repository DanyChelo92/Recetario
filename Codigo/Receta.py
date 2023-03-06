import datetime
import json
import sys


class Receta:
    def __init__(self, nombre, ingredientes, preparacion, tiempo_preparacion, 
                 tiempo_coccion, etiquetas,
                 imagen=None, favorita=False):
        self.nombre=nombre
        self.ingredientes=ingredientes
        self.preparacion=preparacion
        self.imagen=imagen
        self.tiempo_preparacion=tiempo_preparacion
        self.tiempo_coccion=tiempo_coccion
        self.fecha_creacion=(str) (datetime.datetime.now().date())
        self.etiquetas=etiquetas
        self.favorita=favorita
        try:
            with open('recetas.txt','x')as archivo:
                data={}
                data['recetas']=[]
                json.dump(data,archivo,indent=4)
        except:
                pass    
        
    def crear_receta(self):
        receta={
            'Nombre':self.nombre,
            'Ingredientes':self.ingredientes,
            'Preparacion':self.preparacion,
            'Imagen':self.imagen,
            'Tiempo_prepacion':self.tiempo_preparacion,
            'Tiempo_coccion':self.tiempo_coccion,
            'Fecha_creacion':self.fecha_creacion,
            'Etiquetas':self.etiquetas,
            'Favorita':self.favorita
        }  
        
        nombre=receta.get('Nombre')          
        print(nombre)
        with open('recetas.txt','r') as archivo:
            lista=json.load(archivo)
        list_receta=[]       
        for list in lista['recetas']:
            list_receta.append(list.get('Nombre'))  
        if nombre not in list_receta:            
            with open ('recetas.txt','w') as archivo:
                archivo.write('')
            with open('recetas.txt','r+') as archivo:        
                lista['recetas'].append(receta)
                json.dump(lista,archivo,indent=4)      
    
    def modificar_receta(self):
        pass
    
    def eliminar_receta(nombre):
        try:
            with open('recetas.txt','r') as archivo:
                lista=json.load(archivo)  
            for index,receta in enumerate(lista['recetas']):
                if(receta.get('Nombre') == nombre):
                    lista['recetas'].pop(index) 
                    break
                else:
                    return print('No se encuentra elemento!!!')    
            with open ('recetas.txt','w') as archivo:
                archivo.write('')
            with open('recetas.txt','r+') as archivo:        
                json.dump(lista,archivo,indent=4)
        except:
            print('Hubo un problema, no se encuentra elemento!!!')                  
                  
    def receta_del_dia(self):
        pass
    
    def buscar_receta(self):
        pass    

ing=[[1,'unidad','papa'],[1,'kg','carne'],[2,'un','cebolla']]
et=['rico','sano','verano']
prep='''cocinar todo junto,
y sazonar a gusto'''
        
# r2=Receta('Guiso',ing,prep,400,30,et,None,False)
# r2.crear_receta()
# r1=Receta('Humita',ing,prep,400,30,et,None,False)
# r1.crear_receta() 
# r3=Receta('Empanada',ing,prep,400,30,et,None,False)
# r3.crear_receta()  
#r4=Receta('Humita',ing,prep,400,30,et,None,False)
#r4.crear_receta() 
Receta.eliminar_receta('Empanada')