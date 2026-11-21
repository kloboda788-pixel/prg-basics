# Program to write movie details to a text file

# Variables containing movie details
movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"

# Name of the file to write to
file_name = 'movie_details.txt'

# Writing movie details to the file
# 'w' - write mode: creates the file or overwrites it
with open(file_name, 'w', encoding='utf-8') as file:
    # \n moves to the next line in the file
    file.write(f"Movie Title: {movie_title}\n")
    file.write(f"Director: {director}\n")
    file.write(f"Lead Actor: {lead_actor}\n")

print(f"Movie details have been written to {file_name}.")