__all__ = ["InvalidMarker", "UndefinedComparison", "UndefinedEnvironmentName", "Marker", "default_environment"]

class InvalidMarker(ValueError): ...
class UndefinedComparison(ValueError): ...
class UndefinedEnvironmentName(ValueError): ...

def default_environment() -> dict[str, str]: ...

class Marker:
    def __init__(self, marker: str) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def evaluate(self, environment: dict[str, str] | None = None) -> bool: ...
