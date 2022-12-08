import spotipy 
from spotipy.oauth2 import SpotifyOAuth

Spot_URI: str = 'http://localhost:8888/spotify/callback' 

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="", #put your client id here
                                               client_secret="", #put your client secret here
                                               redirect_uri="http://localhost:8888/spotify/callback",
                                               scope="user-read-currently-playing")) # You can find out more about what this means here, https://developer.spotify.com/documentation/general/guides/authorization/scopes/ basically it allows the program to read your current playing song, but no other control over your spotify account.

# 1: Go to https://developer.spotify.com/dashboard/ and log in with your Spotify account and then create yourself a new app. 
# 2: You will be redirected to the dashboard of your app, copy the client id and client secret (press Show Client Secret) and paste them in the apove string feilds as discribed.
# !NOTE!: Always store the client secret key securely; never reveal it publicly! If you suspect that the secret key has been compromised, regenerate it immediately by clicking the ROTATE button on the app overview page!!!
# It is time to configure our app. Click on Edit Settings and find "Redirect URLs", type http://localhost:8888/spotify/callback in the feild.
# Refrence: https://developer.spotify.com/documentation/general/guides/authorization/app-settings/ 

def DisplayName():
    return sp.current_user()['display_name'] #returns the display name of the user.
def CurrentSong():
    CurSong = sp.current_user_playing_track() 
    if CurSong is None:
        print("No song is currently playing")
    else: 
        Song = CurSong["item"]["name"]
        #Artist = CurSong['item']['artists'][0]['name'] # https://stackoverflow.com/a/63907495 the [0]['name'] part fixed it :)
        print('\x1B[38;5;211m[DEBUG] \x1B[0mCurrent song is', Song) #used to test if filtering item name was working
        # print('\x1B[38;5;211m[DEBUG] \x1B[0mCurrent artist is', Artist)
        return Song 
def CurrentArtist():
    CurSong = sp.current_user_playing_track() 
    if CurSong is None:
        print("No song is currently playing")
    else: 
        Artist = CurSong['item']['artists'][0]['name']
        print('\x1B[38;5;211m[DEBUG] \x1B[0mCurrent artist is', Artist)
        return Artist

def main():
    print("--------------------------------")
    print("- Starting Spotify API Python  -")
    print("- Current User:", DisplayName())
    print("- Currently Playing:", CurrentSong(), 'by', CurrentArtist())
    print("--------------------------------")
                                     
       
main()
if __name__ == "__main__":
    main()