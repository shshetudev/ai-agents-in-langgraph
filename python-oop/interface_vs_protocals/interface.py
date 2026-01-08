from abc import ABC, abstractmethod

class AIModel(ABC):

    @abstractmethod
    def predict(self, input_data):
        pass

    @abstractmethod
    def load_weights(self, path):
        pass

# This will fail as `load_weights` abstract method is not implemented
class MyModel(AIModel):
    def predict(self, input_data):
        return "Prediction"

