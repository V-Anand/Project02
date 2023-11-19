#!/usr/bin/env python
def genAdapter(name):
  comment = '''
  Convert the interface of one class into another interface that clients expect
  '''
  usecase = '''
  Integrating legacy systems, making incompatible classes work together
  '''

def genBridge(name):
  comment = '''
  Decouple an abstraction from its implementation, allowing them to vary independently
  '''
  usecase = '''
  Separating an abstraction from its implementation, supporting multiple implementations of an abstraction
  '''
def genDecorator(name):
  comment = '''
  Dynamically add new behaviors to an object by wrapping it with one or more decorators
  '''
  usecase = '''
  Adding additional features or responsibilities to an object without modifying its core functionality
  '''

def genComposite(name):
  comment = '''
  Compose objects into tree-like structures to represent part-whole hierarchies
  '''
  usecase = '''
  Representing hierarchies of objects, treating individual objects and compositions uniformly
  '''

def genFacade(name):
  comment = '''
  Provide a simplified interface to a complex system or set of classes
  '''
  usecase = '''
  Hiding complex subsystems, providing a higher-level interface for clients
  '''

def genFlyweight(name):
  comment = '''
  Efficiently share objects to minimize memory usage
  '''
  usecase = '''
  Managing large numbers of similar objects with shared state
  '''

def genProxy(name):
  comment = '''
  Control access to an object or add functionality through an intermediary object
  '''
  usecase='''
  Access control, lazy initialiation, remote communications, caching, loggine.
  '''
  
def generate(type, prefix):
  if type == None:
    type = 'Adapter'
  if prefix == None:
    prefix = 'Example'
  name = "%s%s" % (prefix, type)  
  if type == 'Adapter':
    genAdapter(name)
  elif type == 'Bridge':
    genBridge(name)
  elif type == 'Decorator':
    genDecorator(name)
  elif type == 'Composite':
    genComposite(name)
  elif type == 'Facade':
    genFacade(name)
  elif type == 'Flyweight':
    genFlyweight(name)
  elif type == 'Proxy'
    genProxy(name)
  
if __name__ == '__main__':
  import sys
  generate(sys.argv[1], sys.argv[2])
