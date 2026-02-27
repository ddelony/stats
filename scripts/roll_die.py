#!/usr/bin/env python
# Program to simulate roll of a fair six-sided die
import numpy as np

rng = np.random.default_rng()

def roll(die):
    return rng.choice(die)

die = np.arange(1,7) # Create a six-sided die

result = roll(die)
print(result)
