import datetime

playlist=[]
filename="playlists.txt"

def load_songs():
    file=open(filename,'r')
    for line in file:
        song=line.strip()
        song=line.split(',')
        playlist.append(song)
    file.close()
load_songs()

def save_playlist():
    file=open(filename,'w')
    for song in playlist:
        file.write(song[0]+ ", "+ song[1]+"," + "Date:"+ song[2]+ "\n")
    file.close()

def view_playlist():
    number=len(playlist)
    if number==0:
        print("Playlist is empty.")
    else:
        for i in range(number):
            song = playlist[i]
            print(i + 1,":", song[0], "-", song[1], "(", song[2], ")")

def remove_song(x):
    number=len(playlist)
    if 0<= x < number:
        remove_song = playlist.pop(x)
        print(remove_song[0],"Has been removed. ")
    else:
        print("invalid number. ")

def add_song(title, artist, date):
    playlist.append([title, artist, date])

def sort_playlist():
        playlist.sort(key=lambda song: song[2]) 

while 1:
    print("1. Add song. ")
    print("2. Remove song. ")
    print("3. Sort playlist. ")
    print("4. View playlists. ")
    print("5. Save and exit. ")

    choice = input("Enter which function to run:")

    if choice=='1':
        title=input("Enter the tile of your song: ")
        artist=input("Enter the name of your song's artists: ")
        date=str(datetime.datetime.now())
        add_song(title, artist, date)
        print(title , "has been added to the playlist. ")
    
    elif choice=='2':
        view_playlist()
        x=int(input("Song number to delete: ")) - 1
        remove_song(x)
    
    elif choice=='3':
        sort_playlist()
        view_playlist()
        print("Playlist has been sorted.")
        

    elif choice=='4':
        view_playlist()
        

    elif choice=='5':
        save_playlist()
        print("Playlist saved. Byee ;)")
        break
    
    else:
        print("Invalid choice. ")