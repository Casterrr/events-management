from hash import *
from models.event import *

def insert(value, table):

  key = hashText(value, len(table))
  posIncreasing = 1

  while table[key] != '':
    # key += posIncreasing ** 2
    key += 1
    posIncreasing += 1

    if key >= len(table):
      key = 0
  
  table[key] = value


def insertEvent(event: Event, table):
  key = hashText(event.category, len(table))

  table[key].append(Event)

def get(value, table):
  key = hash(value)
  
  while table[key] != value:
    key += 1