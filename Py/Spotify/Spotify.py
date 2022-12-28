import spotipy 
from spotipy.oauth2 import SpotifyOAuth
from pythonosc.udp_client import SimpleUDPClient
import time
import configparser
import os.path
import threading

client = SimpleUDPClient("127.0.0.1", 9000)
config = configparser.ConfigParser()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="", #put your client id here
                                               client_secret="", #put your client secret here
                                               redirect_uri="http://localhost:8888/spotify/callback",
                                               scope="user-read-currently-playing")) # You can find out more about what this means here, https://developer.spotify.com/documentation/general/guides/authorization/scopes/ basically it allows the program to read your current playing song, but no other control over your spotify account.
Song1 = ["", True]
# 1: Go to https://developer.spotify.com/dashboard/ and log in with your Spotify account and then create yourself a new app. 
# 2: You will be redirected to the dashboard of your app, copy the client id and client secret (press Show Client Secret) and paste them in the apove string feilds as discribed.
# !NOTE!: Always store the client secret key securely; never reveal it publicly! If you suspect that the secret key has been compromised, regenerate it immediately by clicking the ROTATE button on the app overview page!!!
# It is time to configure our app. Click on Edit Settings and find "Redirect URLs", type http://localhost:8888/spotify/callback in the feild.
# Refrence: https://developer.spotify.com/documentation/general/guides/authorization/app-settings/ 

def TimeConversion(time):
    seconds, time = divmod(time, 1000)
    minutes, seconds = divmod(seconds, 60)
    return seconds, minutes

def DisplayName():
    return sp.current_user()['display_name'] #returns the display name of the user.
     
def get_current_song_and_artist():
    CurSong = sp.current_user_playing_track()
    if CurSong is None:
        print("No song is currently playing")
        return None, None
    else:
        Song = CurSong["item"]["name"]

        Artist = CurSong['item']['artists'][0]['name']

        Length = CurSong['item']["duration_ms"]
        sec,min = TimeConversion(int(Length))
        song_lenth=("{0}:{1}".format(min,sec))

        Position = CurSong["progress_ms"]
        sec,min = TimeConversion(int(Position))
        song_pos=("{0}:{1}".format(min,sec))

        return (Song, Artist, song_lenth, song_pos)

def Prefs():
    exist = os.path.exists("Settings/settings.ini")
    if exist == True:
        config.read('Settings/settings.ini')
    else:
        print("Prefs file doesn't exist, creating now.")
        os.mkdir("Settings")
        writeNewFile = open('Settings/settings.ini', 'w')
        writeNewFile.write('[Preferences]\nKeepSendingOSC=true')
        writeNewFile.close

def loop():
    prev_song = ""
    while True:
        song,artist,song_lenth,song_pos = get_current_song_and_artist()
        cur_song = song
        cur_artist = artist
        KeepSendingOSC = config.getboolean('Preferences', 'KeepSendingOSC')
        if KeepSendingOSC == True:
            if cur_song != prev_song:
                print("- Currently Playing:", cur_song, "by", cur_artist)
                prev_song = cur_song
            time1 = song_lenth
            time2 = song_pos
            Song1[0] = f"Now playing {cur_song} by {cur_artist} {time2}/{time1}"
            client.send_message("/chatbox/input",Song1) #want to clean this up with threading but it was working not as expected, will look more into later after getting the feature out in the first place.
        time.sleep(2)

        if cur_song != prev_song:
            print("- Currently Playing:", cur_song, "by", cur_artist)
            Song1[0] = f"Now playing {cur_song} by {cur_artist}"
            client.send_message("/chatbox/input",Song1) #/chatbox/input 
            prev_song = cur_song
        time.sleep(2) # pause for 2 seconds before checking again

def main():
    song,artist,song_lenth,song_pos = get_current_song_and_artist()
    print("--------------------------------")
    print("- Starting Spotify API Python  -")
    print("- Current User:", DisplayName())
    print("- Currently Playing:", song, 'by', artist)
    print("--------------------------------")
    Prefs()
    thread = threading.Thread(target=loop)
    thread.start()
    
main()
if __name__ == "__main__":
    main()