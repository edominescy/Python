import os


def load(name):
    """
    This method creates and loads a new journal.

    :param name: This is the base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = get_full_path(name)
    if os.path.exists(filename):
        with open(filename) as fileIn:
            for entry in fileIn.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    """
    This method saves the journal data at the end of each journal session.

    :param name: This is the base name of the journal to load.
    :param journal_data: This is the variable to store the data of the journal in.
    """
    filename = get_full_path(name)
    print('.... saving to: {}'.format(filename))

    with open(filename, 'w') as fileOut:
        for entry in journal_data:
            fileOut.write(entry + '\n')


def get_full_path(name):
    """
    This method creates and returns the full path where the journal is to be stored.

    :param name:  This is the base name of the journal to load.
    :return: Returns the full filename path.
    """
    filename = os.path.abspath(os.path.join('.', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    """
    This method adds the entry to the journal.

    :param text: This is the entry given by the user.
    :param journal_data: This is the variable used to store the entries.
    """
    journal_data.append(text)
