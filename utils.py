from hashTable import *

def showOptions():
  print('\nO que deseja fazer?: \n')
  print('1 - Inserir um evento')
  print('2 - Remover um evento')
  print('3 - Listar categorias disponíveis')
  print('4 - Listar eventos de uma categoria')
  print('5 - Sair\n')

def hasCategories(eventsTable: HashEventTable):
  availableCategories = eventsTable.getCategories()

  if len(availableCategories) == 0:
    print('\nNão existem categorias ou eventos disponíveis.')
    return False
  
  return True

def categoryExists(eventsTable: HashEventTable, eventCategory):
  availableCategories = eventsTable.getCategories()
  
  if eventCategory not in availableCategories:
    print("\nEsta categoria não está disponível.")
    return False
  
  return True