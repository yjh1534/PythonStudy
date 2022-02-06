import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="17e9a403e3644cf8b5e6bdb0df353aa6",
        client_secret="74efdee84750445d98bc9664997a683f",
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]