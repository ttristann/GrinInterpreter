# project3.py
# The main module that executes your Grin interpreter.

import grin.reading_input as g_input
import grin.variables as g_var
import grin.asking_input as g_ask
import grin.arithmetic as g_arith
import grin.goto_process as g_goto
import grin.labels as g_label
import grin.gosub_process as g_gosub


def main() -> None:

    input_dict = g_input.creating_input_dict()
    lexing_tokens_list = g_input.lexing_process(input_dict)
    parsing_tokens_list = g_input.parsing_process(input_dict)
    if type(parsing_tokens_list) is not list:
        print(parsing_tokens_list)
        quit()

    labels_dict = g_label.creating_labels_dictionary(input_dict)
    namedtuple_collection = []

    for parsing_token in parsing_tokens_list:
        g_input.creating_various_namedtuples(parsing_token, namedtuple_collection)

    universal_variables_dict = {}
    current_return_index = 0
    current_index = 0
    max_index = len(namedtuple_collection)
    while current_index != max_index:
        ind_nt = namedtuple_collection[current_index]
        if type(ind_nt) is g_input.LET:
            var_class = g_var.Variables(ind_nt)
            var_class.assigning_variables(universal_variables_dict)
            current_index += 1
        elif type(ind_nt) is g_input.PRINT:
            print_class = g_var.Print(ind_nt)
            print_class.printing_variables(universal_variables_dict)
            current_index += 1
        elif type(ind_nt) is g_input.INNUM:
            innum_class = g_ask.Innum(ind_nt)
            innum_result = innum_class.storing_into_variables_dict(universal_variables_dict)
            if innum_result is None:
                print('The inputted value is invalid. Must be the type of int or float')
                quit()
            current_index += 1
        elif type(ind_nt) is g_input.INSTR:
            instr_class =  g_ask.Instr(ind_nt)
            instr_class.storing_into_variables_dict(universal_variables_dict)
            current_index += 1
        elif type(ind_nt) is g_input.ADD:
            add_class = g_arith.Addition(ind_nt)
            add_result = add_class.adding_process(universal_variables_dict)
            if add_result is None:
                print('Invalid Operation. Cannot add a int/float with a string literal')
                quit()
            current_index += 1
        elif type(ind_nt) is g_input.SUB:
            sub_class = g_arith.Subtraction(ind_nt)
            sub_result = sub_class.subtracting_process(universal_variables_dict)
            if sub_result is None:
                print('Invalid Operation. Cannot do subtraction a int/float and a string literal')
                quit()
            current_index += 1
        elif type(ind_nt) is g_input.MULT:
            mult_class = g_arith.Multiplication(ind_nt)
            mult_result = mult_class.multiplying_process(universal_variables_dict)
            if mult_result is None:
                print('Invalid Operation. Cannot multiply a float/string with a string literal')
                quit()
            current_index += 1
        elif type(ind_nt) is g_input.DIV:
            div_class = g_arith.Division(ind_nt)
            div_result = div_class.dividing_process(universal_variables_dict)
            if div_result is None:
                print('Invalid Operation. Cannot divide with literal strings')
                quit()
            current_index += 1
        elif type(ind_nt) is g_input.GOTO:
            goto_class = g_goto.GOTO(ind_nt)
            goto_result = goto_class.jumping_process(current_index, max_index, labels_dict, universal_variables_dict)
            if goto_result is None:
                print('Invalid line to jump to.')
                quit()
            current_index = goto_result
        elif type(ind_nt) is g_input.GOSUB:
            gosub_class = g_gosub.GOSUB(ind_nt)
            gosub_result = gosub_class.gosub_jumping_process(current_index, max_index, labels_dict, universal_variables_dict)
            if gosub_result is None:
                print('Invalid line to jump to')
                quit()
            current_return_index = current_index + 1
            current_index = gosub_result
        elif type(ind_nt) is g_input.C_GOTO:
            c_goto_class = g_goto.CONT_GOTO(ind_nt)
            c_goto_class.figuring_out_values(universal_variables_dict)
            g_goto_cont = c_goto_class.determining_conditionally()
            if g_goto_cont is True:
                c_goto_class_result = c_goto_class.jumping_process(current_index, max_index, labels_dict, universal_variables_dict)
                if c_goto_class_result is None:
                    print('Invalid line to jump to')
                    quit()
                current_index = c_goto_class_result
            else:
                current_index += 1
        elif type(ind_nt) is g_input.C_GOSUB:
            c_gosub_class = g_gosub.CONT_GOSUB(ind_nt)
            c_gosub_class.c_gosub_figuring_out_values(universal_variables_dict)
            c_gosub_cont = c_gosub_class.c_gosub_determining_conditionally()
            if c_gosub_cont is True:
                c_gosub_class_result = c_gosub_class.gosub_jumping_process(current_index, max_index, labels_dict, universal_variables_dict)
                if c_gosub_class_result is None:
                    print('Invalid line to jump to')
                    quit()
                current_return_index = current_index + 1
                current_index = c_gosub_class_result
            else:
                current_index += 1
        elif type(ind_nt) is g_input.RETURN:
            current_index = current_return_index
        elif type(ind_nt) is g_input.END:
            quit()


if __name__ == '__main__':
    main()
