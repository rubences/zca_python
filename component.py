# adaptar ambos objetos en una única clase. Empezaremos creando una interfaz. Esta adaptación se realiza, simplemente, utilizando la función adapts.
#
# from zope.interface import Interface, Attribute, implementer
# from zope.interface import implements
# from zope.component import adapts
#


from zope.interface import Interface, Attribute, implementer
from zope.component import adapts

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

class IAdaptador(Interface):
    def adaptar():
        """Método que permite a un  Adaptador expresarse"""
        pass

@implementer(IAdaptador)
class Adaptador(object):

    adapts(Perro, Gato)
    def __init__(self, perro, gato):
        self.perro = perro
        self.gato = gato
    def adaptar(self):
        print ("Se va a expresar un Animal")
        if isinstance(self.perro, Perro):   
                    self.perro.ladrar()   
        if isinstance(self.gato, Gato):   
                    self.gato.maullar()   
        else:   
            raise Exception("Este animal no sabe expresarse")    

perro = Perro('Firulais')
gato = Gato('Garfield')
adaptador = Adaptador(perro, gato)
adaptador.adaptar()
