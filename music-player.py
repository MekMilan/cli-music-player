from os import system, remove

system("cls")

NOME            = input("qual nome da playlist ?: ")
PLAYLIST_URL    = input("Input playlist url: ")

system("cls")
print(f'running...')

PLAYLIST_URL = PLAYLIST_URL.split('&')

link = PLAYLIST_URL[0] + '\"' + "&" + '\"' + PLAYLIST_URL[1]

system(f"youtube-dl --get-id {link} >> temp-{NOME}.txt")

count = -1
list_of_url = []

with open(f'temp-{NOME}.txt', 'r+') as line:
    f = line.readlines()
    for i in f:
        count += 1 
        f[count] = "https://www.youtube.com/watch?v=" + f[count]
        list_of_url.append(f[count])
    line.close()

with open(f'playlist-{NOME}.txt', 'w') as txt_file:
    for line in list_of_url:
        txt_file.write("".join(line))

remove(f'temp-{NOME}.txt')
system("cls")
print(f'playing: playlist-{NOME}.txt')
system(f"mpv --no-video -playlist=playlist-{NOME}.txt")