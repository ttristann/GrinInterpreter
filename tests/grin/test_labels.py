import unittest
import grin.labels as g_label

class TestLabels(unittest.TestCase):

    def test_one_label_dictionary(self):
        var_dict = {1: 'LET A 1', 2: 'FINAL: PRINT A'}
        labels_dict = g_label.creating_labels_dictionary(var_dict)

        self.assertEqual(labels_dict, {'FINAL': 1})

    def test_two_label_dictionary(self):
        var_dict = {1: 'LET A 1', 2: 'FIRST: PRINT B', 3: 'FINAL: PRINT A'}
        labels_dict = g_label.creating_labels_dictionary(var_dict)

        self.assertEqual(labels_dict, {'FIRST': 1,'FINAL': 2})

    def test_empty_label_dictionary(self):
        var_dict = {1: 'LET A 1', 2: 'PRINT A'}
        labels_dict = g_label.creating_labels_dictionary(var_dict)

        self.assertEqual(labels_dict, {})


