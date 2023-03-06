class Ingredientes:
    def __init__(self,nombre_ing,unidad_medida,cantidad):
        self.cantidad=cantidad
        self.unidad_medida=unidad_medida
        self.nombre_ing=nombre_ing
        
        
# import json
#     def cargar_datos(ruta):
#         with open(ruta) as contenido:
#         cursos = json.loads(contenido)
#         for curso in cursos:
#             print(curso.get('nombre'))
# if __name__ == '__main__':
#     ruta = 'data/cursos.json*
#     cargar_datos(ruta)
        