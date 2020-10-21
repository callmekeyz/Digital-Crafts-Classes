#def multi_two_numbers(a,b):
    #print(a*b)

#a = 10
#b = 10
#multi_two_numbers(a,b)


def movie(movie_item):
    title = movie_item[0]
    genre = movie_item[1]
    year = movie_item[2]

    print(f"1. title: {title}")
    print(f"2. genere: {genre}")
    print(f"3.year: {year}")

def movie(movie_item):
    idx = 1
    for item in movie_item:
        print(f"{idx},{item}:{movie_item{item}}")
        idx += 1