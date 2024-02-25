import unittest
import grin.goto_process as g_goto
import grin.variables as g_var
import grin.reading_input as g_input

class TestGotoProcess(unittest.TestCase):

    def test_goto_with_positive_jump(self):
        var_dict = {}
        labels_dict = {}
        collection = [g_input.LET('A', 1), g_input.GOTO(2), g_input.LET('A', 2), g_input.LET('B', 2)]
        current_index = 0
        max_index = len(collection)
        while current_index != max_index:
            ind_nt = collection[current_index]
            if type(ind_nt) is g_input.LET:
                var_class = g_var.Variables(ind_nt)
                var_class.assigning_variables(var_dict)
                current_index += 1
            if type(ind_nt) is g_input.GOTO:
                goto_class = g_goto.GOTO(ind_nt)
                goto_result = goto_class.jumping_process(current_index, max_index, labels_dict, var_dict)
                current_index = goto_result
        self.assertEqual(var_dict, {'A': 1, 'B': 2})

    def test_goto_with_negative_jump(self):
        var_dict = {}
        labels_dict = {}
        collection = [g_input.LET('A', 1), g_input.LET('A', 2), g_input.END(0), g_input.GOTO(-2), g_input.LET('A', 4)]
        current_index = 0
        max_index = len(collection)
        while current_index != max_index:
            ind_nt = collection[current_index]
            if type(ind_nt) is g_input.LET:
                var_class = g_var.Variables(ind_nt)
                var_class.assigning_variables(var_dict)
                current_index += 1
            if type(ind_nt) is g_input.GOTO:
                goto_class = g_goto.GOTO(ind_nt)
                goto_result = goto_class.jumping_process(current_index, max_index, labels_dict, var_dict)
                current_index = goto_result
            if type(ind_nt) is g_input.END:
                break
        self.assertEqual(var_dict, {'A': 2})

    def test_goto_positive_jump_invalid(self):
        var_dict = {}
        labels_dict = {}
        collection = [g_input.LET('A', 1), g_input.GOTO(3), g_input.LET('A', 2), g_input.LET('B', 2)]
        current_index = 0
        max_index = len(collection)
        while current_index != max_index:
            ind_nt = collection[current_index]
            if type(ind_nt) is g_input.LET:
                var_class = g_var.Variables(ind_nt)
                var_class.assigning_variables(var_dict)
                current_index += 1
            if type(ind_nt) is g_input.GOTO:
                goto_class = g_goto.GOTO(ind_nt)
                goto_result = goto_class.jumping_process(current_index, max_index, labels_dict, var_dict)
                if goto_result is None:
                    break
                else: current_index = goto_result
        self.assertEqual(goto_result, None)

    def test_goto_negative_jump_invalid(self):
        var_dict = {}
        labels_dict = {}
        collection = [g_input.LET('A', 1), g_input.LET('A', 2), g_input.GOTO(-4), g_input.LET('A', 4)]
        current_index = 0
        max_index = len(collection)
        while current_index != max_index:
            ind_nt = collection[current_index]
            if type(ind_nt) is g_input.LET:
                var_class = g_var.Variables(ind_nt)
                var_class.assigning_variables(var_dict)
                current_index += 1
            if type(ind_nt) is g_input.GOTO:
                goto_class = g_goto.GOTO(ind_nt)
                goto_result = goto_class.jumping_process(current_index, max_index, labels_dict, var_dict)
                if goto_result is None:
                    break
                else: current_index = goto_result

        self.assertEqual(goto_result, None)

    def test_goto_process_jump_with_variable(self):
        var_dict = {}
        labels_dict = {}
        collection = [g_input.LET('A', 1), g_input.LET('B', -2), g_input.END(0), g_input.GOTO('B'),
                      g_input.LET('A', 4)]
        current_index = 0
        max_index = len(collection)
        while current_index != max_index:
            ind_nt = collection[current_index]
            if type(ind_nt) is g_input.LET:
                var_class = g_var.Variables(ind_nt)
                var_class.assigning_variables(var_dict)
                current_index += 1
            if type(ind_nt) is g_input.GOTO:
                goto_class = g_goto.GOTO(ind_nt)
                goto_result = goto_class.jumping_process(current_index, max_index, labels_dict,
                                                         var_dict)
                current_index = goto_result
            if type(ind_nt) is g_input.END:
                break
        self.assertEqual(var_dict, {'A': 1, 'B': -2})

    def test_goto_process_jump_with_label(self):
        var_dict = {}
        labels_dict = {'FINAL': 1}
        collection = [g_input.LET('A', 1), g_input.LET('A', 2), g_input.END(0), g_input.GOTO('FINAL'),
                      g_input.LET('A', 4)]
        current_index = 0
        max_index = len(collection)
        while current_index != max_index:
            ind_nt = collection[current_index]
            if type(ind_nt) is g_input.LET:
                var_class = g_var.Variables(ind_nt)
                var_class.assigning_variables(var_dict)
                current_index += 1
            if type(ind_nt) is g_input.GOTO:
                goto_class = g_goto.GOTO(ind_nt)
                goto_result = goto_class.jumping_process(current_index, max_index, labels_dict,
                                                         var_dict)
                current_index = goto_result
            if type(ind_nt) is g_input.END:
                break
        self.assertEqual(var_dict, {'A': 2})

    def test_c_goto_determining_conditionality_with_lt(self):
        var_dict = {'A': 2.5}
        c_goto_nt = g_input.C_GOTO(2, 1, '<', 'A')
        c_goto_class = g_goto.CONT_GOTO(c_goto_nt)
        c_goto_class.figuring_out_values(var_dict)
        result = c_goto_class.determining_conditionally()

        self.assertEqual(result, True)

    def test_c_goto_determining_conditionality_with_le(self):
        var_dict = {'A': 2.5}
        c_goto_nt = g_input.C_GOTO(2, 1, '<=', 'A')
        c_goto_class = g_goto.CONT_GOTO(c_goto_nt)
        c_goto_class.figuring_out_values(var_dict)
        result = c_goto_class.determining_conditionally()

        self.assertEqual(result, True)

    def test_c_goto_determining_conditionality_with_gt(self):
        var_dict = {'A': 2.5}
        c_goto_nt = g_input.C_GOTO(2, 'A', '>', 1)
        c_goto_class = g_goto.CONT_GOTO(c_goto_nt)
        c_goto_class.figuring_out_values(var_dict)
        result = c_goto_class.determining_conditionally()

        self.assertEqual(result, True)

    def test_c_goto_determining_conditionality_with_ge(self):
        var_dict = {'A': 2.5}
        c_goto_nt = g_input.C_GOTO(2, 'A', '>=', 2.4)
        c_goto_class = g_goto.CONT_GOTO(c_goto_nt)
        c_goto_class.figuring_out_values(var_dict)
        result = c_goto_class.determining_conditionally()

        self.assertEqual(result, True)

    def test_c_goto_determining_conditionality_with_eq(self):
        var_dict = {'A': 2.5}
        c_goto_nt = g_input.C_GOTO(2, 2.5, '=', 'A')
        c_goto_class = g_goto.CONT_GOTO(c_goto_nt)
        c_goto_class.figuring_out_values(var_dict)
        result = c_goto_class.determining_conditionally()

        self.assertEqual(result, True)

    def test_c_goto_determining_conditionality_with_ne(self):
        var_dict = {'A': 2.5}
        c_goto_nt = g_input.C_GOTO(2, 1, '<>', 'A')
        c_goto_class = g_goto.CONT_GOTO(c_goto_nt)
        c_goto_class.figuring_out_values(var_dict)
        result = c_goto_class.determining_conditionally()

        self.assertEqual(result, True)
