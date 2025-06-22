from __future__ import annotations
from abc import ABC, abstractmethod

class ClientDAO(ABC):

    @abstractmethod
    def add_client(self, client):
        pass

    @abstractmethod
    def update_client(self, client):
        pass

    @abstractmethod
    def get_client(self, dni):
        pass

    @abstractmethod
    def release(self, dni):
        pass

    @abstractmethod
    def deregister(self, dni):
        pass