import argparse
import configparser
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import logging
from tenacity import retry, wait_fixed, stop_after_attempt, RetryError

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Read Spotify API credentials from the configuration file
config = configparser.ConfigParser()
config.read("config.ini")

SPOTIPY_CLIENT_ID = config["spotify"]["client_id"]
SPOTIPY_CLIENT_SECRET = config["spotify"]["client_secret"]
SPOTIPY_REDIRECT_URI = config["spotify"]["redirect_uri"]

# Add songs to the playlist in parts
chunk_size = 25

# Authentication - without user authorization
scope = 'playlist-modify-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope))


def read_song_names_from_excel(excel_file):
    df = pd.read_excel(excel_file, skiprows=1)  # Skip the first row as it is a header
    return df.iloc[:, 0].tolist()  # Read the first column as a list


def search_song_on_spotify(song_name):
    results = sp.search(q=song_name, type='track', limit=1)
    tracks = results['tracks']['items']
    if tracks:
        return tracks[0]['uri']
    else:
        return None


def create_spotify_playlist(name, description=''):
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user=user_id, name=name, public=False, description=description)
    return playlist['id']


@retry(wait=wait_fixed(2), stop=stop_after_attempt(5))
def add_songs_to_playlist(playlist_id, track_uris):
    sp.playlist_add_items(playlist_id, track_uris)


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Create a Spotify playlist from an Excel file of song names.")
    parser.add_argument("excel_file", type=str, help="Path to the Excel file containing song names.")
    parser.add_argument("playlist_name", type=str, help="Name of the new Spotify playlist.")
    parser.add_argument("--playlist_description", type=str, default='', help="Description of the new Spotify playlist (optional).")
    args = parser.parse_args()

    excel_file = args.excel_file
    playlist_name = args.playlist_name
    playlist_description = args.playlist_description

    # Read song names from the Excel file
    logger.info(f"Reading song names from {excel_file}")
    song_names = read_song_names_from_excel(excel_file)

    # Search for each song on Spotify and collect their URIs
    logger.info("Searching for songs on Spotify")
    track_uris = []
    for song_name in song_names:
        track_uri = search_song_on_spotify(song_name)
        if track_uri:
            logger.info(f"Found '{song_name}' on Spotify")
            track_uris.append(track_uri)
        else:
            logger.warning(f"Song '{song_name}' not found on Spotify and will be skipped")

    # Create a new Spotify playlist
    logger.info(f"Creating a new playlist: {playlist_name}")
    playlist_id = create_spotify_playlist(playlist_name, playlist_description)

    # Add songs to the playlist in parts
    total_songs = len(track_uris)
    num_chunks = (total_songs + chunk_size - 1) // chunk_size
    logger.info(f"Adding songs to the playlist in {num_chunks} parts")

    for i in range(num_chunks):
        start_idx = i * chunk_size
        end_idx = min((i + 1) * chunk_size, total_songs)
        chunk_uris = track_uris[start_idx:end_idx]
        if chunk_uris:
            try:
                logger.info(
                    f"Adding part {i + 1}/{num_chunks} ({len(chunk_uris)} songs) to the playlist '{playlist_name}'")
                add_songs_to_playlist(playlist_id, chunk_uris)
                logger.info(f"Added part {i + 1}/{num_chunks} to the playlist '{playlist_name}'")
            except RetryError:
                logger.error("Failed to add songs to the playlist after several attempts")
        else:
            logger.info("All songs have been added to the playlist")
            break


if __name__ == "__main__":
    main()