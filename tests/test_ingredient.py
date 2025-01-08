import pytest

from data.data import DEFAULT_INGREDIENT_NAME, DEFAULT_INGREDIENT_PRICE, DEFAULT_INGREDIENT_TYPE
from ingredient import Ingredient

class TestIngredient:

    def test_get_name_returns_expected_value(self, default_ingredient: Ingredient):
        assert default_ingredient.get_name() == DEFAULT_INGREDIENT_NAME

    def test_get_price_returns_expected_value(self, default_ingredient: Ingredient):
        assert default_ingredient.get_price() == DEFAULT_INGREDIENT_PRICE

    def test_get_type_returns_expected_value(self, default_ingredient: Ingredient):
        assert default_ingredient.get_type() == DEFAULT_INGREDIENT_TYPE