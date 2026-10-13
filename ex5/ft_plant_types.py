class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
    ) -> None:
        self.name = name
        self._height = height
        self._age = age

    def grow(self, growth: float = 0.8) -> None:
        self._height += growth

    def age(self, days: int = 1) -> None:
        self._age += days

    def show(self) -> None:
        print(
            f"{self.name}: {self._height:.1f}cm, "
            f"{self._age} days old"
        )


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")

        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0

    def grow(self, growth: float = 2.1) -> None:
        super().grow(growth)
        self.nutritional_value += 0.5

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(
            f"Nutritional value: "
            f"{round(self.nutritional_value)}"
        )

def main() -> None:
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 15.0, 10, "red")

    print("\n=== Flower ===")
    rose.show()

    print("\n[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    oak = Tree("Oak", 200.0, 365, 5.0)

    print("\n=== Tree ===")
    oak.show()

    print("\n[asking the oak to produce shade]")
    oak.produce_shade()

    tomato = Vegetable("Tomato", 5.0, 10, "April")

    print("\n=== Vegetable ===")
    tomato.show()

    print("\n[make tomato grow and age for 20 days]")

    for _ in range(20):
        tomato.grow()
        tomato.age()

    tomato.show()


if __name__ == "__main__":
    main()
