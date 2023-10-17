from models.event import *
from utils import nextSize, generateHash, printEvents
from hashMapEvents import HashMapEvents

class HashMap:
  def __init__(self):
    self._size: int = 11
    self._slots:list = [None] * self._size
    self._values: list[HashMapEvents] = [[] for _ in range(self._size)]
    self._numberOfElements: int = 0

  #Gera o hash da categoria
  def hashEventCategory(self, category: str, hashTableSize: int):
    return generateHash(category, hashTableSize)
  #Retorna o fator de carga do HashMap
  def getLoadFactor(self):
    return self._numberOfElements / self._size
  # Gera um novo hash apartir do hash gerado anteriormente
  def rehash(self, oldhash: int, size: int):
    return (oldhash + 1) % size
  #Adiciona os eventos de acordo com suas respectivas categorias
  def put(self, event: Event):
    loadFactor = self.getLoadFactor()
    #Verifica o fator de carga se está entre 0.7 e 0.8 e redimensiona a tabela para evitar de ter colisões.
    if (loadFactor >= 0.7) and (loadFactor <= 0.8): 
      self.resize()
    # Gera o hash com base na categoria
    hashKey = self.hashEventCategory(event["category"], self._size)
    # Verificar se no espaço do hash está vazio
    if self._slots[hashKey] == None:
      #Se estiver adiciona a categoria e o seu respectivo evento.
      # Armazena a categoria do evento no espaço do hash
      self._slots[hashKey] = event["category"]
      # cria instancia para os eventos
      events = HashMapEvents()
      # Adiciona o evento
      events.put(event)
      self._values[hashKey] = events
      self._numberOfElements += 1
    
    else: 
      #Caso a chave da categoria ja esteja criada, apenas incrementara o evento nessa categoria.
      if self._slots[hashKey] == event["category"]: 
        events =  self._values[hashKey]
        events.put(event)

      #Se caso tiver preenchido e for outra categoria, seria um caso de colisão. Então é necessario fazer um rehash
      else:
        # Pega o próximo slot da lista de chaves a partir da função rehash
        proximo_slot = self.rehash(hashKey, self._size)
        # Enquanto houver chave no próximo slot e essa chave for diferente da chave recebida continua pegando o próximo slot
        while self._slots[proximo_slot] != None and self._slots[proximo_slot] != event["category"]:
          proximo_slot = self.rehash(proximo_slot, self._size)
        # Se tiver achando um slot vazio
        if self._slots[proximo_slot] == None: 
          self._slots[proximo_slot] = event["category"]
          events = HashMapEvents()
          events.put(event)

          self._values[proximo_slot] = events
          self._numberOfElements += 1
        else:
          events = self._values[proximo_slot] 
          events.put(event)

  def getEventsByCategory(self, eventKey: str):
    hash = self.hashEventCategory(eventKey, self._size)

    if self._slots[hash] != None and self._values[hash] != None:
      events = self._values[hash]
      return events.listEvents()

  def removeEvent(self, category, name):
     hashKey = self.hashEventCategory(category, len(self._slots))

     if self._slots[hashKey] != None and self._values[hashKey] != None:
       events = self._values[hashKey]
       events.removeEvent(name)

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
    self._values = [[] for _ in range(self._size)]
    self._numberOfElements = 0

    # Percorre as chaves e seus respectivos valores para adicionar na lista com o tamanho atualizado
    for index in range(currentSize):
      if currentSlots[index] != None and currentValues[index] != None:
        tempEvents = currentValues[index]

        for i in range(tempEvents._size):
          if tempEvents._slots[i] != None and tempEvents._values[i] != None:
            tempEvent = tempEvents._values[i]
            self.put(tempEvent)

