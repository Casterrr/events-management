from hashTable import *

# FC = (número de itens)/(tamanho da tabela)

# eventos = [
#     {"name": "Tech Summit 2023", "category": "Conferência"},
#     {"name": "Inovação em TI", "category": "Seminário"},
#     {"name": "Masterclass de Desenvolvimento Web", "category": "Workshop"},
#     {"name": "Palestra Visionária: O Futuro da Tecnologia", "category": "Palestra"},
#     {"name": "Feira de Tecnologia Avançada", "category": "Feira"},
#     {"name": "Exposição de Arte Contemporânea", "category": "Exposição"},
#     {"name": "Concerto das Estrelas", "category": "Concerto"},
#     {"name": "Espetáculo de Teatro Clássico", "category": "Teatro"},
#     {"name": "Campeonato de Esportes Radicais", "category": "Esportes"},
#     {"name": "Festa na Praia: Sunset Vibes", "category": "Festa"},
#     {"name": "Festival de Gastronomia Internacional", "category": "Festival"}
# ]

eventsTable = HashEventTable()

eventsTable['Conferência'] = {"name": "Tech Summit 2023", "category": "Conferência"}
eventsTable['Conferência'] = {"name": "RogaDX 2023", "category": "Conferência"}
eventsTable['Seminário'] = {"name": "Inovação em TI", "category": "Seminário"}

print(eventsTable['Conferência'])
