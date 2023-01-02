<h1 align="center">
  VRC-SpotifyOSC-Py
</h1>

<h4 align="center">A simple Spotify OSC chatbox for VRChat using SpotifyAPI.</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#spotify-dev-portal">Dev Portal Instructions</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

## Key Features
* Customizable
  - Able to change the chatbox text formatting very easy! Just change the formatting on</br> `Song1[0] = f"Now playing {cur_song} by {cur_artist} {time2}/{time1}"` (time display/OSC always mode)</br> or `Song1[0] = f"Now playing {cur_song} by {cur_artist}"` (send once per song mode).
* Uses API
  - Slightly more optimized than reading the Spotify program name, though I do believe python will end up using slightly more ram then some other solutions, less cpu usage.
  - Able to display the current song playing on any device due to using API to retrieve playing information.
* Cross platform
  - Windows, macOS and Linux ready.
* Timestamp and song length display. (updated aprox every 5 seconds)</br>
  <img width="364" alt="image" src="https://user-images.githubusercontent.com/31026406/209856558-0795712f-80d3-4e2c-9e42-25851255b0f9.png">
* Or alternatively only send playing song once per each song, checked for song change on a 2 second interval. </br>
  <img width="270" alt="image" src="https://user-images.githubusercontent.com/31026406/209856924-3bc72e83-9d65-415f-b43f-cf0f6d2d306c.png">
  
> **Note**
>: Usage of the Spotify API requires a premium account; this will not work with free accounts.
## How To Use

To clone and run this application, you'll need [Python](https://www.python.org/downloads/) and [git](https://gitforwindows.org/) (if on windows) From your command line:

```bash
# Clone this repository
$ git clone https://github.com/Mezque/VRC-Music-Py

# Go into the repository
$ cd VRC-Music-Py/Py/Spotify

# Install dependencies
$ pip install -r requirements.txt

# Run the app
$ py Spotify.py
```
Open Spotify.py and set `client_id` and `client_secret` to their respected value on your created application from the [Spotify Dev Portal](https://developer.spotify.com/dashboard/)
> **Note**
> If you're using Windows, there is included bat files to do step 3 and 4. </br>
> (if you choose to download below you don't need to clone the repositroy or install git) </br>
> If Python is failing to run properly on Windows install it from the [Microsoft Store](https://apps.microsoft.com/store/detail/python-311/9NRWMJP3717K?hl=en-us&gl=us) instead of the python website for an easy fix; this is a Windows problem to do with how python is set up under your system variables. </br>

## Download

You can [download](https://github.com/Mezque/VRC-Music-Py/releases/download/download/Spotify.zip) the latest version as well if you don't want to use git to clone the repository. It's the same thing just slower for people less experienced with usage of git through a CLI.

## Spotify Dev Portal
How to set up the application,
1. Head to the [Spotify Dev Portal](https://developer.spotify.com/dashboard/) and log into your account. 
2. Press the green button on the top of the right side that says "Create an app", the name doesn't matter and a description is not required.
3. Open up the newly created app and copy your Client ID and set this value in the `Spotify.py` file. Do the same thing for the Client Secret after pressing Show Client Secret.
4. Press the green button around the same location where the create app button was on the previous menu and under the section "Redirect URIs" put `http://localhost:8888/spotify/callback`
## Credits

This software uses the following open source packages:

- [Python-Osc](https://pypi.org/project/python-osc/)
- [Spotipy](https://pypi.org/project/spotipy/)
## License

MIT

---
