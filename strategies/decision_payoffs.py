from enum import Enum
import numpy as np


class Decision(Enum):
    COOPERATE = 0
    DEFECT = 1


class PrisonersDillemaPayoffs:

    prisoners_dillema_p1_payoffs = np.array([
        [3, 0],
        [5, 1]
    ])

    prisoners_dillema_p2_payoffs = prisoners_dillema_p1_payoffs.T.copy()

    @staticmethod
    def from_decision(decision):
        # get the index of the matrix for this decision
        if decision == Decision.COOPERATE:
            return 0 # index 0 in the matrix
        elif decision == Decision.DEFECT:
            return 1 # index 1 in the matrix
        else:
            raise Exception("decision is not valid")

    @staticmethod
    def get_payoffs(p1_decision, p2_decision):

        # retrieve the index for each decision
        d1 = PrisonersDillemaPayoffs.from_decision(p1_decision)
        d2 = PrisonersDillemaPayoffs.from_decision(p2_decision)

        # return the payoffs from the payoff matrix
        return (
            PrisonersDillemaPayoffs.prisoners_dillema_p1_payoffs[d1, d2],
            PrisonersDillemaPayoffs.prisoners_dillema_p2_payoffs[d1, d2])
