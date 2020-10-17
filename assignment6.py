_author_ = 'Joshua Rhoades, jrhoades@email.unc.edu, Onyen = jrhoades'


# Loads data for both books and movies, returning a dictionary with two keys, 'books' and 'movies', one for
# each subset of the collection.
def load_collections():
    # Load the two collections.
    book_collection, max_book_id = load_collection("books.csv")
    movie_collection, max_movie_id = load_collection("movies.csv")

    # Check for error.
    if book_collection is None or movie_collection is None:
        return None, None

    # Return the composite dictionary.
    return {"books": book_collection, "movies": movie_collection}, max(max_book_id, max_movie_id)


# Loads a single collection and returns the data as a dictionary.  Upon error, None is returned.
def load_collection(file_name):
    max_id = -1
    try:
        # Create an empty collection.
        collection = {}

        # Open the file and read the field names
        collection_file = open(file_name, "r")
        field_names = collection_file.readline().rstrip().split(",")

        # Read the remaining lines, splitting on commas, and creating dictionaries (one for each item)
        for item in collection_file:
            field_values = item.rstrip().split(",")
            collection_item = {}
            for index in range(len(field_values)):
                if (field_names[index] == "Available") or (field_names[index] == "Copies") or (
                        field_names[index] == "ID"):
                    collection_item[field_names[index]] = int(field_values[index])
                else:
                    collection_item[field_names[index]] = field_values[index]
            # Add the full item to the collection.
            collection[collection_item["ID"]] = collection_item
            # Update the max ID value
            max_id = max(max_id, collection_item["ID"])

        # Close the file now that we are done reading all of the lines.
        collection_file.close()

    # Catch IO Errors, with the File Not Found error the primary possible problem to detect.
    except FileNotFoundError:
        print("File not found when attempting to read", file_name)
        return None
    except IOError:
        print("Error in data file when reading", file_name)
        return None

    # Return the collection.
    return collection, max_id


# Display the menu of commands and get user's selection.  Returns a string with  the user's reauexted command.
# No validation is performed.
def prompt_user_with_menu():
    print("\n\n********** Welcome to the Collection Manager. **********")
    print("COMMAND    FUNCTION")
    print("  ci         Check in an item")
    print("  co         Check out an item")
    print("  ab         Add a new book")
    print("  am         Add a new movie")
    print("  db         Display books")
    print("  dm         Display movies")
    print("  qb         Query for books")
    print("  qm         Query for movies")
    print("  x          Exit")
    return input("Please enter a command to proceed: ")


# Checks in an item
def check_in():
    print("Enter the ID for the item you wish to check in: ")


# Checks out an item
def check_out():
    print("Enter the ID for the item you wish to check out: ")
    # The program should check to see if the requested item is available. If so, the availability number should be
    # decreased by one and the user told that he/she has checked out the item. If the item is not available, or
    # if the ID is not valid, the user should be shown an appropriate error message informing them about what went wrong.


# Adds a new book
def new_book():
    print("Please enter the following attributes for the new book.")
    new_title = input("Title: ")
    new_author = input("Author: ")
    new_publisher = input("Publisher: ")
    new_pages = input("Pages: ")
    new_year = input("Year: ")
    new_copies = input("Copies: ")
    new_available = input("Available: ")
    print("You have entered the following data:")
    print(new_title)
    print(new_author)
    print(new_publisher)
    print(new_pages)
    print(new_year)
    print(new_copies)
    print(new_available)


# Adds a new movie
def new_movie():
    return Noneprint("Please enter the following attributes for the new movie.")
    new_title = input("Title: ")
    new_director = input("Director: ")
    new_genre = input("Genre: ")
    new_length = input("Length: ")
    new_year = input("Year: ")
    new_copies = input("Copies: ")
    new_available = input("Available: ")
    print("You have entered the following data:")
    print(new_title)
    print(new_director)
    print(new_genre)
    print(new_length)
    print(new_year)
    print(new_copies)
    print(new_available)


# Displays the items in the collection
def display_collection(load_collections):

    # Displays the book and movie collection
    for key in load_collections.values():
        print("ID: ", key['ID'])
        print("Title:", key['Title'])
        if key == ['Author']:
            try:
                print("Director:", key['Director'])
            except KeyError:
                print("Author:", key['Author'])
        else:
            try:
                print("Director:", key['Director'])
            except KeyError:
                print("Author:", key['Author'])
            try:
                print("Genre:", key['Genre'])
            except KeyError:
                print("Publisher:", key['Publisher'])
            try:
                print("Length:", key['Length'])
            except KeyError:
                print("Pages:", key['Pages'])

        print("Year:", key['Year'])
        print("Copies:", key['Copies'])
        print("Available:", key['Available'])
        print('\n')


# Search for a certain parameter
def query_collection():
    input("Enter a query string to use for the search: ")


# This is the main program function.  It runs the main loop which prompts the user and performs the requested actions.
def main():
    # Load the collections, and check for an error.
    library_collections, max_existing_id = load_collections()

    if library_collections is None:
        print("The collections could not be loaded. Exiting.")
        return
    print("The collections have loaded successfully.")

    # Display the error and get the operation code entered by the user.  We perform this continuously until the
    # user enters "x" to exit the program.  Calls the appropriate function that corresponds to the requested operation.

    operation = prompt_user_with_menu()
    while operation != "x":
        ###############################################################################################################
        ###############################################################################################################
        # HINTS HINTS HINTS!!! READ THE FOLLOWING SECTION OF COMMENTS!
        ###############################################################################################################
        ###############################################################################################################
        #
        # The commented-out code below gives you a some good hints about how to structure your code.
        #
        # FOR BASIC REQUIREMENTS:
        #
        # Notice that each operation is supported by a function.  That is good design, and you should use this approach.
        # Moreover, you will want to define even MORE functions to help break down these top-level user operations into
        # even smaller chunks that are easier to code.
        #
        # FOR ADVANCED REQUIREMENTS:
        #
        # Notice the "max_existing_id" variable?  When adding a new book or movie to the collection, you'll need to
        # assign the new item a unique ID number.  This variable is included to make that easier for you to achieve.
        # Remember, if you assign a new ID to a new item, be sure to keep "max_existing_id" up to date!
        #
        # Have questions? Ask on Piazza!
        #
        ###############################################################################################################
        ###############################################################################################################

        if operation == "ci":
            check_in(library_collections)
        elif operation == "co":
            check_out(library_collections)
        elif operation == "ab":
            max_existing_id = add_book(library_collections["books"], max_existing_id)
        elif operation == "am":
            max_existing_id = add_movie(library_collections["movies"], max_existing_id)
        elif operation == "db":
            display_collection(library_collections["books"])
        elif operation == "dm":
            display_collection(library_collections["movies"])
        elif operation == "qb":
            query_collection(library_collections["books"])
        elif operation == "qm":
            query_collection(library_collections["movies"])
        else:
            print("Unknown command.  Please try again.")

        operation = prompt_user_with_menu()


# Kick off the execution of the program.
main()
















