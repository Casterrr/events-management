from models.event import *
from utils import nextSize, generateHash

class HashMapEvents:
  def __init__(self):
    self._size:int = 11
    self._slots: list = [None] * self._size
    self._values:list[Event] = [None] * self._size
    self._numberOfElements:int = 0

  #Gera o hash da categoria
  def hashEventCategory(self, category: str, hashTableSize: int):
    return generateHash(category, hashTableSize)
  #Retorna o fator de carga do HashMap
  def getLoadFactor(self):
    return self._numberOfElements / self._size
  
  def rehash(self, oldhash: int, size: int):
    return (oldhash + 1) % size

  def put(self, event: Event):
    loadFactor = self.getLoadFactor()
    #Verifica o fator de carga se está entre 0.7 e 0.8 e redimensiona a tabela para evitar de ter colisões.
    if (loadFactor >= 0.7) and (loadFactor <= 0.8):
      self.resize()
    # Gera o hash com base na categoria
    hashKey = self.hashEventCategory(event["name"], self._size)

    # Verificar se no espaço do hash está vazio
    if self._slots[hashKey] == None: 
      # Se estiver adiciona a categoria e o seu respectivo evento.
      self._slots[hashKey] = event["name"]
      self._values[hashKey] = event 
      self._numberOfElements += 1
    elif self._slots[hashKey] == event["name"]:
        self._values[hashKey] = event 
    else:
      proximo_slot = self.rehash(hashKey, self._size)
      # Enquanto houver chave no próximo slot e essa chave for diferente da chave recebida continua pegando o próximo slot
      while self._slots[proximo_slot] != None and self._slots[proximo_slot] != event["name"]:
        proximo_slot = self.rehash(proximo_slot, self._size)
      # Se tiver achando um slot vazio
      if self._slots[proximo_slot] == None:
        self._slots[proximo_slot] = event["name"]
        self._values[proximo_slot] = event
        self._numberOfElements += 1
      else:
        self._values[proximo_slot] = event
    print('size evens', self._size)

  def listEvents(self):
    events = []

    for event in self._values:
      if event != None:
        events.append(event)
    return events

  def removeEvent(self, name):
     hashKey = self.hashEventCategory(name, self._size)

     if self._slots[hashKey] != None:
       self._slots[hashKey] = None
       self._values[hashKey] = None
       print("Evento removido com sucesso!")
     else:
        print("Evento não encontrado!")

  def getCategories(self):
    return [key for key in self._slots if key is not None]

  def resize(self):
    # Salva os atributos atuais
    currentSize = self._size
    currentSlots = self._slots
    currentValues = self._values

    # Redefine o tamanho da tabela para o novo tamanho
    self._size = nextSize(self._size)
    self._slots = [None] * self._size
    self._values = [None] * self._size
    self._numberOfElements = 0

    # Percorre as chaves e valores da tabela atual e os adicionar na nova tabela
    for index in range(currentSize):
      if currentSlots[index] != None and currentValues[index] != None:
        event = currentValues[index]
        self.put(event)

  