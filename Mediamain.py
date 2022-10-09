#Nicholas Pelletier, nwp28, This is the Main program that interacts with the user.
from MediaLibrary import *
#Adding Media items to the list
media=list()
media.append(Song("Baby come back","7/10","Player","Player"))
media.append(Song("Speedcore 300","7/10","Hypernite Industries","Unknown"))
media.append(Song("Ghost","10/10","Camellia","Cyphisonia"))
media.append(Song("World.execute(me)","8/10","Mili","Miracle Milk"))
media.append(Movie("Avengers EndGame","9/10","Anthony/Joe Russo","182 minutes"))
media.append(Movie("John Cena's Return","6/10","John Cena","120 minutes"))
media.append(Movie("Fast and Furious 7","8/10","James Won","140 minutes"))
media.append(Movie("Kimi no na wa","10/10","Makoto Shinkai","112 minutes"))
media.append(Picture("Mona Lisa","10/10",300))
media.append(Picture("Mom","7/10",250))
media.append(Picture("Picasso's Randomness","6/10",201))
media.append(Picture("Meme","9/10",500))

#Method used for Finding a Specific Song/Movie/Picture
def Find(name,Instance):
    for i in range(0,len(media)):
            if isinstance(media[i],Instance):
                if(media[i].getName().lower()==name.lower()):
                    return media[i].Play()
            if(i==len(media)-1):
                print("Error:", Instance, "not in Media Library")
                return
#Method used for displaying only Songs/only Movies/only Pictures
def displaySpecific(Instance):
    for i in range(0,len(media)):
            if isinstance(media[i],Instance):
                print(media[i])
                print()
    return

#main function
if __name__ == "__main__":
    Quit=False #setting up the quit ability for the user
    while not Quit: #loop until quit is changed
        print("Welcome to the Menu, You can:\nDisplay all items in the Media Library: dmedia\nDisplay only the Song objects: dsong\nDisplay only the Movie objects: dmovie\nDisplay only the Picture objects: dpicture\nPlay a Song: psong\nPlay a Movie: pmovie\nDisplay a Picture: dpic\nYou can quit the program by typing q")
        Answer=input() #whatever they input is put in here, if it's not one of the if statements then it just goes through the loop again (displays menu again)
        print()
        #displays all Media
        if Answer=="dmedia": 
            for i in range(0,len(media)):
                print(media[i])
                print()
        #Displays only Movie's
        elif Answer=="dmovie":
            displaySpecific(Movie)
        #Displays only Songs
        elif Answer=="dsong":
            displaySpecific(Song)
        #Displays only Pictures
        elif Answer=="dpicture":
            displaySpecific(Picture)
        #Plays the song requested if it is there
        elif Answer=="psong":
            songname=input("Enter the name of the Song:")
            Find(songname,Song)
        #Plays the movie requested if it is there
        elif Answer=="pmovie":
            moviename=input("Enter the name of the Movie:")
            Find(moviename,Movie)
        #Displays the picture requested if it is there
        elif Answer=="dpic":
            picname=input("Enter the name of the Picture:")
            Find(picname,Picture)
        #User Quits Loop
        elif Answer=="q":
            Quit=True
