# Huy Kevin Nguyen
# PSID: 1346435

class FoodItem:  # TODO: Define constructor with parameters to initialize instance # attributes (name, fat, carbs, protein)

    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0, num_servings=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.servings = num_servings

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

if __name__ == "__main__":
    n = input()
    f = float(input())
    c = float(input())
    p = float(input())
    s = float(input())
    food1 = FoodItem()
    food2 = FoodItem(n, f, c, p, s)
    food1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}\n'.format(s, food1.get_calories(s)))
    food2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(s, food2.get_calories(s)))



