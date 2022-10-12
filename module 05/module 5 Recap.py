# print('Abdul', end=" ")
# print('Aouwal')

games = ['Cricket', 'Football', 'Hockey', 'Running', 'Kabaddi']
another_games = ['Chess','Ludu', 'Carrom']
# print(games[0], games[1])
# print(len(games), type(games))
# print(games[-1])
# games[-1] = 'Kabadi'
# print(games[2:])
# games.append('Swimming')
# games.insert(3,'Walking')
# games.pop(-2)
# del games[0]
# games.remove('Hockey')
# games.sort()
# print(games)

indoor_games = ['Chess','Ludu', 'Carrom']
outdoor_games = ['Cricket', 'Football', 'Kabadi']
indoors = ['Hide-and-seek','Pictionary']
sports = indoor_games + outdoor_games
indoor_games.extend(indoors)
print(sports)
print(indoor_games)
print(outdoor_games.index('Football'))