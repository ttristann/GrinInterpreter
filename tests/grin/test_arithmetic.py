import unittest
from collections import namedtuple
import grin.arithmetic as g_arith

class TestArithmetic(unittest.TestCase):

    def test_add_with_both_int(self):
        ADD = namedtuple('ADD', 'var value')
        add_nt = ADD('A', 1)
        var_dict = {'A': 1}
        add_class = g_arith.Addition(add_nt)
        add_class.adding_process(var_dict)

        self.assertEqual(var_dict, {'A': 2})

    def test_add_with_both_float(self):
        ADD = namedtuple('ADD', 'var value')
        add_nt = ADD('A', 1.5)
        var_dict = {'A': 1.5}
        add_class = g_arith.Addition(add_nt)
        add_class.adding_process(var_dict)

        self.assertEqual(var_dict, {'A': 3.0})

    def test_add_with_int_and_float(self):
        ADD = namedtuple('ADD', 'var value')
        add_nt = ADD('A', 1)
        var_dict = {'A': 1.5}
        add_class = g_arith.Addition(add_nt)
        add_class.adding_process(var_dict)

        self.assertEqual(var_dict, {'A': 2.5})

    def test_add_with_float_and_int(self):
        ADD = namedtuple('ADD', 'var value')
        add_nt = ADD('A', 1.5)
        var_dict = {'A': 1}
        add_class = g_arith.Addition(add_nt)
        add_class.adding_process(var_dict)

        self.assertEqual(var_dict, {'A': 2.5})

    def test_add_with_both_string(self):
        ADD = namedtuple('ADD', 'var value')
        add_nt = ADD('A', '"WORLD"')
        var_dict = {'A': '"HELLO"'}
        add_class = g_arith.Addition(add_nt)
        add_class.adding_process(var_dict)

        self.assertEqual(var_dict, {'A': '"HELLOWORLD"'})

    def test_add_with_string_and_int(self):
        ADD = namedtuple('ADD', 'var value')
        add_nt = ADD('A', '"WORLD"')
        var_dict = {'A': 1}
        add_class = g_arith.Addition(add_nt)
        result = add_class.adding_process(var_dict)

        self.assertEqual(result, None)

    def test_sub_with_both_int(self):
        SUB = namedtuple('SUB', 'var value')
        sub_nt = SUB('A', 2)
        var_dict = {'A': 4}
        sub_class = g_arith.Subtraction(sub_nt)
        sub_class.subtracting_process(var_dict)

        self.assertEqual(var_dict, {'A': 2})

    def test_sub_with_both_floats(self):
        SUB = namedtuple('SUB', 'var value')
        sub_nt = SUB('A', 2.0)
        var_dict = {'A': 4.0}
        sub_class = g_arith.Subtraction(sub_nt)
        sub_class.subtracting_process(var_dict)

        self.assertEqual(var_dict, {'A': 2.0})

    def test_sub_with_float_and_int(self):
        SUB = namedtuple('SUB', 'var value')
        sub_nt = SUB('A', 2)
        var_dict = {'A': 4.0}
        sub_class = g_arith.Subtraction(sub_nt)
        sub_class.subtracting_process(var_dict)

        self.assertEqual(var_dict, {'A': 2.0})

    def test_sub_with_int_float(self):
        SUB = namedtuple('SUB', 'var value')
        sub_nt = SUB('A', 2.0)
        var_dict = {'A': 4}
        sub_class = g_arith.Subtraction(sub_nt)
        sub_class.subtracting_process(var_dict)

        self.assertEqual(var_dict, {'A': 2.0})

    def test_sub_with_str_and_int_invalid(self):
        SUB = namedtuple('SUB', 'var value')
        sub_nt = SUB('A', 2.0)
        var_dict = {'A': '"HELLO"'}
        sub_class = g_arith.Subtraction(sub_nt)
        result = sub_class.subtracting_process(var_dict)

        self.assertEqual(result, None)

    def test_sub_with_both_str_invalid(self):
        SUB = namedtuple('SUB', 'var value')
        sub_nt = SUB('A', '"WORLD"')
        var_dict = {'A': '"HELLO"'}
        sub_class = g_arith.Subtraction(sub_nt)
        result = sub_class.subtracting_process(var_dict)

        self.assertEqual(result, None)

    def test_mult_with_both_int(self):
        MULT = namedtuple('MULT', 'var value')
        mult_nt = MULT('A', 2)
        var_dict = {'A': 4}
        mult_class = g_arith.Multiplication(mult_nt)
        mult_class.multiplying_process(var_dict)

        self.assertEqual(var_dict, {'A': 8})

    def test_mult_with_both_float(self):
        MULT = namedtuple('MULT', 'var value')
        mult_nt = MULT('A', 2.0)
        var_dict = {'A': 4.0}
        mult_class = g_arith.Multiplication(mult_nt)
        mult_class.multiplying_process(var_dict)

        self.assertEqual(var_dict, {'A': 8.0})

    def test_mult_with_float_and_int(self):
        MULT = namedtuple('MULT', 'var value')
        mult_nt = MULT('A', 2.0)
        var_dict = {'A': 4}
        mult_class = g_arith.Multiplication(mult_nt)
        mult_class.multiplying_process(var_dict)

        self.assertEqual(var_dict, {'A': 8.0})

    def test_mult_with_int_and_float(self):
        MULT = namedtuple('MULT', 'var value')
        mult_nt = MULT('A', 2)
        var_dict = {'A': 4.0}
        mult_class = g_arith.Multiplication(mult_nt)
        mult_class.multiplying_process(var_dict)

        self.assertEqual(var_dict, {'A': 8.0})

    def test_mult_with_string_and_int(self):
        MULT = namedtuple('MULT', 'var value')
        mult_nt = MULT('A', '"BOO"')
        var_dict = {'A': 2}
        mult_class = g_arith.Multiplication(mult_nt)
        mult_class.multiplying_process(var_dict)

        self.assertEqual(var_dict, {'A': '"BOOBOO"'})

    def test_mult_with_int_and_str(self):
        MULT = namedtuple('MULT', 'var value')
        mult_nt = MULT('A', 2)
        var_dict = {'A': '"BOO"'}
        mult_class = g_arith.Multiplication(mult_nt)
        mult_class.multiplying_process(var_dict)

        self.assertEqual(var_dict, {'A': '"BOOBOO"'})

    def test_mult_with_float_and_str_invalid(self):
        MULT = namedtuple('MULT', 'var value')
        mult_nt = MULT('A', 1.5)
        var_dict = {'A': '"BOO"'}
        mult_class = g_arith.Multiplication(mult_nt)
        result = mult_class.multiplying_process(var_dict)

        self.assertEqual(result, None)

    def test_mult_with_str_and_float_invalid(self):
        MULT = namedtuple('MULT', 'var value')
        mult_nt = MULT('A', '"BOO"')
        var_dict = {'A': 2.5}
        mult_class = g_arith.Multiplication(mult_nt)
        result = mult_class.multiplying_process(var_dict)

        self.assertEqual(result, None)

    def test_mult_with_str_and_str_invalid(self):
        MULT = namedtuple('MULT', 'var value')
        mult_nt = MULT('A', '"BOO"')
        var_dict = {'A': '"HELLO"'}
        mult_class = g_arith.Multiplication(mult_nt)
        result = mult_class.multiplying_process(var_dict)

        self.assertEqual(result, None)

    def test_div_with_both_int(self):
        DIV = namedtuple('DIV', 'var value')
        div_nt = DIV('A', 2)
        var_dict = {'A': 4}
        div_class = g_arith.Division(div_nt)
        div_class.dividing_process(var_dict)

        self.assertEqual(var_dict, {'A': 2})

    def test_div_with_both_float(self):
        DIV = namedtuple('DIV', 'var value')
        div_nt = DIV('A', 2.0)
        var_dict = {'A': 4.0}
        div_class = g_arith.Division(div_nt)
        div_class.dividing_process(var_dict)

        self.assertEqual(var_dict, {'A': 2.0})

    def test_div_with_int_and_float(self):
        DIV = namedtuple('DIV', 'var value')
        div_nt = DIV('A', 2)
        var_dict = {'A': 4.0}
        div_class = g_arith.Division(div_nt)
        div_class.dividing_process(var_dict)

        self.assertEqual(var_dict, {'A': 2.0})

    def test_div_with_float_and_int(self):
        DIV = namedtuple('DIV', 'var value')
        div_nt = DIV('A', 2.0)
        var_dict = {'A': 4}
        div_class = g_arith.Division(div_nt)
        div_class.dividing_process(var_dict)

        self.assertEqual(var_dict, {'A': 2.0})

    def test_div_with_float_and_str(self):
        DIV = namedtuple('DIV', 'var value')
        div_nt = DIV('A', 2.0)
        var_dict = {'A': '"HELLO"'}
        div_class = g_arith.Division(div_nt)
        result = div_class.dividing_process(var_dict)

        self.assertEqual(result, None)

    def test_div_with_int_and_str(self):
        DIV = namedtuple('DIV', 'var value')
        div_nt = DIV('A', 2)
        var_dict = {'A': '"HELLO"'}
        div_class = g_arith.Division(div_nt)
        result = div_class.dividing_process(var_dict)

        self.assertEqual(result, None)

    def test_div_with_both_str(self):
        DIV = namedtuple('DIV', 'var value')
        div_nt = DIV('A', '"WORLD"')
        var_dict = {'A': '"HELLO"'}
        div_class = g_arith.Division(div_nt)
        result = div_class.dividing_process(var_dict)

        self.assertEqual(result, None)
