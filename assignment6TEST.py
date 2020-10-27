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
def check_in(library_collections):
    stop_loop = 0

    # The program should prompt the user to enter an ID number.
    check_in_item = int(input("Enter the ID for the item you wish to check in: "))

    # Iterates through the first and second levels of the library_collections dictionary
    for library_id, library_content in library_collections.items():

        # Iterates through the third level of the library_collections dictionary
        for key in library_content:
            second_step = key
            third_step = library_content[key]

            # If the inputted ID matches any of the ID numbers
            if check_in_item == second_step:
                if third_step['Available'] == third_step['Copies']:
                    print("All copies are already available, so this item can not be checked in.")

                # If Available copies is less than total copies
                if third_step['Available'] < third_step['Copies']:
                    print("Your check in has been successful.")
                    third_step['Available'] += 1
                    print("ID: ", third_step['ID'])
                    print("Title:", third_step['Title'])
                    try:
                        print("Director:", third_step['Director'])
                        print("Length:", third_step['Length'])
                        print("Genre:", third_step['Genre'])
                    except KeyError:
                        print("Author:", third_step['Author'])
                        print("Publisher:", third_step['Publisher'])
                        print("Pages:", third_step['Pages'])
                    print("Year:", third_step['Year'])
                    print("Copies:", third_step['Copies'])
                    print("Available:", third_step['Available'])
                    print('')

                stop_loop += 1

    # If ID does not match the inputted ID, return an error message
    if stop_loop == 0:
        print("Error: can not find the ID you were looking for.")


# Checks out an item
def check_out(library_collections):
    stop_loop = 0

    # Asks the user to input the ID they wish to check out
    check_out_item = int(input("Enter the ID for the item you wish to check out: "))

    # Iterates through the first and second levels of the library_collections dictionary
    for library_id, library_content in library_collections.items():

        # Iterates through the third level of the library_collections dictionary
        for key in library_content:
            second_step = key
            third_step = library_content[key]

            # Matches the inputted ID number with all unique identifiers
            if check_out_item == second_step:
                # If available copies is less than zero
                if third_step['Available'] <= 0:
                    print("No copies of the item are available for check out.")

                # If available copies is equal to total amount of copies or greater than zero
                if third_step['Available'] == third_step['Copies'] or third_step['Available'] > 0:
                    print("Your check out has been successful.")
                    third_step['Available'] -= 1
                    print("ID: ", third_step['ID'])
                    print("Title:", third_step['Title'])
                    try:
                        print("Director:", third_step['Director'])
                        print("Length:", third_step['Length'])
                        print("Genre:", third_step['Genre'])
                    except KeyError:
                        print("Author:", third_step['Author'])
                        print("Publisher:", third_step['Publisher'])
                        print("Pages:", third_step['Pages'])
                    print("Year:", third_step['Year'])
                    print("Copies:", third_step['Copies'])
                    print("Available:", third_step['Available'])
                    print('')

                stop_loop += 1

    # If the stop_loop variable is equal to zero, print an error message
    if stop_loop == 0:
        print("Error: can not find the ID you were looking for.")


# Adds a new book
def add_book(library_collections, max_existing_id):
    # Asks the user to input the book details
    print("Please enter the following attributes for the new book.")
    new_title = input("Title: ")
    new_author = input("Author: ")
    new_publisher = input("Publisher: ")
    new_pages = input("Pages: ")
    new_year = input("Year: ")
    new_copies = int(input("Copies: "))

    # Shows the details that were entered to ensure accuracy
    print("You have entered the following data:")
    print("ID: ", max_existing_id + 1)
    print("Title: ", new_title)
    print("Author: ", new_author)
    print("Publisher: ", new_publisher)
    print("Pages: ", new_pages)
    print("Year: ", new_year)
    print("Copies: ", new_copies)
    print("Available: ", new_copies)

    # Asks the user if they want to add the details to the dictionary
    add_to_collection = input("Press enter to add this book to the collection.  Enter 'x' to cancel. ")

    # Adds the specific book details to the dictionary if the user hits enter
    if add_to_collection == '':
        library_collections[max_existing_id + 1] = {'Title': str(new_title), 'Author': str(new_author),
        'Publisher': str(new_publisher), 'Pages': str(new_pages), 'Year': str(new_year),
        'Copies': int(new_copies), 'Available': int(new_copies), 'ID': max_existing_id + 1}
        print("Your book has been added.")

        # Updates the max existing ID
        max_existing_id = max_existing_id + 1
        return max_existing_id
    else:
        return print("Your book was not added.")


