from unittest.mock import Mock

import pytest

from burger import Burger
from data.data import DEFAULT_INGREDIENT_NAME, DEFAULT_INGREDIENT_TYPE, DEFAULT_INGREDIENT_PRICE
from database import Database
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING


@pytest.fixture()
def empty_burger():
    return Burger()

@pytest.fixture
def default_ingredient():
    return Ingredient(DEFAULT_INGREDIENT_TYPE, DEFAULT_INGREDIENT_NAME, DEFAULT_INGREDIENT_PRICE)

@pytest.fixture
def default_database():
    return Database()

@pytest.fixture()
def mock_bun():
    bun = Mock()
    bun.get_price.return_value = 2
    bun.get_name.return_value = 'Вкусная булочка'
    return bun

@pytest.fixture()
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_price.return_value = 1.5
    ingredient.get_name.return_value = 'Вкусная начинка'
    ingredient.get_type.return_Value = INGREDIENT_TYPE_FILLING
    return ingredient

@pytest.fixture()
def burger_with_one_ingredient():
    burger = Burger()
    burger.ingredients.append(mock_ingredient)

    return burger