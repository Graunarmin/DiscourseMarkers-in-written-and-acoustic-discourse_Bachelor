import sys
import CorpusParser as cp
import ShowFilter as sf

def error():
    if len(sys.argv) < 2:
        print ("""ERROR: \n
                Please specify which functionality should be executed by typing either 'Parser' or 'Filter'""")
        sys.exit(1)

def main():

    error()

    function = sys.argv[1]

    if function == "parser":
        file = sys.argv[2]
        arguments = sys.argv[3]
        parser = cp.CorpusParser(file, arguments)
        parser.read_lines()

    elif function == "filter":
        show_filter = sf.ShowFilter()
        show_filter.read_in_shows()
    
    else:
        print("ERROR: Invalid functionality. Try 'parser' or 'filter'")
        sys.exit(1)

if __name__ == '__main__':
    main()