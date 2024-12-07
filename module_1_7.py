grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_sort_list = sorted(list(students))  #   созд. перемен. для списка студ. и сортируем
average_grades = (sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]),
                  sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[1]))  # перем. для списка ср. оценок
students_and_grades = dict(zip(students_sort_list, average_grades))   # созд. соловарь
print(students_and_grades)