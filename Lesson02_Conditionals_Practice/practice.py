user_age = input("User age: ")

if user_age:
    age = int(user_age)
    movie_rating = input("Movie rating(G, PG, PG-13, R): ")

    print(f"Input: Age = {user_age}, Rating = {movie_rating}")

   
    if movie_rating == "R":
        if user_age >= 17:
            print("Output: Approved: You can watch this movie.")
        else:
            print("Output: Disaprroved: Must be 17+ for R-rated movies")
    elif movie_rating == "PG-13":
        if user_age >= 13:
            print("Output: Approved: You can watch this movie.")
        else:
            print("Output: WARNING: Not recommended for your age.")
    elif: movie_rating = "movie_rating"