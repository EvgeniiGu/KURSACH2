from datetime import *
from flask import render_template, request, url_for, redirect, flash, jsonify
from kursach import app
import re
from kursach.kursachMySQL import Database

#genres_from_mydb = ["Рок", "Метал", "Поп","Опера"]
#exe_cutors_from_mydb = [["Маквала Филимоновна Касрашвили","На состояла в группах",[],"Опера"],
 #             ["Кети Топурия","Состояла в группе:",["А’Студио"],"Поп"],
  #            ["Ника Кочаров","Состоял в группе:",["Nika Kocharov & Young Georgian Lolitaz"],"Рок"]]#,
      #        ["Гиги Дедаламазишвили", "Состоял в группе:", ["Mgzavrebi"],"Рок"]]
#songs_from_mydb = [["«Пиковая дама» П. И. Чайковского", "4:30", "Опера"],
#          ["«Dark Device»", "3:54", "Рок"],
#          ["«Тик-так»", "4:02", "Поп"],
#          ["Мгзаврули", "4:20", "Рок"]]
#albums_from_mydb = [["Название", "Длительность", "Название товара", "Группа", "Жанр", ["трек1", "трек2"], "Стоимость"],
#           ["«Волны»", "30 мин", "Диск", "А’Студио", "Поп", ["«Сердцем к сердцу»", "«Так же как все»", "«Это война»", "«Fashion Girl»"], "300$"]]

#search_exemple = re.search(r'-?\d+\.?\d*', albums_from_mydb[1][1], re.M|re.I)
#if search_exemple:
#   print("search --> search_exemple.group():", search_exemple.group())

@app.route('/')
def home():
    return render_template('main.html')
aldums_ = []
@app.route('/Albums.html', methods=['post', 'get'])
def album():
    genres_from_mydb = Database.get_genres_from_mydb()
    albums_from_mydb = Database.get_albums_from_mydb()
    four_minutes = 4
    eight_minutes = 8
    sixteen_minutes = 16
    thirty_two_minutes = 32
    sixty_four_minutes = 64
    #print(int(albums_from_mydb[1][1][3:5])>thirty_two_minutes)
    if request.method == 'POST':
        selected_genre = request.form.get('select_genre')
        print(selected_genre)
        selected_duration = request.form.get('select_duration')
        print(selected_duration)
        global aldums_
        aldums_ = []
        if selected_genre == "Не выбрано" and selected_duration == "Не выбрано":
            aldums_ = albums_from_mydb
        else:
            for album in albums_from_mydb:
                if int(album[1][3:5]) <= int(selected_duration[3:5].strip(" ")) and album[4] == selected_genre:
                    print(album)
                    aldums_.append(album)
    return render_template('Albums.html', genres = genres_from_mydb, albums = aldums_)
songs_ = []
@app.route('/Songs.html', methods=['post', 'get'])
def songs():
    genres_from_mydb = Database.get_genres_from_mydb()
    songs_from_mydb = Database.get_songs_from_mydb()
    executors_from_mydb = Database.get_executors_from_mydb()
    if request.method == "POST":
        selected_genre = request.form.get('select_genre')
        print(selected_genre)
        selected_executor = request.form.get('select_executor')
        print(selected_executor)
        global songs_
        songs_ = []
        if selected_genre == "Не выбрано" and selected_executor == "Не выбрано":
            songs_= songs_from_mydb
        else:
            for song in songs_from_mydb:
                print(song)
                print(" song[2] == selected_genre and song[3] == selected_executor:")
                print( song[2] , selected_genre , song[3] , selected_executor)
                if song[2] == selected_genre and song[3] == selected_executor:
                    songs_.append(song)
    print(songs_)
    return render_template('Songs.html', genres = genres_from_mydb, songs = songs_, executors=executors_from_mydb)

executor_s = []
@app.route('/Executors.html', methods=['post', 'get'])
def executors_html():
    genres_from_mydb = Database.get_genres_from_mydb()
    executors_from_mydb = Database.get_executors_from_mydb()
    if request.method == 'POST':
        selected_genre = request.form.get('select_genre')
        #print(selected_genre)
        global executor_s
        executor_s = []
        for executor in executors_from_mydb:
            if executor[3] == selected_genre:
                print(selected_genre)
                executor_s.append(executor)
        executors_from_mydb = executor_s
        print(executors_from_mydb)
        return render_template('/Executors.html', genres = genres_from_mydb, executors=executor_s)
    else:
        return render_template('/Executors.html', genres = genres_from_mydb, executors= executor_s)
