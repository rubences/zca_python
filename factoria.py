'''Se ha presentado antes la noción de fábrica y cómo implementar este patrón de diseño de manera sencilla con Python. La ZCA utiliza con frecuencia este patrón de diseño y, en consecuencia, se le presta bastante atención para permitir un uso sencillo y eficaz. Una fábrica es una utilidad que implementa la interfaz IFactory, de modo que se provee un objeto genérico Factory.'''

from zope.interface import Interface, Attribute, implementer
from zope.component.factory import Factory 

class IFactory(Interface):
    def __call__():
        """Método que permite crear un objeto"""
        pass

'''@implementer(IFactory)
class Factory(object):
    def __init__(self, clase):
        self.clase = clase
    def __call__(self):
        return self.clase()'''

@implementer(IFactory)       
class IPerro(Interface):   
      nombre = Attribute("""Nombre del perro""")  
      def ladrar(filename):   
          """Método que permite hacerlo ladrar"""  

@implementer(IPerro)    
class Perro(object):   
    nombre = 'u'
    def __init__(self, nombre):   
          self.nombre = nombre   
    def ladrar(self):   
          """Método que permite hacerlo ladrar"""  
          print('Guau')  
    
factory = Factory(Perro, 'Perro') 
perro = factory("Manolo")
print(perro.nombre)
perro.ladrar()
