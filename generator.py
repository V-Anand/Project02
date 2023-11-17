#!/usr/bin/env python
def genAdapter(name):
  className = "%sAdapter" % name
  
def generate(type, name):
  if type == None:
    type = 'Adapter'
  if name == None:
    name = 'Example'
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
