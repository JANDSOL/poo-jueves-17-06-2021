class LoopFor:

    def __init__(self):
        pass

    def useFor(self):
        name = "Daniel"
        data = ["Daniel", 50, True]
        numbers = (2, 5.6, 4, 1)
        teacher = {"nombre": "Daniel", "edad": 50, "fac": "faci"}
        
        # exercise 1
        # print("~ 1Exercise.")
        # for i in range(5):
        #     print(" ! Número de i: {}".format(i))
        
        # exercise 2
        # print("~ 2Exercise.")
        # for i in range(2, 10):
        #     print(" ! Número de i: {}".format(i))
        
        # exercise 3
        # print("~ 3Exercise.")
        # for i in range(4, 10, 2):
        #     print(" ! Número de i: {}".format(i))

        # exercise 4
        # print("~ 4Exercise.")
        # for i in range(12, 3, -3):
        #     print(" Número de i: {}".format(i), end=";")

        # exercise 5
        # length = len(data)
        # print(data[0])
        # print(data[1])
        # print(data[2])
        # j = 0
        # print("~ 5Exercise.")
        # while j < length:
        #     print(" While datos[{}]:".format(j), data[j], end="; ")
        #     j += 1
        # print("")
        # for i in range(length-1, -1, -1):
        #     print(" For datos[{}]:".format(i), data[i], end="; ")

        # exercise 6
        # print("~ 6Exercise.")
        # for i, dato in enumerate(numbers):
        #     print(" For:", i, dato)
        
        # exercise 7
        # print("~ 7Exercise.")
        # for dato in numbers:
        #     print(" ! Dato:", dato)
        
        # exercise 8
        # print("~ 8Exercise.")
        # for dato in ['H', 'o', 'l', 'a', 'que', 'tal']:
        #     print(" ! Dato:", dato)

        # exercise 9
        # print("~ 9Exercise.")
        # print(" / Diccionario de notas.")
        # print(end="    ")
        # for key, value in teacher.items():
        #     print(key + ":" + str(value), end="; ")
        
        # exercise 10
        # print("~ 10Exercise.")
        # print(end="   ")
        # for student in list_students:
        #     for key, value in student.items():
        #         print(key + ":" + str(value), end="; ")

        # exercise 11
        # list_notes = [(30, 40), [20, 40] ,(50, 40)]
        # print("~ 11Exercise.")
        # accum = 0
        # length = 0
        # for notes in list_notes:
        #     partial = 0
        #     print("  ", notes, end="")
        #     for note in notes:
        #         length += 1
        #         accum += note
        #         partial += note
        #     partial_aver = partial/len(notes)
        #     print("\n ! Notas Parciales= {}; Promedio Parcial= {}".format(partial, partial_aver))
        # average = round((accum/length), 2)
        # print(" ! Total notas= {} - #Notas= {}; Promedio= {}".format(accum, length, average))

        # exercise 12
        # print("~ 12Exercise.")
        # list_students = [{"nombre": "Erick", "final": 70}, {"nombre": "Yady", "final": 60},\
        #                  {"nombre": "Danny", "final": 90}]
        # accum = 0
        # counter = 0
        # for students in list_students:
        #     print(" !", students)
        #     for key, value in students.items():
        #         print("  ", key, ":", value, end="")
        #         if key == "final": accum += value
        #         print("")
        #     counter += 1
        # print("  ", round((accum/counter), 2))

        # exercise 13
        print("~ 13Exercise.")
        # sentence = "Hola como estas"
        # vowels = []
        # for car in sentence:
        #     if car in ('a', 'e', 'i', 'o', 'u'):
        #         vowels.append(car)
        # print(" !", vowels)
        print(" !", [car for car in "Hola como estas" if car in ('a', 'e', 'i', 'o', 'u')])


use_of_for = LoopFor()
use_of_for.useFor()
