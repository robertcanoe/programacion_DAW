from __future__ import annotations
from abc import ABC, abstractmethod

class TransactionDAO(ABC):

    @abstractmethod
    def create_movement(self, movement):
        pass