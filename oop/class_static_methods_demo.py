class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static Method: Does not need access to class or instance attributes
    @staticmethod
    def add(a, b):
        return a + b

    # Class Method: Accesses class-level attributes
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
