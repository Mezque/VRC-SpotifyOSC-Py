#!/bin/bash

echo "Enter the Spotify client ID: "
read client_id
export SPOTIPY_CLIENT_ID="$client_id"
echo "SPOTIPY_CLIENT_ID set to: $client_id"

echo "Enter the Spotify secret ID: "
read client_secret
export SPOTIPY_CLIENT_SECRET="$client_secret"
echo "SPOTIPY_CLIENT_SECRET set to: $client_secret"
