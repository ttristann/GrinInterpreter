import unittest
import grin.parsing as g_parse
import grin.reading_input as g_input


class TestReadingInput(unittest.TestCase):

    def test_lexing_process(self):
        sample_dict = {1: 'LET A 3', 2: 'PRINT A'}
        lexing_list = g_input.lexing_process(sample_dict)
        self.assertEqual(len(lexing_list), 2)


    def test_parsing_process(self):
        sample_dict = {1: 'LET A 3', 2: 'LET B 2', 3: 'ADD A B', 4: 'PRINT A'}
        parsing_list = g_input.parsing_process(sample_dict)
        self.assertEqual(len(parsing_list), 4)

    def test_invalid_parsing_process(self):
        sample_dict = {1: 'INVALID ONE'}
        parsing_list = g_input.parsing_process(sample_dict)
        self.assertEqual(type(parsing_list), g_parse.GrinParseError)


    def test_creation_of_namedtuples_one(self):
        sample_dict = {1: 'LET A 3'}
        parsing_list = g_input.parsing_process(sample_dict)
        nt_collection = []
        for token in parsing_list:
            g_input.creating_various_namedtuples(token, nt_collection)

        self.assertEqual(len(nt_collection), 1)

    def test_creation_of_namedtuples_various(self):
        sample_dict = {1: 'LET A 3', 2: 'LET B 2', 3: 'ADD A B', 4: 'PRINT A'}
        parsing_list = g_input.parsing_process(sample_dict)
        nt_collection = []
        for token in parsing_list:
            g_input.creating_various_namedtuples(token, nt_collection)

        self.assertEqual(len(nt_collection), 4)

