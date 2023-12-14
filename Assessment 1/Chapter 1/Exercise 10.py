#creating a dictionary for film details
film = {
    "Genre": "Thriller/ Action/ History/ Documentary/ Mystery/ Drama",
    "Title": "Oppenheimer",
    "Director": "Christopher Nolan",
    "Year": 2023,
    
    
}

#showing film details using loop
print("Film Details:")
for key, value in film.items():
    print(f"{key}: {value}")