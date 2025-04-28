class TestClass:
    """test class for sphinx documentation.
    """
    def __init__(self) -> None:
        """__init__"""
        self.name = None
        self.value = None

    def set_attribute(self, name: str, value: float):
        """set_attribute
        Set the name and value attributes of the class.

        Args:
            name (str): name of the attribute
            value (float): value of the attribute
        """
        self.name = name
        self.value = value
