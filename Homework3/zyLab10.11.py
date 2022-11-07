# Waleed Yusuf
# 2104654

class FoodItem:
    def __init__(self, item="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = item
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    food_nut1 = FoodItem()

    item_name = input()
    fat_info = float(input())
    carbs_info = float(input())
    protein_info = float(input())

    food_nut2 = FoodItem(item_name, fat_info, carbs_info, protein_info)

    servings = float(input())

    food_nut1.print_info()
    print(f'Number of calories for {servings:.2f} serving(s): {food_nut1.get_calories(servings):.2f}')

    print()

    food_nut2.print_info()
    print(f'Number of calories for {servings:.2f} serving(s): {food_nut2.get_calories(servings):.2f}')
