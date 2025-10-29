import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

# for movies in data:
#     print(movies["title"], movies["year"])


# Age=(int(input("input year, and movie after is printed")))
# for movies in data:
#     if Age < movies["year"]:
#         print(movies["title"],movies["year"])


m = (int(input("input year, and movie after is printed")))
          


