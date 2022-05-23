from kursach import app
import pymysql
from dataclasses import dataclass

class Database:
    genres_from_mydb = []
    executors_from_mydb = []
    songs_from_mydb = []
    albums_from_mydb = []

    def get_genres_from_mydb():
        result = []
        connection = pymysql.connections.Connection(host='localhost', user='root',passwd='0099',db='mydb')
        with connection: 
            cur = connection.cursor()
            cur.execute("SELECT title FROM genres")
            genres = cur.fetchall()
            for item in genres:
                result.append(item[0])
            return result
    def get_executors_from_mydb():
        connection = pymysql.connections.Connection(host='localhost', user='root',passwd='0099',db='mydb')
        with connection: 
            cur = connection.cursor()
            cur.execute("SELECT title FROM executors")
            title = cur.fetchall()
            cur.execute("SELECT id FROM executors")
            ids = cur.fetchall()
            cur.execute("SELECT id_genre FROM executors")
            id_genres = cur.fetchall()
            genres = []
            for id in id_genres:
                cur.execute("SELECT title FROM genres WHERE id LIKE %s", id[0])
                genre = cur.fetchall()
                genres.append(genre[0])
            groups_all = []
            for id in ids:
                groups = []
                cur.execute("SELECT title FROM music_groups WHERE id_executor LIKE %s", id[0])
                group = cur.fetchall()
                if group != ():
                    for g in group:
                        groups.append(g[0])
                else:
                    groups_all.append([])
                groups_all.append(groups)
            result = []
            for i in range(len(title)):
                result.append([title[i][0],"Состоял(а) в группе:",groups_all[i],genres[i][0]])
            return result
    def get_songs_from_mydb():
        connection = pymysql.connections.Connection(host='localhost', user='root',passwd='0099',db='mydb')
        with connection: 
            cur = connection.cursor()
            cur.execute("SELECT title FROM songs")
            title = cur.fetchall()
            cur.execute("SELECT duration FROM songs")
            duration = cur.fetchall()
            cur.execute("SELECT id_genre FROM songs")
            id_genres = cur.fetchall()
            cur.execute("SELECT id FROM executors")
            id_executors = cur.fetchall()
            genres = []
            for id in id_genres:
                cur.execute("SELECT title FROM genres WHERE id LIKE %s", id[0])
                genre = cur.fetchone()
                genres.append(genre)
            executors = []
            for id in id_executors:
                cur.execute("select title from executors where id like %s", id[0])
                executor = cur.fetchone()
                executors.append(executor)
            result = []
            for i in range(len(title)):
                result.append([title[i][0],duration[i][0],genres[i][0],executors[i][0]])
            return result
    def get_albums_from_mydb():
        connection = pymysql.connections.Connection(host='localhost', user='root',passwd='0099',db='mydb')
        with connection: 
            cur = connection.cursor()
            cur.execute("SELECT title FROM albums")
            title = cur.fetchall()
            cur.execute("SELECT sound_time FROM albums")
            duration = cur.fetchall()
            cur.execute("SELECT cost FROM albums")
            cost = cur.fetchall()
            cur.execute("SELECT id FROM albums")
            ids = cur.fetchall()
            cur.execute("SELECT id_product_type FROM albums")
            id_product_type = cur.fetchall()
            product_types = []
            for id in id_product_type:
                cur.execute("SELECT title FROM product_types WHERE id LIKE %s", id[0])
                product_type = cur.fetchone()
                product_types.append(product_type)
            executors = []
            for id in ids:
                cur.execute("SELECT title FROM music_groups WHERE id_album LIKE %s", id[0])
                executor = cur.fetchone()
                if executor != None:
                    executor = executor[0]
                executors.append(executor)
            songs_all = []
            cur.execute("SELECT id FROM songs")
            id_songs = cur.fetchall()
            for id in ids:
                songs = []
                cur.execute("SELECT title FROM songs WHERE id_album LIKE %s", id[0])
                song = cur.fetchall()
                if song != ():
                    for s in song:
                        songs.append(s[0])
                songs_all.append(songs)
            cur.execute("SELECT id_genre FROM albums")
            id_genres = cur.fetchall()
            genres = []
            for id in id_genres:
                cur.execute("SELECT title FROM genres WHERE id LIKE %s", id[0])
                genre = cur.fetchone()
                genres.append(genre)
            result = []
            for i in range(len(title)):
                result.append([title[i][0],duration[i][0],product_types[i][0],executors[i],genres[i][0],songs_all[i],cost[i][0]])
            return result
