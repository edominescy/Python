import journal
import time


def timestamp_now():
    """
    timestamp_now function returns the timestamp in the format of hours:minutes.

    :return: Returns the time when called.
    """
    return str(time.strftime("%H:%M"))


def today():
    """
    today function returns the month, day, and year respectively in that format.

    :return: Returns the date when called.
    """
    return str(time.strftime("%m-%d-%y"))


def main():
    """
    main function is where the other functions in the program are run.
    """
    printHeader()
    runEventLoop()



def printHeader():
    """
    printHeader function prints the header for the program.
    """
    print('-----------------------------')
    print('         JOURNAL APP')
    print('-----------------------------')



def runEventLoop():
    """
    runEventLoop function is where the user interacts with the journal by viewing
        previous entries, adding an entry, or exiting the journal. Once the user
        chooses to exit the program, the entries are saved as a file called
        'journal.jrl' found wherever the program is stored and it reads as a text
        file.
    """
    journal_name = 'journal'
    journal_data = journal.load(journal_name)  # []  # list()

    print('What would you like to do with your journal?')
    cmd = 'EMPTY'

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, '{}' is not an understood command.".format(cmd))

    journal.save(journal_name, journal_data)
    print('Goodbye!')


def list_entries(entries):
    """
    list_entries function lists all entries with most recent at the bottom of the list.
    A copy of the data from the entries list is made and because it is a shallow copy,
    it is used to display the list of entries while there is data in the copy.

    :param entries: The extended list of data so it will include all new entries and old entries.
    """
    print('---------------')
    print('    ENTRIES')
    print('---------------')
    entrylist = entries.copy()
    while entrylist:
        print('* {} '.format(entrylist.pop(0)))
        print('   written {} '.format(entrylist.pop(0)))
        print('   @ {}'.format(entrylist.pop(0)))


def add_entry(data):
    """
    add_entry function is called when the user wishes to add an entry to the journal. It adds
    the entry as well as the date and time the entry was entered and stores them into the data list.
    The entries list was created to make a copy of the data list after it is recorded.

    :param data: This list is where the entry data is stored, and is then added to an extended
        list called entries.
    """
    text = input('Type your entry, <enter> to exit: \n')
    date = today()
    timestamp = timestamp_now()
    journal.add_entry(text, data)
    journal.add_entry(date, data)
    journal.add_entry(timestamp, data)
    entries = []
    entries.extend(data)


main()
