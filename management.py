from hashMap import *
from crud import *

def startManagement():
  eventsTable = HashMap()

  while True:
    showOptions()

    choice = int(input("Digite a opção desejada: "))

    if(choice == 5):
      print('Programa finalizado com sucesso!')
      break
    elif(choice == 1):
      insertEvent(eventsTable)
    elif(choice == 2):
      removeEvent(eventsTable)
    elif(choice == 3):
      listCategories(eventsTable)
    elif (choice == 4):
      listEventsByCategory(eventsTable)
    else: 
      print("Selecione uma opção válida!")