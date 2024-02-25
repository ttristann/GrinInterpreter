# Module that handles the process of altering the flow
# of the grin program by jumping into certain lines of
# the program.

class GOTO:

    def __init__(self, goto_nt):
        self._target = goto_nt.target

    def jumping_process(self, current_index, max_index, labels_dict, variables_dict):
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
            else: new_index = labels_dict[self._target]
            return new_index
        else:
            new_index = current_index + self._target
            if new_index <= 0:
                return None
            elif new_index >= max_index:
                return None
            elif type(new_index) is not int:
                return None
            else: return new_index

class CONT_GOTO(GOTO):

    def __init__(self, c_goto_nt):
        self._target = c_goto_nt.target
        self._val1 = c_goto_nt.val1
        self._op = c_goto_nt.op
        self._val2 = c_goto_nt.val2

    def figuring_out_values(self, variables_dict):
        """
        Updates self._val1 and/or self._val2 by checking
        if either the values are entries in the variables_dict
        and updates it to the value associated in the dictionary.
        """
        if type(self._val1) is str:
            if self._val1 in variables_dict:
                self._val1 = variables_dict[self._val1]
        if type(self._val2) is str:
            if self._val2 in variables_dict:
                self._val2 = variables_dict[self._val2]

    def determining_conditionally(self):
        """
        Executes various equality statements based on the
        attributes updated in the object's attributes.

        Returns the result of the statements.
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






