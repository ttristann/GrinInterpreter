# Module that handles all the process involving adding
# subtracting, multiplying, and dividing values with
# another variables.

# The result of the arithmetic result becomes the new
# updated value associated with variable

import math

class Addition:

    def __init__(self, add_nt):
        self._var = add_nt.var
        self._value = add_nt.value

    def _getting_value(self, var_dict):
        """
        Iterates through the var dict to check if the
        value already an existing entry, if so, the value
        gets replaced with the entry value.

        If not, it checks whether if the value is a string
        or int literal to assign the value as it is.

        Lastly, if value is neither, the value is assigned 0
        """
        if type(self._value) is str:
            if self._value in var_dict:
                self._value = var_dict[self._value]
                if type(self._value) is str:
                    if '"' in self._value:
                        self._value = self._value[1:-1]
            elif '"' in self._value:
                self._value = self._value[1:-1]
            else:
                self._value = 0

    def adding_process(self, var_dict):
        """
        Adds the entry value associated with the variable
        with the newly assigned self._value from the
        _getting_value method.

        If there's an error while adding, the method returns
        False. Otherwise, it updates the dictionary with
        the result of the addition and returns True.
        """
        self._getting_value(var_dict)
        try:
            if type(var_dict[self._var]) is str:
                var_dict[self._var] = f'"{var_dict[self._var][1:-1] + self._value}"'
                return True
            elif type(var_dict[self._var]) in [int, float]:
                var_dict[self._var] = var_dict[self._var] + self._value
                return True
        except:
            return None

class Subtraction(Addition):

    def __init__(self, sub_nt):
        self._var = sub_nt.var
        self._value = sub_nt.value

    def subtracting_process(self, var_dict):
        """
        Calls the getting_data method from the base class
        to assign the self._value properly.

        With self._value established, it is subtracted
        from the value associated with variable within
        the var_dict.

        If any errors occur, it returns False, otherwise,
        it returns True.
        """
        super()._getting_value(var_dict)
        try:
            if type(var_dict[self._var]) is str:
                var_dict[self._var] = f'"{var_dict[self._var][1:-1] - self._value}"'
                return True
            elif type(var_dict[self._var]) in [int, float]:
                var_dict[self._var] = var_dict[self._var] - self._value
                return True
        except:
            return None

class Multiplication(Addition):

    def __init__(self, mult_nt):
        self._var = mult_nt.var
        self._value = mult_nt.value

    def multiplying_process(self, var_dict):
        """
        Calls the _getting_value method from the
        base class to properly format the value.

        Once that value is established, it
        multiplies the two values and updates the
        dictionary entry to reflect the multiplication.
        """
        super()._getting_value(var_dict)
        try:
            if type(var_dict[self._var]) is str:
                var_dict[self._var] = f'"{var_dict[self._var][1:-1] * self._value}"'
                return True
            elif type(var_dict[self._var]) in [int, float]:
                var_dict[self._var] = var_dict[self._var] * self._value
                if type(var_dict[self._var]) is str:
                    var_dict[self._var] = f'"{var_dict[self._var]}"'
                return True
        except:
            return None


class Division(Addition):

    def __init__(self, div_nt):
        self._var = div_nt.var
        self._value = div_nt.value

    def dividing_process(self, var_dict):
        """
        Calls the _getting_value method from the
        base class to get the value in the proper value.

        Once that is established, it divides it accordingly
        and updates the dictionary to reflect the
        division process.
        """
        super()._getting_value(var_dict)
        try:
            if type(var_dict[self._var]) is str:
                var_dict[self._var] = f'"{var_dict[self._var][1:-1] / self._value}"'
                return True
            elif type(var_dict[self._var]) in [int, float]:
                if type(var_dict[self._var]) is int and type(self._value) is int:
                    var_dict[self._var] = math.floor(var_dict[self._var] / self._value)
                else: var_dict[self._var] = var_dict[self._var] / self._value
                return True
        except:
            return None
