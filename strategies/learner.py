from .strategy import Strategy
from .decision_payoffs import Decision
import torch
import torch.nn as nn
import torch.nn.functional as F


class DecisionModel(nn.Module):

    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(4, 32)
        self.layer2 = nn.Linear(32, 2)

    def forward(self, x):
        x = F.leaky_relu(self.layer1(x))
        return self.layer2(x)


class Learner(Strategy):

    def __init__(self):
        super().__init__()
        self.model = DecisionModel()

    @staticmethod
    def vectorize_decision(decision):
        if decision == Decision.COOPERATE:
            return [1, 0]
        elif decision == Decision.DEFECT:
            return [0, 1]
        else:
            return [0, 0]

    @staticmethod
    def get_model_inputs(self_history, other_history):
        assert len(self_history) == len(other_history)
        n = len(self_history)
        inputs = torch.zeros((n-1, 4))
        outputs = torch.zeros((n-1, 2))

        for i in range(n - 1):
            self_inp = Learner.vectorize_decision(self_history[i])
            other_inp = Learner.vectorize_decision(other_history[i])
            x = self_inp + other_inp
            inputs[i] = torch.tensor(x)

            y = torch.tensor(Learner.vectorize_decision(other_history[i+1]))
            outputs[i] = y

        return inputs, outputs

    def make_decision(self, self_history, other_history):
        inputs, outputs = Learner.get_model_inputs(self_history, other_history)
        self.model.fit(inputs, outputs)
        self_prev = Learner.vectorize_decision(self_history[-1])
        other_prev = Learner.vectorize_decision(other_history[-1])
        x = torch.tensor(self_prev + other_prev)
        prediction = self.model(x)

        prob_other_cooperate = prediction[0]
        prob_other_defect = prediction[1]
