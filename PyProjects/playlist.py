print("~~~PLAYLIST MAKER~~~")
name=input("Enter yoour name:-")
PLAYLIST=input("Enter the name of the playlist:-")
pl=[]
favourite=[]
FOVartis={}

def addsong(song):
    if song in pl:
        print("Already in the playlist")
    else:
        pl.append(song)
        print("Song entered")
        
def displayplaylist():
    print("Songs in the playlist are:-",pl)
    
def deletesong(song):
    if song in pl:
        pl.remove(song)
        print("Song deleted successfully")
    else:
        print("The song is not present in the playlist")
        
def addfavourite(song):
    if song in favourite:
        ("Song already in favourite")
    else:
        favourite.append(song)
        
def Displayfavourite():
    print("Songs in the favourite playlist are:-",favourite)
    
def deletefromfavourite(song):
    if song in favourite:
        favourite.remove(song)
        print("song deleted successfully")
    else:
        print("The song is not found in your favourites list.")
        
def Favartist(artist,song):
    if artist in FOVartis:
        print("Artist already in the list")
    else:
        FOVartis[artist]=song
        print("Artist added succesfully")
        
def  displayfavartist():
    print("The Artist and their favourite song is:-",FOVartis)
        

while True:
    print("\n1.Add a Song to Playlist\n2.Display Playlist\n3.Delete a song\n4.ADD favourite\n5.display favourite")
    print("6.Delete from playlist\n7.ADD favourite artist\n8.Display favourite artist\n9.Exit")
    choice=int(input("Enter you choice:-"))
    if choice==1:
        song=input("Enter the song to add in the playtlist:-")
        addsong(song)
    elif choice==2:
        displayplaylist()
    elif choice==3:
        song=input("Enter the song to delete from the playlist:-")
        deletesong(song)
    elif choice==4:
        song=input("Enter the song to ADD favourite to the playlist:-")
        addfavourite(song)
    elif choice==5:
        Displayfavourite()
    elif choice==6:
        song=input("Enter the song to delete from the Favouriter playlist:-")
        deletefromfavourite(song)
    elif choice==7:
        artist=input("Enter the Artist name:-")
        song=input("Enter the favourite song of the artist:-")
        Favartist(artist,song)
    elif choice==8:
        displayfavartist()
    elif choice==9:
        break
    else:
        print("Enter the correct choice..........")