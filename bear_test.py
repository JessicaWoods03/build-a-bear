import random

from bear import Bear
import pytest


# basic unit test
def test_bear_creation():
    # name, arms, legs, body, ears, e_n_m
    bear = Bear("Sir Bear", "short", "long", 10, "round", "blue, black, big")
    assert bear.name == "Sir Bear"
    assert bear.arms == "short"
    assert bear.legs == "long"
    assert bear.body == 10
    assert bear.ears == "round"
    assert bear.e_n_m == "blue, black, big"


# unit testing
def test_foraging():
    bear_foraging = Bear("Sir Bear", "short", "long", 10, "round", "blue, black, big")
    random.seed(0)  # Set a seed for reproducible random choices
    food_found = bear_foraging.foraging()
    assert food_found in ["honey", "bugs", "berries", "worms", "tree bark", "a fart"]

# demo for Test Driven Development
# def test_foraging_tdd():
