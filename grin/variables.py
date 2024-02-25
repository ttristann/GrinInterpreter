# Module that handles the process of assigning variables
# and their associated values based on the inputted grin line.

# Module is also able to handle the process of printing
# variables whether if the variable does or does not exist
# in the universal dictionary.



class Variables:
    def __init__(self, nt_let):
        self._var = nt_let.var
        self._value = nt_let.value

    def assigning_variables(self, variables_dict):
        """
        Updates the universal variables_dict that is created
        once the program is starts and compiles all
        the information that deal with assigning variables.

        Returns the updated variables_dict.
        """
        if self._value in variables_dict:
            variables_dict[self._var] = variables_dict[self._value]
        else:
            variables_dict[self._var] = self._value

class Print:

    def __init__(self, nt_print):
        self._value = nt_print.value

    def printing_variables(self, variables_dict):
        """
        Checks the value is an existing variable
        and manipulates the value to print the
        value in accordance to its format as int
        or string literal.
        """
        if self._value not in variables_dict:
            if type(self._value) is int:
                print(self._value)
            elif '"' in self._value:
                print(self._value[1:-1])
            else:
                print(0)
        else:
            value_to_print = variables_dict[self._value]
            if type(value_to_print) is str:
                if '"' in value_to_print:
                    value_to_print = value_to_print[1:-1]

            print(value_to_print)

