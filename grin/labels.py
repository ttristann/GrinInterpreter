# Module that handles the process of accessing the information
# when the grin line has a LABEL.

import grin.reading_input as g_input

def creating_labels_dictionary(input_dict):
    """
    Creates a dictionary that maps the name of the label and
    its associating index within the grin program.

    Returns the newly created the dictionary to the main module.
    """
    labels_dict = {}
    for key, value in input_dict.items():
        if ':' in value:
            labels_dict[value.split()[0][:-1]] = key - 1

    return labels_dict

def creation_of_label_namedtuple(grin_command):
    """
    Creates a specific namedtuple listed in the grin.reading_input
    module for the grin command associated with the label.

    Returns the newly created namedtuple to be added in the
    collection of namedtuples of the grin commands.
    """
    nt_collection = []
    g_input.creating_various_namedtuples(grin_command, nt_collection)
    return nt_collection[0]





