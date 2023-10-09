from models.event import *

class HashEventTable:
  def __init__(self):
    self._size = 11 #
    self._slots = [None] * self._size
    self._values = [[] for _ in range(self._size)]

  def hashEventCategory(self, category: str, hashTableSize: int):
    ordSum = 0
    count = 0
    for character in category:
      ordSum += (ord(character) * count)
      count += 1
    return ordSum % hashTableSize

  def rehash(self, oldhash, size):
    return (oldhash + 1) % size
  
  def put(self, eventKey: str, eventValue: Event):
    hashKey = self.hashEventCategory(eventKey, len(self._slots))

    if self._slots[hashKey] == None: # Caso na lista de chaves não exista uma chave nesse hash
      self._slots[hashKey] = eventKey
      self._values[hashKey].append(eventValue) # Adiciona o valor na lista de valores na posição do hash da chave recebida
    else: # Caso já exista
      if self._slots[hashKey] == eventKey: # Caso a chave que já tem na lista de chaves seja igual a chave recebida
        self._values[hashKey].append(eventValue) # Adiciona o valor na lista de valores na posição do hash da chave recebida
      else: # Caso não seja igual
        proximo_slot = self.rehash(hashKey, len(self._slots)) # Pega o próximo slot da lista de chaves a partir da função rehash
        
        while self._slots[proximo_slot] != None and self._slots[proximo_slot] != eventKey: # Enquanto houver chave no próximo slot e essa chave for diferente da chave recebida
          proximo_slot = self.rehash(proximo_slot, len(self._slots)) # Continua pegando o próximo slot
        
        if self._slots[proximo_slot] == None: # Se tiver achando um slot vazio
          self._slots[proximo_slot] = eventKey
          self._values[proximo_slot].append(eventValue) # Adiciona na lista de valores da chave
        else: # Se tiver achado um slot ocupado
          self._values[proximo_slot].append(eventValue) # Adiciona na lista de valores da chave

  def getEventsByCategory(self, eventKey: str):
    slot_inicial = self.hashEventCategory(eventKey, len(self._slots))

    valor = None
    parar = False
    encontrou = False
    posicao = slot_inicial

    while self._slots[posicao] != None and not encontrou and not parar: # Enquanto houver chave na lista de chaves na posição do hash da chave recebida e não tiver encontrado o valor da chave recebida
      if self._slots[posicao] == eventKey: # Se a chave encontrada for igual a chave recebida
        encontrou = True
        valor = self._values[posicao] # Define o valor a ser retornado com o valor da lista de valores no hash/rehash da chave recebida
      else: # Caso contrário, significa que a chave recebida deve estar em um rehash
        posicao = self.rehash(posicao, len(self._slots)) # Pega o rehash da chave recebida

        if posicao == slot_inicial: # Para evitar que fique num ciclo de rehash infinito
          parar = True # Oberse que nesse caso, o valor não pôde ser encontrado, e o valor retornado será None.
    
    return valor

  def removeEvent(self, eventKey, eventName):
    categoryEvents = self.getEventsByCategory(eventKey) # Pega a lista de eventos da categoria recebida
    categoryPosition = self._values.index(categoryEvents) # Pega a posição da lista de eventos na lista de valores de cada categoria

    for event in categoryEvents: # Para cada evento na lista de eventos
      if event["name"] == eventName: # Se o nome do evento da lista for igual ao nome de evento recebido
        categoryEvents.remove(event) # Remove o evento da lista
    
    self._values[categoryPosition] = categoryEvents # Atualiza a lista de eventos da categoria recebida, tornando-a a lista com o evento removido

  def listCategories(self):
    return [key for key in self._slots if key is not None]

  def __getitem__(self, eventKey: str):
    return self.getEventsByCategory(eventKey)
  
  def __setitem__(self, eventKey: str, valor: Event):
    self.put(eventKey, valor)
