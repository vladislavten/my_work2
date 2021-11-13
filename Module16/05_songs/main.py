violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# TODO здесь писать код

hm_songs = int(input('Сколько песен выбрать? '))
time = 0
for i in range(hm_songs):
    print('Название', i + 1, 'песни:', end = ' ')
    song_name = input()
    for i_song in range(len(violator_songs)):
        if song_name == violator_songs[i_song][0]:
            time += violator_songs[i_song][1]

print('\nОбщее время звучания песен:', round(time, 2))