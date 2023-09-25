from bear_bat import BearBat
import pytest


# bear body stuffing scale = 1 to 10, skinny to fluffy fat
# bat wings can be small, medium or large
def test_bear_bat_creation():
    # name, arms, legs, body, ears, e_n_m, bat_wings
    bear = BearBat("Sir Batty Bat", "short", "long", 10, "round", "blue, black, big", "large")
    assert bear.name == "Sir Batty Bat"
    assert bear.arms == "short"
    assert bear.legs == "long"
    assert bear.body == 10
    assert bear.ears == "round"
    assert bear.e_n_m == "blue, black, big"
    # my modification to the bear
    assert bear.bat_wings == "large"
    assert bear.energy == 1000


def test_flying():
    bear_flying = BearBat("Sir Batty Bat", "short", "long", 10, "round", "blue, black, big", "large")
    flying = bear_flying.flying(flapping=20)
    assert flying is True

