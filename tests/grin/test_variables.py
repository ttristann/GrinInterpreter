import unittest
from collections import namedtuple
import grin.variables as g_var
import contextlib
import io

class TestVariables(unittest.TestCase):

    def test_let_with_one_value(self):
        LET = namedtuple('LET', "var value")
        let_nt1 = LET('A', 2)
        var_dict = {}
        let_class = g_var.Variables(let_nt1)
        let_class.assigning_variables(var_dict)

        self.assertEqual(var_dict, {'A': 2})

    def test_let_with_multiple_values(self):
        LET = namedtuple('LET', "var value")
        var_dict = {}
        nt_collection = [LET('A', 2), LET('B', 3), LET('C', 4)]
        for nt in nt_collection:
            let_class = g_var.Variables(nt)
            let_class.assigning_variables(var_dict)

        self.assertEqual(var_dict, {'A': 2, 'B': 3, 'C': 4})

    def test_let_with_updated_values(self):
        LET = namedtuple('LET', "var value")
        var_dict = {}
        nt_collection = [LET('A', 2), LET('B', 3), LET('A', 4)]
        for nt in nt_collection:
            let_class = g_var.Variables(nt)
            let_class.assigning_variables(var_dict)

        self.assertEqual(var_dict, {'A': 4, 'B': 3})


    def test_let_with_assigning_a_var_with_another(self):
        LET = namedtuple('LET', "var value")
        var_dict = {}
        nt_collection = [LET('A', '"A"'), LET('B', 'A')]
        for nt in nt_collection:
            let_class = g_var.Variables(nt)
            let_class.assigning_variables(var_dict)

        self.assertEqual(var_dict, {'A': '"A"', 'B': '"A"'})

    def test_let_with_various_kinds_of_variables(self):
        LET = namedtuple('LET', "var value")
        var_dict = {}
        nt_collection = [LET('A', '"A"'), LET('B', 2), LET('C', 'A'), LET('B', 4)]
        for nt in nt_collection:
            let_class = g_var.Variables(nt)
            let_class.assigning_variables(var_dict)

        self.assertEqual(var_dict, {'A': '"A"', 'B': 4, 'C': '"A"'})

    def test_print_with_literal_string(self):
        PRINT = namedtuple('PRINT',"value")
        var_dict = {}
        print_nt = PRINT('"A"')
        print_class = g_var.Print(print_nt)
        with contextlib.redirect_stdout(io.StringIO()) as print_result:
            print_class.printing_variables(var_dict)

        self.assertEqual(print_result.getvalue(), 'A\n')

    def test_print_with_integer(self):
        PRINT = namedtuple('PRINT',"value")
        var_dict = {}
        print_nt = PRINT(2)
        print_class = g_var.Print(print_nt)
        with contextlib.redirect_stdout(io.StringIO()) as print_result:
            print_class.printing_variables(var_dict)

        self.assertEqual(print_result.getvalue(), '2\n')


    def test_print_with_non_existing_variable(self):
        PRINT = namedtuple('PRINT',"value")
        var_dict = {}
        print_nt = PRINT('A')
        print_class = g_var.Print(print_nt)
        with contextlib.redirect_stdout(io.StringIO()) as print_result:
            print_class.printing_variables(var_dict)

        self.assertEqual(print_result.getvalue(), '0\n')

    def test_print_with_existing_variable(self):
        PRINT = namedtuple('PRINT',"value")
        var_dict = {'A': '"A"'}
        print_nt = PRINT('A')
        print_class = g_var.Print(print_nt)
        with contextlib.redirect_stdout(io.StringIO()) as print_result:
            print_class.printing_variables(var_dict)

        self.assertEqual(print_result.getvalue(), 'A\n')

