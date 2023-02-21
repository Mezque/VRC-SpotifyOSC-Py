#!/bin/bash

echo "Enter the Spotify client ID: "
read client_id
sudo sh -c 'echo "SPOTIPY_CLIENT_ID='$client_id'" >> /etc/launchd.conf'

echo "Enter the Spotify secret ID: "
read client_secret
sudo sh -c 'echo "SPOTIPY_CLIENT_SECRET='$client_secret'" >> /etc/launchd.conf'

echo "Persistent environment variables set."
