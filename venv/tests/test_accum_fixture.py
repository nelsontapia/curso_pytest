"""
This module contains basic unit tests for the accum module. using fixtures
their pupose is to show how to iuse the pytest framework by example
"""

import pytest
from stuff.accum import Accumulator


@pytest.fixture()
def accum():
    return Accumulator()

def test_accumulator_init(accum):
    #accum = Accumulator()
    assert accum.count == 0

@pytest.mark.math
def test_accumulator_add_one(accum):
    #accum = Accumulator()
    accum.add()
    assert accum.count == 1

@pytest.mark.accumulator
def test_accumulator_add_three(accum):
    #accum = Accumulator()
    accum.add(3)
    assert accum.count == 3

@pytest.mark.math
def test_accumulator_add_twice(accum):
    #accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2

@pytest.mark.math
def test_accumulator_cannot_set_count_directly(accum):
    #accum = Accumulator()
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10


