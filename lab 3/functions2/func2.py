# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
is_above_5_5 = lambda movie: movie.get("imdb", 0) > 5.5

results = {movie["name"]: is_above_5_5(movie) for movie in movies}

for movie, result in results.items():
    print("{}: {}".format(movie, result))

#2
def goodmovie(): 
    result = [] 
    for movie in movies: 
        if goodmovie(movie.get('idmb', 0)): 
            result.append(movie) 
    return result
        

#3
def returncategory(category): 
    result = [] 
    for movie in movies: 
        if movie.get('category') == category: 
            result.append(movie) 
    return result

print(returncategory('Thriller'))

#4
def averagescorelist(): 
    count=0 
    sum=0 
    for movie in movies: 
        sum += float(movie.get('imdb')) 
        count += 1 
    return (sum / count) 

#5
def averageScore(category): 
    listcategory = averageScore(category) 
    return averageScore(listcategory)

