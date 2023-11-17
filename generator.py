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
