import sys


def search_word_in_file(file_name, *args):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            if(args[0]):
                if(args[0] in content):
                    print("Found %s" % args[0])
                else:
                    print("Couldn't Find %s" % args[0])
    except FileNotFoundError:
        print(f"File '{file_name}' not found")
        print( 'usage: waga.txt', 'apple')


# Example usage:
search_word_in_file(sys.argv[1], sys.argv[2])
