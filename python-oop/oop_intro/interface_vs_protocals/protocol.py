from typing import Protocol, runtime_checkable

# Protocol: Blueprint
@runtime_checkable
class AIModel(Protocol):
    def predict(self, input_data: list) -> str:
        ...

    def load_weights(self, path: str) -> None:
        ...


# Implementing a compliant class -> No inheritance is needed like MyCorrectModel(AIModel)
class MyCorrectModel:
    def predict(self, input_data: list) -> str:
        return f"Result for {input_data}"

    def load_weights(self, path: str) -> None:
        print(f"Weights loaded from {path}")

# Missing load weights! Will flag `Protocol compatibility` error
class MyIncorrectModel:
    def predict(self, input_data: list) -> str:
        return f"Result for {input_data}"