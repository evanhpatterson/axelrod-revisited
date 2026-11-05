from .strategy import Strategy
from .decision_payoffs import Decision


class TitForTat(Strategy):

    def __init__(self):
        super().__init__()
        pass

    def make_decision(self, self_history, other_history):
        if len(other_history) > 0:
            if other_history[-1] == Decision.DEFECT:
                return Decision.DEFECT
            else:
                return Decision.COOPERATE
        else:
            return Decision.COOPERATE
