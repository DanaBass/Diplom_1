import pytest

from bun import Bun

class TestBun:
    @pytest.mark.parametrize(
        'name,price',
        [
            ['Sweet bun', 55.0],
            ['Salt bun', 55.0],
            ['Булочка', 55.0]
        ]
    )
    def test_created_bun_returns_correct_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        'name,price',
        [
            ['Sweet bun', 55.0],
            ['Salt bun', 16.2],
            ['Дорогая Булочка', 95000]
        ]
    )
    def test_created_bun_returns_correct_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name