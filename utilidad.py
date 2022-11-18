'''lo que propone la ZCA es trabajar con una metodología basada en la interfaz. Se busca una utilidad que sea capaz de proveer un servicio identificado por dicha interfaz. Por detrás pueden existir muchas otras funcionalidades, comenzando por el hecho de poder registrar las utilidades e invocarlas, a continuación, desde otra sección del código.
Se declaran la interfaz, la clase y la instancia:'''


from zope.interface import Interface, implementer  


class IidGenerator(Interface):   
    def get(self):   
        """Provee un id único"""

    def getIdFor(self, category):  
        """Provee un id único para cada categoría"""  
    def getIdFores(self, category, name):   
        """Provee un id único para cada categoría y nombre"""
   
@implementer(IidGenerator)   
class IdGenerator(object):   
    """Generador de ids"""

    def __init__(self):   
        self.id = 0   
        self.ids = {}   
        self.ids['default'] = 0

    def get(self):   
        """Provee un id único"""   
        self.id += 1
        return self.id  
        
   
    def getIdFor(self, category):   
        """Provee un id único para cada categoría"""  
        if category not in self.ids.keys():   
            self.ids[category] = 0   
        self.ids[category] += 1   
        return self.ids[category]  

    def getIdFores(self, category, name):   
        """Provee un id único para cada categoría y nombre"""   
        if category not in self.ids.keys():   
            self.ids[category] = {}   
        if name not in self.ids[category].keys():   
            self.ids[category][name] = 0   
        self.ids[category][name] += 1   
        return self.ids[category][name]

    
id_generator = IdGenerator()
print(id_generator.get())
id_generator.getIdFor('default')
print(id_generator.getIdFor('default'))
id_generator.getIdFor('default')
#id_generator.getIdFores('default', 'default')
#id_generator.getIdFores('default', 'default')


