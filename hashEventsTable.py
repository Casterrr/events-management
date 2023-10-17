from models.event import *
from utils import nextSize

class HashEventsTable:
  def __init__(self):
    self._size = 11 
    self._slots = [None] * self._size
    self._values = [None] * self._size
    self._numberOfElements = 0

  def __setitem__(self, eventKey: str, valor: Event):
    self.put(eventKey, valor, True)

  def hashEventCategory(self, category: str, hashTableSize: int):
    ordSum = 0
    count = 0
    for character in category:
      ordSum += (ord(character) * count)
      count += 1
    return ordSum % hashTableSize

  def rehash(self, oldhash: int, size: int):
    return (oldhash + 1) % size

  def put(self, event: Event, shouldResize: bool = False):
    FC = (self._numberOfElements / self._size) # Verifica o fator de carga
    if ((FC >= 0.7) and (FC <= 0.8) and shouldResize): # Se eestiver entre 0.7 e 0.8, redimensiona
      self.resize()

    hashKey = self.hashEventCategory(event["name"], len(self._slots))

    print("hash", hashKey)

    if self._slots[hashKey] == None: # Caso na lista de chaves não exista uma chave nesse hash
      self._slots[hashKey] = event["name"]
      self._values[hashKey] = event # Adiciona o valor na lista de valores na posição do hash da chave recebida
      self._numberOfElements += 1
    elif self._slots[hashKey] == event["name"]:
      self._values[hashKey] = event # Adiciona o valor na lista de valores na posição do hash da chave recebida
      self._numberOfElements += 1
    else:
      return
      # se cair aqui é pq ta tendo colisao com outro evento...

    # else: # Caso já exista
    #   if self._slots[hashKey] == eventKey: # Caso a chave que já tem na lista de chaves seja igual a chave recebida
    #     self._values[hashKey].append(eventValue) # Adiciona o valor na lista de valores na posição do hash da chave recebida
    #   else: # Caso não seja igual
    #     proximo_slot = self.rehash(hashKey, len(self._slots)) # Pega o próximo slot da lista de chaves a partir da função rehash
        
    #     while self._slots[proximo_slot] != None and self._slots[proximo_slot] != eventKey: # Enquanto houver chave no próximo slot e essa chave for diferente da chave recebida
    #       proximo_slot = self.rehash(proximo_slot, len(self._slots)) # Continua pegando o próximo slot
        
    #     if self._slots[proximo_slot] == None: # Se tiver achando um slot vazio
    #       self._slots[proximo_slot] = eventKey
    #       self._values[proximo_slot].append(eventValue) # Adiciona na lista de valores da chave
    #       self._numberOfElements += 1
    #     else: # Se tiver achado um slot ocupado
    #       self._values[proximo_slot].append(eventValue) # Adiciona na lista de valores da chave
    #       self._numberOfElements += 1

    

  def listEvents(self):
    count = 0

    for event in self._values:
      if event != None:
        count += 1
        print(f'Evento {count} - Nome: {event["name"]}, Categoria: {event["category"]}, Descrição: {event["description"]}')

  def removeEvent(self, name):
     hashKey = self.hashEventCategory(name, len(self._slots))

     if self._slots[hashKey] !=None:
       self._slots[hashKey] = None
       self._values[hashKey] = None
       print("Evento removido com sucesso!")

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

    # Percorre as chaves e valores da tabela atual e os adicionar na nova tabela
    for index in range(currentSize):
      if (currentSlots[index] != None):
        tempEvent = self.getEventsByCategory(currentSlots[index], values = currentValues, slots = currentSlots)

        self.put(currentSlots[index], tempEvent)

  