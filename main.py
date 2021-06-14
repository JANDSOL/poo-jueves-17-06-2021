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
        print("~ 3Exercise.")
        for i in range(4, 10, 2):
            print(" ! Número de i: {}".format(i))


use_of_for = LoopFor()
use_of_for.useFor()
