from .strategy import Strategy
from .decision_payoffs import Decision


class Mean(Strategy):

    def __init__(self):
        super().__init__()
        pass

    def make_decision(self, self_history, other_history):
        return Decision.DEFECT
