# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, sep=','):
    splited1 = group1.split(sep)
    splited2 = group2.split(sep)
    final_list = list(set(splited1).intersection(splited2))
    final_list.sort()
    return final_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(f"Общий список : {find_common_participants(participants_first_group, participants_second_group, '|')}")
