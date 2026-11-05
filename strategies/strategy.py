from abc import ABC, abstractmethod
from .decision_payoffs import Decision


class Strategy(ABC):

    def __init__(self):
        pass

    def __hash__(self):
        return hash(self.__class__.__name__)

    def get_name(self):
        return self.__class__.__name__

    @abstractmethod
    def make_decision(self, self_history, other_history) -> Decision:
        pass