# Adds a new movie
def add_movie(library_collections, max_existing_id):
    # Asks the user to input the movie details
    print("Please enter the following attributes for the new movie.")
    new_title = input("Title: ")
    new_director = input("Director: ")
    new_length = input("Length: ")
    new_genre = input("Genre: ")
    new_year = input("Year: ")
    new_copies = int(input("Copies: "))

    # Shows the details that were entered to ensure accuracy
    print("You have entered the following data:")
    print("ID: ", max_existing_id + 1)
    print("Title: ", new_title)
    print("Director: ", new_director)
    print("Length: ", new_length)
    print("Genre: ", new_genre)
    print("Year: ", new_year)
    print("Copies: ", new_copies)
    print("Available: ", new_copies)

    # Asks the user if they want to add the details to the dictionary
    add_to_collection = input("Press enter to add this movie to the collection.  Enter 'x' to cancel. ")

    # Adds the specific movie details to the dictionary if the user hits enter
    if add_to_collection == '':
        library_collections[max_existing_id + 1] = {'Title': str(new_title), 'Director': str(new_director),
        'Genre': str(new_genre), 'Length': str(new_length), 'Year': str(new_year),
        'Copies': int(new_copies), 'Available': int(new_copies), 'ID': max_existing_id + 1}
        print("Your movie has been added.")

        # Updates the max existing ID
        max_existing_id = max_existing_id + 1
        return max_existing_id
    else:
        return print("Your movie was not added.")


# Displays the items in the collection
def display_collection(library_collections):

    # Variable is used to initialize the count
    count = 0

    # Makes a new list that stores the ID numbers in numerical order
    id_list = []
    for key in library_collections:
        id_list.append(key)
        id_list.sort()

    # Displays the collection
    for value in id_list:
        print("ID: ", library_collections[value]['ID'])
        print("Title:", library_collections[value]['Title'])
        try:
            print("Director:", library_collections[value]['Director'])
            print("Length:", library_collections[value]['Length'])
            print("Genre:", library_collections[value]['Genre'])
        except KeyError:
            print("Author:", library_collections[value]['Author'])
            print("Publisher:", library_collections[value]['Publisher'])
            print("Pages:", library_collections[value]['Pages'])
        print("Year:", library_collections[value]['Year'])
        print("Copies:", library_collections[value]['Copies'])
        print("Available:", library_collections[value]['Available'])
        print('')
        count += 1

        # While count is equal to ten, asks the user if they want more items printed
        while count == 10:

            # Resets the count to zero, causing it to close out of the loop
            count = 0
            continue_input = input("Press enter to show more items, or type 'm' to return to the menu: ")
            if continue_input == 'm':
                return
            elif continue_input == '':
                count = 0
            else:
                return print("Error: Invalid input detected.")


# Search for a certain parameter
def query_collection(library_collections):
    # Asks the user to input a query string
    query_search = str(input("Enter a query string to use for the search: "))

    # Iterates through the dictionary
    for library_id, library_content in library_collections.items():

        # Iterates through the second level of keys in the dictionary
        for key in library_content:
            third_step = str(library_content[key])

            # Searches to see if the query search matches any of the collections
            if query_search.lower() in third_step.lower():
                print("ID: ", library_content['ID'])
                print("Title:", library_content['Title'])
                try:
                    print("Director:", library_content['Director'])
                    print("Length:", library_content['Length'])
                    print("Genre:", library_content['Genre'])
                except KeyError:
                    print("Author:", library_content['Author'])
                    print("Publisher:", library_content['Publisher'])
                    print("Pages:", library_content['Pages'])
                print("Year:", library_content['Year'])
                print("Copies:", library_content['Copies'])
                print("Available:", library_content['Available'])
                print('')


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
















