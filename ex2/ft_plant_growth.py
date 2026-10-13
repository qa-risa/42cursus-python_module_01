class Plant:
    name: str
    height: float
    plant_age: int

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.plant_age} days old"
        )

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.plant_age += 1

def main() -> None:
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.plant_age = 30

    print("=== Garden Plant Growth ===")
    rose.show()

    starting_height: float = rose.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    growth = round(rose.height - starting_height, 1)
    print(f"Growth this week: {growth}cm")


if __name__ == "__main__":
    main()
