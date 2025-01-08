import pytest

from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_database_initialized_without_errors(self):
        is_success = True
        try:
            database = Database()
        except:
            is_success = False

        assert is_success

    def test_available_buns_returns_correct_data(self, default_database):
        assert default_database.available_buns() == default_database.buns

    def test_available_ingredients_returns_correct_data(self, default_database):
        assert default_database.available_ingredients() == default_database.ingredients

    @pytest.mark.parametrize("ingredient_name, ingredient_type", [
        ("hot sauce", INGREDIENT_TYPE_SAUCE),
        ("sour cream", INGREDIENT_TYPE_SAUCE),
        ("chili sauce", INGREDIENT_TYPE_SAUCE),
        ("cutlet", INGREDIENT_TYPE_FILLING),
        ("dinosaur", INGREDIENT_TYPE_FILLING),
        ("sausage", INGREDIENT_TYPE_FILLING),
    ])
    def test_ingredient_types(self, default_database, ingredient_name, ingredient_type):
        ingredients = default_database.available_ingredients()
        ingredient = next(i for i in ingredients if i.name == ingredient_name)

        assert ingredient.type == ingredient_type
