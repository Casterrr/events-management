from hashMap import *
from utils import *

def insertEvent(eventsTable: HashMap):
  category = input("Digite o nome da categoria do evento: ")
  name = input("Digite o nome do evento: ")
  description = input("Digite a descrição do evento: ")

  event = {"category": category, "name":name, "description":description}

  eventsTable.put(event)

  print('\nEvento inserido com sucesso!')

def removeEvent(eventsTable: HashMap):
  if not hasCategories(eventsTable):
    return
  
  eventCategory = input("Digite a categoria do evento: ")

  if not categoryExists(eventsTable, eventCategory):
    return

  eventName = input("Digite o nome do evento: ")

  if not hasEvent(eventsTable, eventCategory, eventName):
    return

  eventsTable.removeEvent(eventCategory, eventName)


def listCategories(eventsTable: HashMap):
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

def listEventsByCategory(eventsTable: HashMap):
  if not hasCategories(eventsTable):
    return

  eventCategory = input("Digite a categoria de evento: ")

  if not categoryExists(eventsTable, eventCategory):
    return

  events = eventsTable.getEventsByCategory(eventCategory)

  if not events:
    return print('Categoria não possui eventos')

  return printEvents(events)
