class Parrot:
    species="Bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Parrot("Blu",11)
p2=Parrot("Rio",12)

#To access the clss variable
print("Blu is {}".format(p1.species))
print("Rio is {}".format(p2.species))

#Instance variables
print("{0} is {1} years old".format(p1.name,p1.age))
print("{0} is {1} years old".format(p2.name,p2.age))