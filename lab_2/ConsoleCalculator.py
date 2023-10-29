from BaseCalculator import BaseCalculator


class ConsoleCalculator(BaseCalculator):

    def _set_parameters(self):
        num_1 = input("Input num_1: ")
        self.num_1 = num_1
        operator = input("Input operator ('+', '-', '*', '/', '^', '√', '%'): ")
        self._operator = self._operator_validate(operator)
        if operator != '√':
            num_2 = input("Input num_2: ")
            self.num_2 = num_2

        custom_round = input("Input round: ")
        self.custom_round = custom_round

    def run(self):
        while input("input 'f' if you want to exit: ") != 'f':
            try:
                self._set_parameters()
                self.calc()
                print(self)
            except ArithmeticError as e:
                print(f"Error: {e}")
            except ValueError as e:
                print(f"Error: {e}")
            except TypeError as e:
                print(f"Error: {e}")
