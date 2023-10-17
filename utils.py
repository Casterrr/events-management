def showOptions():
    print('\nO que deseja fazer?: \n')
    options = [
        '1 - Inserir um evento',
        '2 - Remover um evento',
        '3 - Listar categorias disponíveis',
        '4 - Listar eventos de uma categoria',
        '5 - Sair'
    ]
    print('\n'.join(options))
    print('')

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

def hasEvent(eventsTable, eventCategory: str, eventName:str):
  events = eventsTable.getEventsByCategory(eventCategory)
  hasEvent = False

  for event in events:
    if (event['name'] == eventName):
      hasEvent = True

  if (not hasEvent):
    print("\nEste evento não existe.")
  return hasEvent

def printEvents(events):
    count = 0

    for event in events:
      if event != None:
        count += 1
        print(f'Evento {count} - Nome: {event["name"]}, Categoria: {event["category"]}, Descrição: {event["description"]}')

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

def generateHash(word: str, tableSize: int):
    ordSum = 0
    count = 1
    for character in word:
      ordSum += (ord(character) * count)
      count += 1
    return ordSum % tableSize