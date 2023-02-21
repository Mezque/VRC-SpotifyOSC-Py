@echo off
set /p client_id=Enter the Spotify client ID: 
setx SPOTIPY_CLIENT_ID "%client_id%"
echo SPOTIPY_CLIENT_ID set to: %client_id%
set /p client_secret=Enter the Spotify secret ID: 
setx SPOTIPY_CLIENT_SECRET "%client_secret%"
echo SPOTIPY_CLIENT_SECRET set to: %client_secret%