"""
Midterm Practical Exam — Movie Collection Manager
Student: Pereda,Chris Euki
"""
menu = input()
movies= ["Spiderman - Sam Raimi","Ghost Rider - Mark Steven Johnson","Superman - James Gunn"]


title = input("Enter the Title:")
director = input("Enter the Director:")
status = input("Enter the Status:")
choice = input("Choose an option:")

def display_menu():
    print ("Welcome to Movie Collection Manager")
    print("1. Add a movie")
    print("2. View all movies")
    print("3. Count watched vs unwatched")
    print("4.Find a movie")
    print("5.Exit")
    print(choice)
    if choice == 1:
        (add_movie)
    elif choice == 2:
        (view_movies)
    elif choice == 3:
        (count_watched_unwatched)
    elif choice == 4:
        (find_movie)
    elif choice == 5:
        (exit)
    return()
    
    # print the menu
    # return the user's choice
    pass


def add_movie(movie_list):
    
    print(title)
    print(director)
    print(status)
    movielist.append(title,director,status)
    
    # ask for title, director, and status
    # build the movie string
    # add it to the list
    pass


def view_movies(movie_list):
    for movie in movies:
        print(movie)
    # loop through and print every movie
    # handle empty list
    pass


def count_watched_unwatched(movie_list):

     

    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass


def find_movie(movie_list):
    print("Search Movie Title:")
    if movies == True:
        print(movies)
    elif movies == False:
        print("Movies Not Found")   # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass


def main():
    print
    # create the main menu loop
    # call the appropriate function based on the user's choice
    pass


main()
display_menu()


