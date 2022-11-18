#patrones de uso de la ZCA, dos interfaces y dos objetos
#que implementan las interfaces
from zope.interface import Interface, implements
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
