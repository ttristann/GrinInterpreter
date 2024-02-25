# Module that handles the process of jumping to either a label
# or an integer that represents a new index to jump to.

class GOSUB:

    def __init__(self, gosub_nt):
        self._target = gosub_nt.target

    def gosub_jumping_process(self, current_index, max_index, labels_dict, variables_dict):
        """
        Updates the current index by adding the target
        to it.

        If the new current index is less than 0 or
        greater than the max_index given in the function
        call, it returns None.

        Otherwise, it returns the new current_index.
        """
        if type(self._target) is str:
            if self._target in variables_dict:
                if type(variables_dict[self._target]) is str:
                    self._target = variables_dict[self._target][1:-1]
                    new_index = labels_dict[self._target]
                elif type(variables_dict[self._target]) is int:
                    new_index = current_index + variables_dict[self._target]
            else:
                new_index = labels_dict[self._target]
            return new_index
        else:
            new_index = current_index + self._target
            if new_index <= 0:
                return None
            elif new_index >= max_index:
                return None
            elif type(new_index) is not int:
                return None
            else:
                return new_index


class CONT_GOSUB(GOSUB):

    def __init__(self, c_gosub_nt):
        self._target = c_gosub_nt.target
        self._val1 = c_gosub_nt.val1
        self._op = c_gosub_nt.op
        self._val2 = c_gosub_nt.val2

    def c_gosub_figuring_out_values(self, variables_dict):
        """
        Checks if either values is a variable that has a label
        or int value associated to it, if so, the value becomes
        the new value.

        If not, the value remains unchanged.
        """
        if type(self._val1) is str:
            if self._val1 in variables_dict:
                self._val1 = variables_dict[self._val1]
        if type(self._val2) is str:
            if self._val2 in variables_dict:
                self._val2 = variables_dict[self._val2]

    def c_gosub_determining_conditionally(self):
        """
        Executes various conditional statements depending on
        the type of operation given in the grin command line.

        It returns the boolean result of the conditional
        equality statement.
        """
        if self._op == '<':
            return self._val1 < self._val2
        elif self._op == '<=':
            return self._val1 <= self._val2
        elif self._op == '>':
            return self._val1 > self._val2
        elif self._op == '>=':
            return self._val1 >= self._val2
        elif self._op == '=':
            return self._val1 == self._val2
        elif self._op == '<>':
            return self._val1 != self._val2