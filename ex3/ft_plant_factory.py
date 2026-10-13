class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
    ) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Rose", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    rose.show()

    print("Created: ", end="")
    oak.show()

    print("Created: ", end="")
    cactus.show()

    print("Created: ", end="")
    sunflower.show()

    print("Created: ", end="")
    fern.show()



if __name__ == "__main__":
    main()
