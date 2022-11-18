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

from zope.interface import Interface, Attribute, implementer

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


class IGato(Interface):
  
    nombre = Attribute("""Nombre del gato""")
    def maullar(filename):
        """Método que permite hacerlo maullar"""

@implementer(IGato)
class Gato(object):  
   
    nombre = 'u'   
    def __init__(self, nombre):
        self.nombre = nombre
    def maullar(self):
        """Método que permite hacerlo maullar"""
        print('Miau')