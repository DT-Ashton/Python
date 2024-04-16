class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self._score = score

    def print_info(self):
        print(f"ID: {self.id}, name: {self.name}, score: {self._score}")

    @property
    def score(self):
        print("Getter method called")
        return self._score

    @score.setter
    def score(self, value):
        print("Setter method called")
        self._score = value

def main():
    Ashton = Student("AL123", "Ashton", 9)
    print("Original info:", end=" ")
    Ashton.print_info()
    Ashton.score = 8
    print("After setter:", end=" ")
    Ashton.print_info()
    print(Ashton.score)

if __name__ == "__main__":
    main()

