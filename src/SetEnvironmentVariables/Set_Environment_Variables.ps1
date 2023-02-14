$client_id = Read-Host "Enter the Spotify client ID: "
[Environment]::SetEnvironmentVariable("SPOTIPY_CLIENT_ID", $client_id, "User")
Write-Host "SPOTIPY_CLIENT_ID set to: $client_id"

$client_secret = Read-Host "Enter the Spotify secret ID: "
[Environment]::SetEnvironmentVariable("SPOTIPY_CLIENT_SECRET", $client_secret, "User")
Write-Host "SPOTIPY_CLIENT_SECRET set to: $client_secret"