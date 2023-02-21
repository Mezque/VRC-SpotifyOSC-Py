#!/bin/bash

echo "Enter the Spotify client ID: "
read client_id
echo "SPOTIPY_CLIENT_ID=$client_id" | sudo tee -a /etc/environment

echo "Enter the Spotify secret ID: "
read client_secret
echo "SPOTIPY_CLIENT_SECRET=$client_secret" | sudo tee -a /etc/environment

echo "Persistant Environment variables set."