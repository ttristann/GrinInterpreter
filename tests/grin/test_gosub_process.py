import unittest
import grin.variables as g_var
import grin.reading_input as g_input
import grin.gosub_process as g_gosub

class TestGoSubProcess(unittest.TestCase):

    def test_gosub_process_with_positive_int(self):
        var_dict = {}
        labels_dict = {}
        collection = [g_input.LET('A', 1), g_input.GOSUB(3), g_input.LET('A', 2), g_input.END(0)
                      ,g_input.LET('B', 2), g_input.RETURN(0)]
        current_return_index = 0
        current_index = 0
        max_index = len(collection)
        while current_index != max_index:
            ind_nt = collection[current_index]
            if type(ind_nt) is g_input.LET:
                var_class = g_var.Variables(ind_nt)
                var_class.assigning_variables(var_dict)
                current_index += 1
            if type(ind_nt) is g_input.GOSUB:
                gosub_class = g_gosub.GOSUB(ind_nt)
                gosub_result = gosub_class.gosub_jumping_process(current_index, max_index, labels_dict,
                                                         var_dict)
                current_return_index = current_index + 1
                current_index = gosub_result
            if type(ind_nt) is g_input.RETURN:
                current_index = current_return_index
            if type(ind_nt) is g_input.END:
                break
        self.assertEqual(var_dict, {'A': 2, 'B': 2})

    def test_gosub_process_with_label(self):
        var_dict = {}
        labels_dict = {'FIRST': 4}
        collection = [g_input.LET('A', 1), g_input.GOSUB('FIRST'), g_input.LET('A', 2), g_input.END(0)
            , g_input.LET('B', 2), g_input.RETURN(0)]
        current_return_index = 0
        current_index = 0
        max_index = len(collection)
        while current_index != max_index:
            ind_nt = collection[current_index]
            if type(ind_nt) is g_input.LET:
                var_class = g_var.Variables(ind_nt)
                var_class.assigning_variables(var_dict)
                current_index += 1
            if type(ind_nt) is g_input.GOSUB:
                gosub_class = g_gosub.GOSUB(ind_nt)
                gosub_result = gosub_class.gosub_jumping_process(current_index, max_index,
                                                                 labels_dict,
                                                                 var_dict)
                current_return_index = current_index + 1
                current_index = gosub_result
            if type(ind_nt) is g_input.RETURN:
                current_index = current_return_index
            if type(ind_nt) is g_input.END:
                break
        self.assertEqual(var_dict, {'A': 2, 'B': 2})

    def test_c_gosub_figuring_out_values_with_one_var_and_one_literal(self):
        var_dict = {'A': 2}
        c_gosub_nt = g_input.C_GOSUB(2, 'A', '>', 1)
        c_gosub_class = g_gosub.CONT_GOSUB(c_gosub_nt)
        c_gosub_class.c_gosub_figuring_out_values(var_dict)

        self.assertEqual(c_gosub_class._val1, 2)

    def test_c_gosub_figuring_out_values_with_both_var(self):
        var_dict = {'A': 2, 'B': 1}
        c_gosub_nt = g_input.C_GOSUB(2, 'A', '>', 'B')
        c_gosub_class = g_gosub.CONT_GOSUB(c_gosub_nt)
        c_gosub_class.c_gosub_figuring_out_values(var_dict)

        self.assertEqual((c_gosub_class._val1, c_gosub_class._val2), (2,1))

    def test_c_gosub_figuring_out_values_with_float_and_var(self):
        var_dict = {'A': 2.5}
        c_gosub_nt = g_input.C_GOSUB(2, 1, '<', 'A')
        c_gosub_class = g_gosub.CONT_GOSUB(c_gosub_nt)
        c_gosub_class.c_gosub_figuring_out_values(var_dict)

        self.assertEqual(c_gosub_class._val2, 2.5)

    def test_c_gosub_determining_conditionality_with_lt(self):
        var_dict = {'A': 2.5}
        c_gosub_nt = g_input.C_GOSUB(2, 1, '<', 'A')
        c_gosub_class = g_gosub.CONT_GOSUB(c_gosub_nt)
        c_gosub_class.c_gosub_figuring_out_values(var_dict)
        result = c_gosub_class.c_gosub_determining_conditionally()

        self.assertEqual(result, True)

    def test_c_gosub_determining_conditionality_with_le(self):
        var_dict = {'A': 1}
        c_gosub_nt = g_input.C_GOSUB(2, 1, '<=', 'A')
        c_gosub_class = g_gosub.CONT_GOSUB(c_gosub_nt)
        c_gosub_class.c_gosub_figuring_out_values(var_dict)
        result = c_gosub_class.c_gosub_determining_conditionally()

        self.assertEqual(result, True)

    def test_c_gosub_determining_conditionality_with_gt(self):
        var_dict = {'A': 2.5}
        c_gosub_nt = g_input.C_GOSUB(2, 'A', '>', 2)
        c_gosub_class = g_gosub.CONT_GOSUB(c_gosub_nt)
        c_gosub_class.c_gosub_figuring_out_values(var_dict)
        result = c_gosub_class.c_gosub_determining_conditionally()

        self.assertEqual(result, True)

    def test_c_gosub_determining_conditionality_with_ge(self):
        var_dict = {'A': 2.5}
        c_gosub_nt = g_input.C_GOSUB(2, 'A', '>=', 2.5)
        c_gosub_class = g_gosub.CONT_GOSUB(c_gosub_nt)
        c_gosub_class.c_gosub_figuring_out_values(var_dict)
        result = c_gosub_class.c_gosub_determining_conditionally()

        self.assertEqual(result, True)

    def test_c_gosub_determining_conditionality_with_eq(self):
        var_dict = {'A': 2.5}
        c_gosub_nt = g_input.C_GOSUB(2, 2.5, '=', 'A')
        c_gosub_class = g_gosub.CONT_GOSUB(c_gosub_nt)
        c_gosub_class.c_gosub_figuring_out_values(var_dict)
        result = c_gosub_class.c_gosub_determining_conditionally()

        self.assertEqual(result, True)

    def test_c_gosub_determining_conditionality_with_ne(self):
        var_dict = {'A': 2.5}
        c_gosub_nt = g_input.C_GOSUB(2, 1, '<>', 'A')
        c_gosub_class = g_gosub.CONT_GOSUB(c_gosub_nt)
        c_gosub_class.c_gosub_figuring_out_values(var_dict)
        result = c_gosub_class.c_gosub_determining_conditionally()

        self.assertEqual(result, True)
