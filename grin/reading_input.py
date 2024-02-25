# Module that handles the functionality of asking,
# reading, and processing the inputs given by
# the user.
import sys

# Takes the inputted Grin lines to lexed and parsed
# to check the validity of each lines and be
# converted into Grin tokens.

# If all lines are valid, they are executed in order,
# based on its type.

import grin.lexing as lexing
import grin.parsing as parsing
import grin.labels as g_label
from collections import namedtuple


LET = namedtuple('LET', "var value")
PRINT = namedtuple('PRINT', 'value')
INNUM = namedtuple('INNUM', 'var')
INSTR = namedtuple('INSTR', 'var')
ADD = namedtuple('ADD', 'var value')
SUB = namedtuple('SUB', 'var value')
MULT = namedtuple('MULT', 'var value')
DIV = namedtuple('DIV', 'var value')
GOTO = namedtuple('GOTO', 'target')
C_GOTO = namedtuple('C_GOTO', 'target val1 op val2')
GOSUB = namedtuple('GOSUB', 'target')
C_GOSUB = namedtuple('C_GOSUB', 'target val1 op val2')
END = namedtuple('END', 'index')
RETURN = namedtuple('RETURN', 'index')
LABEL = namedtuple('LABEL', 'name nt')


def creating_input_dict():
    """
    Creates a dictionary that is organized in a way that has it
    keys being the line number, starting from 1, and its associated
    values being the input or grin line.

    It strips any unnecessary spaces within the input.
    """
    main_dict = {}
    while True:
        raw_line = input()
        split_line = raw_line.split()
        grin_line = ' '.join(split_line)
        if grin_line == '.':
            break

        main_dict[len(main_dict) + 1] = grin_line

    return main_dict

def lexing_process(adict):
    """
    Takes a dictionary which its entries are the line numbers and the grin line
    associated with it.

    Iterates through each line number and grin line and uses them to be passed
    into the to_tokens function from the lexing module to create a stream of tokens.

    Returns a list of the newly formed stream of tokens.
    """
    lexing_tokens_list = []
    for line_num, grin_line in adict.items():
        try:
            line_token = lexing.to_tokens(grin_line, line_num)
            lex_token_list = [lex_token for lex_token in line_token]
            lexing_tokens_list.append(lex_token_list)
        except lexing.GrinLexError as error:
            return None, error

    return lexing_tokens_list

def parsing_process(adict):
    """
    Takes a list of strings that is composed of all the lines in the grin code
    and then takes that list to be used in parse function from the parsing module

    If an error comes up in the process, the function causes the system to print
    a corresponding message from the parse function and prints it to the output
    and quits the program

    If no errors, it returns a sequence of GrinTokens.
    """
    grin_lines = [lines for lines in adict.values()]
    parsing_tokens_list = []
    parsing_tokens = parsing.parse(grin_lines)
    try:
        for token in parsing_tokens:
            parsing_tokens_list.append(token)
    except parsing.GrinParseError as error:
        return error

    return parsing_tokens_list

def creating_various_namedtuples(parsing_line_token, collection):
    """
    Checks the type of token and matches it to the corresponding type
    to create the matching the namedtuple to cleanly organize the
    information constructed in the token.

    Appends the newly constructed namedtuple into a collection of
    namedtuples.
    """
    main_identifier = str(parsing_line_token[0]._kind)
    if main_identifier == 'GrinTokenKind.LET':
        let_var = parsing_line_token[1]._value
        if str(parsing_line_token[2]._kind) == 'GrinTokenKind.LITERAL_STRING':
            let_value = f'"{parsing_line_token[2]._value}"'
        else: let_value = parsing_line_token[2]._value
        let_nt = LET(let_var, let_value)
        collection.append(let_nt)

    elif main_identifier == 'GrinTokenKind.PRINT':
        if str(parsing_line_token[1]._kind) == 'GrinTokenKind.LITERAL_STRING':
            print_value = f'"{parsing_line_token[1]._value}"'
        else: print_value = parsing_line_token[1]._value
        print_nt = PRINT(print_value)
        collection.append(print_nt)

    elif main_identifier == 'GrinTokenKind.INNUM':
        innum_var = parsing_line_token[1]._value
        innum_nt = INNUM(innum_var)
        collection.append(innum_nt)

    elif main_identifier == 'GrinTokenKind.INSTR':
        instr_var = parsing_line_token[1]._value
        instr_nt = INSTR(instr_var)
        collection.append(instr_nt)

    elif main_identifier == 'GrinTokenKind.ADD':
        add_var = parsing_line_token[1]._value
        if str(parsing_line_token[2]._kind) == 'GrinTokenKind.LITERAL_STRING':
            add_value = f'"{parsing_line_token[2]._value}"'
        else: add_value = parsing_line_token[2]._value
        add_nt = ADD(add_var, add_value)
        collection.append(add_nt)

    elif main_identifier == 'GrinTokenKind.SUB':
        sub_var = parsing_line_token[1]._value
        sub_value = parsing_line_token[2]._value
        sub_nt = SUB(sub_var, sub_value)
        collection.append(sub_nt)

    elif main_identifier == 'GrinTokenKind.MULT':
        mult_var = parsing_line_token[1]._value
        if str(parsing_line_token[2]._kind) == 'GrinTokenKind.LITERAL_STRING':
            mult_value = f'"{parsing_line_token[2]._value}"'
        else: mult_value = parsing_line_token[2]._value
        mult_nt = MULT(mult_var, mult_value)
        collection.append(mult_nt)

    elif main_identifier == 'GrinTokenKind.DIV':
        div_var = parsing_line_token[1]._value
        div_value = parsing_line_token[2]._value
        div_nt = DIV(div_var, div_value)
        collection.append(div_nt)

    elif main_identifier == 'GrinTokenKind.GOTO':
        if len(parsing_line_token) == 2:
            goto_target = parsing_line_token[1]._value
            goto_nt = GOTO(goto_target)
            collection.append(goto_nt)
        else:
            c_goto_target = parsing_line_token[1]._value
            c_goto_val1 = parsing_line_token[3]._value
            c_goto_op = parsing_line_token[4]._text
            c_goto_val2 = parsing_line_token[5]._value
            c_goto_nt = C_GOTO(c_goto_target, c_goto_val1, c_goto_op, c_goto_val2)
            collection.append(c_goto_nt)

    elif main_identifier == 'GrinTokenKind.GOSUB':
        if len(parsing_line_token) == 2:
            gosub_target = parsing_line_token[1]._value
            gosub_nt = GOSUB(gosub_target)
            collection.append(gosub_nt)
        else:
            c_gosub_target = parsing_line_token[1]._value
            c_gosub_val1 = parsing_line_token[3]._value
            c_gosub_op = parsing_line_token[4]._text
            c_gosub_val2 = parsing_line_token[5]._value
            c_gosub_nt = C_GOSUB(c_gosub_target, c_gosub_val1, c_gosub_op, c_gosub_val2)
            collection.append(c_gosub_nt)

    elif main_identifier == 'GrinTokenKind.IDENTIFIER':
        grin_nt = g_label.creation_of_label_namedtuple(parsing_line_token[2:])
        collection.append(grin_nt)


    elif main_identifier == 'GrinTokenKind.END':
        end_nt = END(0)
        collection.append(end_nt)

    elif main_identifier == 'GrinTokenKind.RETURN':
        return_nt = RETURN(0)
        collection.append(return_nt)



