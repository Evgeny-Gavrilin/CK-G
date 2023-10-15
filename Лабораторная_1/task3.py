list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
middle_of_players = len(list_players) // 2
list1 = list_players[:middle_of_players]
list2 = list_players[middle_of_players:]
print(list1)
print(list2)