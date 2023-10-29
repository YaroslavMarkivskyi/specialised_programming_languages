import math


class BaseCalculator:
    _LIST_OPERATORS = ('+', '-', '*', '/', '^', '√', '%')
    _custom_round = 3
    _num_1 = None
    _operator = None
    _num_2 = None
    _result = None

    def __init__(self, **kwargs):
        if 'num_1' in kwargs:
            self.num_1 = kwargs['num_1']
        if 'num_2' in kwargs:
            self.num_2 = kwargs['num_2']
        if 'operator' in kwargs:
            self.operator = kwargs['operator']
        if 'custom_round' in kwargs:
            self.custom_round = kwargs['custom_round']

    # Number Validate
    @classmethod
    def _number_validate(cls, num):
        try:
            num = float(num)
            return num
        except ValueError:
            raise ValueError(f"Parameter '{num}' is not number")

    # Operator Validate
    @classmethod
    def _operator_validate(cls, symbol):
        if symbol not in cls._LIST_OPERATORS:
            raise TypeError(f"Operator is not in {cls._LIST_OPERATORS}!")
        else:
            return symbol

    # Function Addition
    def _add(self):
        return self._num_1 + self._num_2

    # Function Subtraction
    def _sub(self):
        return self._num_1 - self._num_2

    # Function Multiplication
    def _mul(self):
        return self._num_1 * self._num_2

    # Function Division
    def _div(self):
        if self._num_2 != 0:
            return self._num_1 / self._num_2
        else:
            raise ZeroDivisionError("Division by zero")

    def _deg(self):
        return self._num_1 ** self._num_2

    def _rem(self):
        if self._num_2 != 0:
            return self._num_1 % self._num_2
        else:
            raise ZeroDivisionError("Division by zero")

    def _square(self):
        if self._num_1 >= 0:
            return math.sqrt(self._num_1)
        else:
            raise ArithmeticError("Negative number")

    # Function Calculation
    def calc(self):
        if self._operator == '+':
            self._result = round(self._add(), self._custom_round)
        elif self._operator == '-':
            self._result = round(self._sub(), self._custom_round)
        elif self._operator == '*':
            self._result = round(self._mul(), self._custom_round)
        elif self._operator == '/':
            self._result = round(self._div(), self._custom_round)
        elif self._operator == '^':
            self._result = round(self._deg(), self._custom_round)
        elif self._operator == '√':
            self._result = round(self._square(), self._custom_round)
        elif self._operator == '%':
            self._result = round(self._rem(), self._custom_round)

    # Function
    def __str__(self):
        self.calc()
        if self._operator == '√':
            return f"{self._operator} {self._num_1} = {self._result}"
        else:
            return f"{self._num_1} {self._operator} {self._num_2} = {self._result}"

    # Get num_1
    @property
    def num_1(self):
        return self._num_1

    # Set num_1
    @num_1.setter
    def num_1(self, value):
        self._num_1 = self._number_validate(value)

    # Get num_2
    @property
    def num_2(self):
        return self._num_2

    # Set num_2
    @num_2.setter
    def num_2(self, value):
        self._num_2 = self._number_validate(value)

    # Get operator
    @property
    def operator(self):
        return self._operator

    # Set operator
    @operator.setter
    def operator(self, symbol):
        self._operator = self._operator_validate(symbol)

    @property
    def custom_round(self):
        return self._custom_round

    @custom_round.setter
    def custom_round(self, value):
        self._custom_round = int(self._number_validate(value))
        