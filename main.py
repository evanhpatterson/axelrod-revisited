import numpy as np
from strategies import *
from strategy_collection import StrategyCollection


s = [TitForTat, EternalAnger, Mean]

n_rounds = 10
print(f"Number of Rounds: {n_rounds}")

sc = StrategyCollection(s, n_rounds=n_rounds)

sc.show_payoffs()
