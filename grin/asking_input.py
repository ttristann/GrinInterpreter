# Module that handles the process of asking and reading
# inputs from the user. It handles the processes for
# asking and reading INSTR and INNUM


class Innum:

    def __init__(self, nt_innum):
        self._var = nt_innum.var
        self._value = None

    def _asking_for_input(self):
        """
        Prompts the user to give an input and checks
        whether the input is an int or float.
        If it is either one of the types, the input
        gets converted into the corresponding type
        and updates the self._value to the input.
        """
        value = input()

        def _isnum(num):
            if num.isdigit():
                return True
            elif num[0] == '-':
                return num[1:].isdigit()
            else:
                return False

        def _isfloat(num):
            try:
                float(num)
                return True
            except ValueError:
                return False

        if _isnum(value):
            self._value = int(value)
        elif _isfloat(value):
            self._value = float(value)
        else:
            self._value = None


    def storing_into_variables_dict(self, variables_dict):
        """
        Checks whether self._value is None, if so,
        it returns None. Otherwise, it returns True
        and updates the variables_dict.
        """
        self._asking_for_input()
        if self._value is None:
            return None
        else:
            variables_dict[self._var] = self._value
            return True


class Instr:

    def __init__(self, nt_instr):
        self._var = nt_instr.var
        self._value = None

    def _asking_for_input(self):
        """
        Prompts the user for an input and adds a
        set of "" in between to indicate the value
        as a string literal in the variables_dict.
        """
        value = input()
        self._value = f'"{value}"'

    def storing_into_variables_dict(self, variables_dict):
        """
        Updates the variables_dict to add the entry
        of the self._var and the corresponding
        self._value.
        """

        self._asking_for_input()
        variables_dict[self._var] = self._value

