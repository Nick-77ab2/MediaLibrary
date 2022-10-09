#Nicholas Pelletier, nwp28, This is the backend program that runs the media class and all of its child classes.
import abc
from fractions import Fraction
class Media(metaclass = abc.ABCMeta):
    def __init__(self,mediatype='',name='',rating=''):
        self.__rating=rating
        self.__mediatype=mediatype
        self.__name=name
    
    #getters
    def getRating(self):
        return self.__rating
    
    def getName(self):
        return self.__name

    def getType(self):
        return self.__mediatype
    
    #setters
    def setRating(self,rating):
        self.rating=rating
        return
    
    def setName(self,name):
        self.__name=name
        return
    
    def setType(self,mediatype):
        self.__mediatype=mediatype
        return
    #overloading str
    def __repr__(self):
        mediastr="Name:" + ' ' + self.__name + "\nType:" +' ' + self.__mediatype + "\nRating" +' ' + self.__rating
        return mediastr

class Movie(Media):
    def __init__(self,name='',rating='',director='',runningTime=''):
        super().__init__('Movie',name,rating)
        self.director=director
        self.runningTime=runningTime
    
    #Getters
    def getDirector(self):
        return self.director
    
    def getrunningTime(self):
        return self.runningTime

    #Setters
    def setDirector(self,director):
        self.director=director
        return
    
    def setRunningTime(self,runningTime):
        self.runningTime=runningTime
        return
    #other methods    
    def Play(self):
        print(self.getName(),"playing now!")
        print()
        return
    #overloading str
    def __repr__(self):
        moviestr=super().__repr__() + "\nDirector:" + ' ' +self.director + "\nRunning Time:" + ' ' +self.runningTime
        return moviestr

class Song(Media):
    def __init__(self,name='',rating='',Artist='',Album=''):
        super().__init__('Song',name,rating)
        self.Artist=Artist
        self.Album=Album
    
    #Getters
    def getArtist(self):
        return self.Artist
    
    def getAlbum(self):
        return self.Album

    #Setters
    def setArtist(self,Artist):
        self.Artist=Artist
        return
    
    def setAlbum(self,Album):
        self.Album=Album
        return
    #other methods    
    def Play(self):
        print(self.getName(),"by",self.getArtist(),"playing now!")
        print()
        return
    #overloading str
    def __repr__(self):
        songstr=super().__repr__() + "\nArtist:" + ' ' +self.Artist + "\nAlbum:" + ' ' +self.Album
        return songstr

class Picture(Media):
    def __init__(self,name='',rating='',resolution=200):
        super().__init__('Picture',name,rating)
        self.resolution=resolution
    
    #Getters
    def getResolution(self):
        return self.resolution
    
    #Setters
    def setResolution(self,resolution):
        if(resolution>=200):
            self.resolution=resolution
        else:
            resolution=int(input("Enter a new resolution greater than 200"))
            self.resolution=resolution
        return
    
    #other methods    
    def Play(self):
        print("Showing", self.getName())
        print()
        return
    #overloading str
    def __repr__(self):
        picstr=super().__repr__() +"\nResolution:" +' ' +str(self.resolution)
        return picstr
    