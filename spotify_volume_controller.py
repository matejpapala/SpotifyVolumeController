import keyboard
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import ctypes
import sys


if sys.platform == "win32":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Spotify API credentials
SPOTIFY_CLIENT_ID = 'your_client_ID'
SPOTIFY_CLIENT_SECRET = 'your_client_secret'
SPOTIFY_REDIRECT_URI = 'http://localhost:8888'

# Spotify scope
SPOTIFY_SCOPE = 'user-modify-playback-state user-read-playback-state'

# Create a Spotify object with OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope=SPOTIFY_SCOPE
))

# Function to change the volume
def change_volume(volume_change):
    playback = sp.current_playback()
    if playback is not None and playback['device']['is_active']:
        current_volume = playback['device']['volume_percent']
        new_volume = max(0, min(100, current_volume + volume_change))
        sp.volume(new_volume)
        print(f"Volume changed to: {new_volume}%")

# Add hotkeys for volume control
keyboard.add_hotkey('page up', lambda: change_volume(5), suppress=True)
keyboard.add_hotkey('page down', lambda: change_volume(-5), suppress=True)

keyboard.wait()
