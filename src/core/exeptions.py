class BrandNotFound(Exception):
    def __init__(self, message: str | None = None) -> None:
        self.message = message


class ModelNotFound(Exception):
    def __init__(self, message: str | None = None) -> None:
        self.message = message
        
        
class CarNotFound(Exception):
    def __init__(self, message: str | None = None) -> None:
        self.message = message
            