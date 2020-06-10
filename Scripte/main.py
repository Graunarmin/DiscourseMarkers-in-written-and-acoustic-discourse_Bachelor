import sys
import ShowFilter as sf

def error():
    if len(sys.argv) < 2:
        print ("""ERROR: \n
                Please specify which functionality should be executed by typing filter'""")
        sys.exit(1)

def main():

    error()

    function = sys.argv[1]

    if function == "filter":
        show_filter = sf.ShowFilter()
        show_filter.read_in_shows()
    
    else:
        print("ERROR: Invalid functionality. Try filter'")
        sys.exit(1)

if __name__ == '__main__':
    main()