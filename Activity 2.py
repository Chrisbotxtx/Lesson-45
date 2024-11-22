class Student:
    grade=10
    name="Chris"

    def Wishes(self):
        print("Hi I am a student")

    def intro(self):
        print("Hi I am",self.name)
        print("I study in grade",self.grade)

st=Student()
st.Wishes()
st.intro()

        