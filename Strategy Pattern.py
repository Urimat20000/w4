from abc import ABC, abstractmethod

class LockStrategy(ABC):
    @abstractmethod
    def lock(self):
        pass

class TraditionalLock(LockStrategy):
    def lock(self):
        return "Замок закрыт традиционным ключом"

class ElectronicLock(LockStrategy):
    def lock(self):
        return "Замок закрыт электронным ключом"

class OpenStrategy(ABC):
    @abstractmethod
    def open(self):
        pass

class ManualOpen(OpenStrategy):
    def open(self):
        return "Дверь открыта вручную"

class AutomaticOpen(OpenStrategy):
    def open(self):
        return "Дверь открыта автоматически"

class Door:
    def __init__(self, lock_strategy: LockStrategy, open_strategy: OpenStrategy):
        self.lock_strategy = lock_strategy
        self.open_strategy = open_strategy

    def lock(self):
        print(self.lock_strategy.lock())

    def open(self):
        print(self.open_strategy.open())

door = Door(TraditionalLock(), ManualOpen())
door.lock()
door.open()

door1 = Door(ElectronicLock(), AutomaticOpen())
door1.lock()
door1.open()