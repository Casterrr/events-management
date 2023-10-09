#  quadradict probing

def hashText(text, tableSize):
  ordSum = 0
  count = 0
  for character in text:
    ordSum += (ord(character) * count)
    count += 1
  return ordSum % tableSize


# print(hashText('Festival', 11))
# ["Conferência", "Seminário", "Workshop", "Palestra", "Feira", "Exposição", "Concerto", "Teatro", "Esportes", "Festa", "Festival"]
# ['Festa', 'Festival', 'Conferência', 'Exposição', 'Teatro', 'Palestra', 'Concerto', 'Seminário', 'Feira', 'Esportes', 'Workshop']