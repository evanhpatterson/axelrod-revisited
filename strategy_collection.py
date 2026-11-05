import numpy as np
from typing import List
from strategies.strategy import Strategy
from strategies.decision_payoffs import Decision, PrisonersDillemaPayoffs
import pandas as pd


def run_game(player1, player2, n_rounds):
    p1_history = []
    p2_history = []

    total_p1_payoff = 0
    total_p2_payoff = 0

    for _ in range(n_rounds):
        p1_decision = player1.make_decision(p1_history, p2_history)
        p2_decision = player2.make_decision(p2_history, p1_history)

        p1_history.append(p1_decision)
        p2_history.append(p2_decision)

        p1_payoff, p2_payoff = PrisonersDillemaPayoffs.get_payoffs(p1_decision, p2_decision)

        total_p1_payoff += p1_payoff
        total_p2_payoff += p2_payoff

    return total_p1_payoff, total_p2_payoff


class StrategyCollection:

    def __init__(self, strategies, n_rounds):
        self.strategies = list(set(strategies))
        n = len(self.strategies)

        self.payoffs = np.zeros((n, n))

        for i in range(n):
            for j in range(i, n):
                player1 = self.strategies[i]()
                player2 = self.strategies[j]()

                p1_payoff, p2_payoff = run_game(player1, player2, n_rounds)

                self.payoffs[i, j] = p1_payoff
                self.payoffs[j, i] = p2_payoff

    def show_payoffs(self):

        # convert the list of payoffs to a table, then display that table
        print(pd.DataFrame(
            {s().get_name(): self.payoffs[i] for i, s in enumerate(self.strategies)},
            index=[s().get_name() for i, s in enumerate(self.strategies)]
        ))
