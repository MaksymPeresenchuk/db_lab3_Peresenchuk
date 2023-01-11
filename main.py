import psycopg2
import matplotlib.pyplot as plt

username = 'StudentPeresenchuk'
password = '1984'
database = 'db_lab2_Peresenchuk'
host = 'localhost'
port = '5432'

query_1 = '''
DROP VIEW IF EXISTS Amount_Of_Films_By_Country;
CREATE VIEW Amount_Of_Films_By_Country AS
SELECT TRIM(countries.country_name) AS country, COUNT(films.country_id) FROM films 
JOIN countries ON countries.country_id = films.country_id
GROUP BY country_name;
SELECT * FROM Amount_Of_Films_By_Country;
'''

query_2 = '''
DROP VIEW IF EXISTS Genres_Percent;
CREATE VIEW Genres_Percent AS
SELECT TRIM(genres.genre_name) AS genre, COUNT(films.genre_id) FROM films 
JOIN genres ON genres.genre_id = films.genre_id
GROUP BY genre_name;
SELECT * FROM Genres_Percent;
'''

query_3 = '''
DROP VIEW IF EXISTS Show_Ratings;
CREATE VIEW Show_Ratings AS
SELECT TRIM(film_title) AS film_title, average_rating FROM films
WHERE average_rating > 7.5
ORDER BY average_rating;
SELECT * FROM Show_Ratings;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


with conn:
    cur = conn.cursor()

# query_1
    cur.execute(query_1)
    country = []
    n_films = []

    for row in cur:
        country.append(row[0])
        n_films.append(row[1])

    x_range = range(len(country))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)

    bar_ax.bar(x_range, n_films, label='Total')
    bar_ax.set_title('Кількість фільмів кожної країни')
    bar_ax.set_xlabel('Фільми')
    bar_ax.set_ylabel('Кількість фільмів')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(country, rotation=45)

# query_2
    cur.execute(query_2)
    genres = []
    films = []

    for row in cur:
        genres.append(row[0])
        films.append(row[1])

    pie_ax.pie(films, labels=genres, autopct='%1.1f%%')
    pie_ax.set_title('Частка фільмів за жанром')

# query_3
    cur.execute(query_3)
    title = []
    ratings = []

    for row in cur:
        title.append(row[0])
        ratings.append(row[1])

    graph_ax.plot(title, ratings, marker='o')
    graph_ax.set_xlabel('Назви фільмів')
    graph_ax.set_ylabel('Рейтинг')
    graph_ax.set_title('Назви фільмів, у яких рейтинг більший за 7.5')
    graph_ax.set_xticklabels(title, rotation=40)

    for qnt, price in zip(title, ratings):
        graph_ax.annotate(price, xy=(qnt, price), xytext=(7, 2), textcoords='offset points')


mng = plt.get_current_fig_manager()
mng.resize(1400, 750)

plt.subplots_adjust(left=0.1, bottom=0.19, right=0.94, top=0.9, wspace=0.4, hspace=0.4)

plt.show()

