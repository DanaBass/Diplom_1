from typing import List

import pytest
import ingredient_types
from bun import Bun
from burger import Burger
from ingredient import Ingredient


class TestBurger:

    def test_set_buns_for_empty_burger_bun_is_setted(self, empty_burger):
        bun = Bun('Sweet bun', 55.0)
        empty_burger.set_buns(bun)

        assert  empty_burger.bun == bun

    @pytest.mark.parametrize(
        'ingredients',
        [
            [
                Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "Ingredient_1", 777.09)
            ],
            [
                Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "Ingredient_1", 777.09),
                Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, "Ingredient_2", 1000.4)
            ],
        ]
    )
    def test_set_ingrediend_for_empty_burger_correct_count_is_setted(self, empty_burger, ingredients):
        for ingredient in ingredients:
            empty_burger.add_ingredient(ingredient)

        assert len(empty_burger.ingredients) == len(ingredients)

    def test_remove_first_ingredient_for_burger_with_two_ingridients_second_remains(self, empty_burger):
        first_ingridient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "Ingredient_1", 777.09),
        second_ingridient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, "Ingredient_2", 1000.4)

        empty_burger.add_ingredient(first_ingridient)
        empty_burger.add_ingredient(second_ingridient)

        empty_burger.remove_ingredient(0)

        assert len(empty_burger.ingredients) == 1 and empty_burger.ingredients[0] == second_ingridient

    def test_move_ingredient_from_first_to_second_position_works_correctly(self, empty_burger):
        ingredient1 = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "sause 1", 15)
        ingredient2 = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, "filling 1", 15)
        empty_burger.add_ingredient(ingredient1)
        empty_burger.add_ingredient(ingredient2)

        # Перемещение с первой на вторую на вторую позицию
        empty_burger.move_ingredient(0, 1)

        assert empty_burger.ingredients[0].get_name() == "filling 1" and empty_burger.ingredients[1].get_name() == "sause 1"

    @pytest.mark.parametrize(
        'bun,ingredients,expected_price',
        [
            (
                    Bun("Булочка", 200),
                    [
                        Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "Вкусный соус", 355.50),
                        Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "Ingredient_1", 700.99),
                    ],
                    1456.49
            ),
            (
                    Bun("Дорогая булочка", 69099),
                    [
                        Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "Вкусный соус", 4000),
                        Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "Очень дорогая начинка", 200000.22),
                    ],
                    342198.22
            ),
        ]
    )
    def test_get_price_returns_correct_sums(self, empty_burger, bun, ingredients, expected_price):
        self.fill_empty_burger_by_ingredients(empty_burger, bun, ingredients)

        assert empty_burger.get_price() == expected_price

    @staticmethod
    def fill_empty_burger_by_ingredients(empty_burger: Burger, bun: Bun, ingredients: List[Ingredient]):
        empty_burger.set_buns(bun)

        for ingredient in ingredients:
            empty_burger.add_ingredient(ingredient)

    @pytest.mark.parametrize("burger_setup, expected_price", [
        (lambda b, i: None, 4.0),  # только булочка
        (lambda b, i: b.add_ingredient(i), 5.5),  # булочка + один ингредиент
        (lambda b, i: (b.add_ingredient(i), b.add_ingredient(i)), 7.0)  # два ингредиента(одинаковых)
    ])
    def test_get_price_by_ingredients(self, mock_bun, mock_ingredient, burger_setup, expected_price):
        burger = Burger()
        burger.set_buns(mock_bun)

        burger_setup(burger, mock_ingredient)

        assert burger.get_price() == expected_price

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self, burger_with_one_ingredient: Burger):
        burger_with_one_ingredient.remove_ingredient(0)
        assert len(burger_with_one_ingredient.ingredients) == 0

    def test_get_receipt_returns_currect_data(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()
        assert "Вкусная булочка", "Price: 5.5" in receipt