#patrones de uso de la ZCA, dos interfaces y dos objetos
#que implementan las interfaces
''' from zope.interface import Interface, implements
class IAdaptador(Interface):
    def adaptar():
        pass
class Adaptador(object):
    implements(IAdaptador)
    def adaptar(self):
        print ("Adaptador")
class Adaptado(object):
    pass
class Adaptado2(object):
    pass
'''

from zope.interface import Interface, Attribute,  implements

class IPerro(Interface):
    nombre = Attribute("""Nombre del perro""")
    def ladrar(filename):
        """Método que permite hacerlo ladrar"""

class Perro(object):
    implements(IPerro)
    nombre = 'u'  
    def __init__(self, nombre):
        self.nombre = nombre
    def ladrar(self): 
        """Método que permite hacerlo ladrar"""
        print('Guau')   

class IGato(Interface):   
    nombre = Attribute("""Nombre del gato""")   
    def maullar(filename):   
        """Método que permite hacerlo maullar"""   

class Gato(object):   
    implements(IGato)   
    nombre = u''   
    def __init__(self, nombre):   
        self.nombre = nombre   
    def maullar(self):   
        """Método que permite hacerlo maullar"""  
        print('Miau')   