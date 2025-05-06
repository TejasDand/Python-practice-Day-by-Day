# Create class Train and find booking status, train status and how much fare.

from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book(self, fro, to):
        print(f"\nTicket is booked in train no: {self.trainNo} from {fro} to {to}.")
    
    def getStatus(self):
        print(f"\nTrain no: {self.trainNo} is running on time!")

    def getFare(self, fro, to):
        print(f"\nTicket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}\n")
    

train = Train(12366)
train.book("Gujarat", "Mumbai")
train.getStatus()
train.getFare("Gujarat", "Mumbai")