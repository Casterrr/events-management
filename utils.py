# from hashTable import *

def showOptions():
  print('\nO que deseja fazer?: \n')
  print('1 - Inserir um evento')
  print('2 - Remover um evento')
  print('3 - Listar categorias disponíveis')
  print('4 - Listar eventos de uma categoria')
  print('5 - Sair\n')

def hasCategories(eventsTable):
  availableCategories = eventsTable.getCategories()

  if len(availableCategories) == 0:
    print('\nNão existem categorias ou eventos disponíveis.')
    return False
  
  return True

def categoryExists(eventsTable, eventCategory):
  availableCategories = eventsTable.getCategories()
  
  if eventCategory not in availableCategories:
    print("\nEsta categoria não está disponível.")
    return False
  
  return True

def eventExists(eventsTable, eventCategory, eventName):
  categoryEvents = eventsTable.getEventsByCategory(eventCategory)
  hasEvent = False

  for event in categoryEvents:
    if (event["name"] == eventName):
      hasEvent = True
  
  if (not hasEvent):
    print("\nEste evento não existe.")

  return hasEvent

def isPrime(number):
  if number < 2:
    return False
  for i in range(2, int(number/2)):
    if number % i == 0:
      return False
  return True

def nextSize(number):
  doubledSize = 2 * number

  if doubledSize < 2:
    return 2
  nearestPrime = None
  distance = 0

  while True:
    if isPrime(doubledSize + distance):
      nearestPrime = doubledSize + distance
      break
    if isPrime(doubledSize - distance):
      nearestPrime = doubledSize - distance
      break
    distance += 1
  return nearestPrime
