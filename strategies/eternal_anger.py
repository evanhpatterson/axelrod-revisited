from .strategy import Strategy
from .decision_payoffs import Decision


class EternalAnger(Strategy):

    def __init__(self):
        super().__init__()
        pass

    def make_decision(self, self_history, other_history):
        if len(other_history) > 0:
            if Decision.DEFECT in other_history:
                return Decision.DEFECT
            else:
                return Decision.COOPERATE
        else:
            return Decision.COOPERATE
