from hashTable import *
from utils import *

def insertEvent(eventsTable: HashEventTable):
  eventCategory = input("Digite a categoria do evento: ")
  eventName = input("Digite o nome do evento: ")
  eventDesc = input("Digite a descrição do evento: ")

  # eventsTable.put(eventCategory, {"name": eventName, "category": eventCategory, "description": eventDesc})
  eventsTable[eventCategory] = {"name": eventName, "category": eventCategory, "description": eventDesc}

  print('\nEvento inserido com sucesso!')

def removeEvent(eventsTable: HashEventTable):
  if not hasCategories(eventsTable):
    return
  
  eventCategory = input("Digite a categoria do evento: ")

  if not categoryExists(eventsTable, eventCategory):
    return

  eventName = input("Digite o nome do evento: ")

  if not eventExists(eventsTable, eventCategory, eventName):
    return

  eventsTable.removeEvent(eventCategory, eventName)

  print('\nEvento removido com sucesso!')

def listCategories(eventsTable: HashEventTable):
  if not hasCategories(eventsTable):
    return
  
  availableCategories = eventsTable.getCategories()
  print('\nAs seguintes categorias estão disponíveis: \n')

  for category in availableCategories:
    if availableCategories.index(category) == len(availableCategories) - 1:
      print(f'{category}', end='.')
    else:
      print(f'{category}', end=', ')

  print('')

def listEventsByCategory(eventsTable: HashEventTable):
  if not hasCategories(eventsTable):
    return

  eventCategory = input("Digite a categoria de evento: ")

  if not categoryExists(eventsTable, eventCategory):
    return

  categoryEvents = eventsTable.getEventsByCategory(eventCategory)

  if (categoryEvents != None):
    count = 1
    print('')
    for event in categoryEvents:
      print(f'Evento {count} - Nome: {event["name"]}, Categoria: {event["category"]}, Descrição: {event["description"]}')
      count += 1
  else:
    print('Não há eventos nesta categoria.')