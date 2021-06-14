class LoopFor:

    def __init__(self):
        pass

    def useFor(self):
        name = "Daniel"
        data = ["Daniel", 50, True]
        numbers = (2, 5.6, 4, 1)
        teacher = [{"nombre": "Erick", "final": 70}, {"nombre": "Yady", "final": 60},\
                   {"nombre": "Danny", "final": 90}]
        
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
        length = len(data)
        # print(data[0])
        # print(data[1])
        # print(data[2])
        j = 0
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
        print("~ 7Exercise.")
        for dato in numbers:
            print(" ! Dato:", dato)


use_of_for = LoopFor()
use_of_for.useFor()
