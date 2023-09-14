import sqlite3

# Read the file and copy content to a list
with open("stephen_king_adaptations.txt", "r") as file:
    stephen_king_adaptations_list = [line.strip().split(",") for line in file]

# Establish a connection with the SQLite database
conn = sqlite3.connect("stephen_king_adaptations.db")
cursor = conn.cursor()

# Create the table
cursor.execute('''CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table 
                  (movieID TEXT, movieName TEXT, movieYear INT, imdbRating REAL)''')

# Insert data into the table
for adaptation in stephen_king_adaptations_list:
    cursor.execute("INSERT INTO stephen_king_adaptations_table VALUES (?, ?, ?, ?)", adaptation)

# Save changes to the database
conn.commit()

# Search for movies in the database
while True:
    print("\nOptions:")
    print("1. Search by movie name")
    print("2. Search by movie year")
    print("3. Search by movie rating")
    print("4. STOP")
    option = input("Enter your choice: ")

    if option == "1":
        movie_name = input("Enter the movie name: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName = ?", (movie_name,))
        result = cursor.fetchone()

        if result is not None:
            print("Movie Details:")
            print("Movie ID: ", result[0])
            print("Movie Name: ", result[1])
            print("Movie Year: ", result[2])
            print("IMDB Rating: ", result[3])
        else:
            print("No such movie exists in our database")

    elif option == "2":
        movie_year = input("Enter the movie year: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear = ?", (movie_year,))
        result = cursor.fetchall()

        if len(result) > 0:
            print("Movies released in {}:".format(movie_year))
            for movie in result:
                print("Movie ID: ", movie[0])
                print("Movie Name: ", movie[1])
                print("Movie Year: ", movie[2])
                print("IMDB Rating: ", movie[3])
        else:
            print("No movies were found for that year in our database.")

    elif option == "3":
        rating_limit = float(input("Enter the minimum rating: "))
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (rating_limit,))
        result = cursor.fetchall()

        if len(result) > 0:
            print("Movies with rating {} and above:".format(rating_limit))
            for movie in result:
                print("Movie ID: ", movie[0])
                print("Movie Name: ", movie[1])
                print("Movie Year: ", movie[2])
                print("IMDB Rating: ", movie[3])
        else:
            print("No movies at or above that rating were found in the database.")

    elif option == "4":
        break

# Close the database connection
conn.close()
