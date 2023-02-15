import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pythonosc.udp_client import SimpleUDPClient
import time
import configparser
import os.path
import threading

CLIENT = SimpleUDPClient("127.0.0.1", 9000)
CONFIG = configparser.ConfigParser()
Song1 = ["", True]
SP = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="", #put your client id here or run Set_Environment_Variables inside the folder with the same name.
                                               client_secret="", #put your client secret here or run Set_Environment_Variables inside the folder with the same name.
                                               redirect_uri="http://localhost:8888/spotify/callback",
                                               scope="user-read-currently-playing user-read-playback-state")) # You can find out more about what this means here, https://developer.spotify.com/documentation/general/guides/authorization/scopes/ basically it allows the program to read your current playing song, but no other control over your spotify account.
'''
1: Go to https://developer.spotify.com/dashboard/ and log in with your Spotify account and then create yourself a new app. 
2: You will be redirected to the dashboard of your app, copy the client id and client secret (press Show Client Secret) and paste them in the apove string feilds as discribed.
!NOTE!: Always store the client secret key securely; never reveal it publicly! If you suspect that the secret key has been compromised, regenerate it immediately by clicking the ROTATE button on the app overview page!!!
It is time to configure our app. Click on Edit Settings and find "Redirect URLs", type http://localhost:8888/spotify/callback in the feild.
Refrence: https://developer.spotify.com/documentation/general/guides/authorization/app-settings/
'''

def DisplayName():
    return SP.current_user()['display_name'] #returns the display name of the user.

def get_current_song_and_artist():
    CurSong = SP.current_user_playing_track()
    CurPlayback = SP.current_playback()
    if CurSong is None:
        print("No song is currently playing")
        return None, None, None, None
    else:
        Song = CurSong["item"]["name"]
        Artist = CurSong['item']['artists'][0]['name']
        Length = CurSong['item']["duration_ms"]
        Volume = CurPlayback['device']['volume_percent']
        minutes, seconds = divmod(int(Length) // 1000, 60)
        song_length = f"{minutes}:{seconds:02d}"

        Position = CurSong["progress_ms"]
        minutes, seconds = divmod(int(Position) // 1000, 60)
        song_pos = f"{minutes}:{seconds:02d}"

        return (Song, Artist, Volume ,song_length, song_pos)

def Prefs():
    exist = os.path.exists("Settings/settings.ini")
    if exist == True:
        CONFIG.read('Settings/settings.ini')
    else:
        print("Prefs file doesn't exist, creating now.")
        try:
            os.mkdir("Settings")
        except(FileExistsError): #i hate windows
            print("directory already exist")
        writeNewFile = open('Settings/settings.ini', 'w')
        writeNewFile.write('[Preferences]\nKeepSendingOSC=true')
        writeNewFile.close

stop_timer=False
def send_message():
    song, artist, volume ,song_lenth, song_pos = get_current_song_and_artist()
    if (volume == 0):
        volume = f"🔇{volume}"
    elif(volume <= 50):
        volume = f"🔉{volume}"
    else:
        volume = f"🔊{volume}"
    Song1[0] = f"Now playing {song} by {artist} {song_pos}/{song_lenth} {volume}"
    CLIENT.send_message("/chatbox/input",Song1) 
    if not stop_timer:
        thread = threading.Timer(5, send_message)
        thread.start()

def loop():
    print("[DEBUG] Enter loop function")
    prev_song = ""
    song, artist, volume, song_lenth, song_pos = get_current_song_and_artist()
    try:
        KeepSendingOSC = CONFIG.getboolean('Preferences', 'KeepSendingOSC')
    except:
        Prefs()
        KeepSendingOSC = CONFIG.getboolean('Preferences', 'KeepSendingOSC')
    if KeepSendingOSC:
        if song != prev_song:
            print("- Currently Playing:", song, "by", artist)
            prev_song = song
        thread2 = threading.Timer(5, send_message)
        thread2.start()
    else:
        if song != prev_song:
            Song1[0] = f"Now playing {song} by {artist}"
            CLIENT.send_message("/chatbox/input",Song1) 
            time.sleep(2)
            loop()

def main():
    song,artist,volume,song_lenth,song_pos = get_current_song_and_artist()
    print("--------------------------------")
    print("- Starting Spotify API Python  -")
    print("- Current User:", DisplayName())
    print("- Currently Playing:", song, 'by', artist)
    print("--------------------------------")
    Prefs()
    thread = threading.Thread(target=loop)
    thread.start()

if __name__ == "__main__":
    main()