# 🎵 Copy Apple Music Library to Spotify 🎶
Looking to make the switch from Apple Music to Spotify effortlessly? Want to copy your entire collection of Apple Music to Spotify in just a few clicks? 🚀 Our tool effortlessly transfers your extensive library makes your music migration smooth and hassle-free! 🎶

This project provides scripts to transfer songs from your Apple Music library (exported as an XML file) to a Spotify playlist. The process involves extracting song names from the Apple Music library XML file, storing them in an Excel file, and then using that Excel file to create a Spotify playlist with the corresponding songs.

Note - The Apple Music Library Should Be In XML Format

## 📋 Table of Contents
- [Features](#features)
- [Supported Platforms](#supportedplatforms)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Files](#files)
- [Contributing](#contributing)
- [Upcoming Updates](#upcoming-updates)

## ✨ Features
- 📄 Extracts song names from an Apple Music XML library file.
- 💾 Saves the extracted song names into an Excel file.
- 📋 Reads song names from the Excel file.
- 🔍 Searches for these songs on Spotify using the Spotipy library.
- ➕ Adds found songs to a new Spotify playlist.
- 📚 Handles large music libraries by adding songs in chunks.
- 🔄 Includes retry logic to handle network issues and API rate limits.

## 🖥️ Supported Platforms
![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white&style=for-the-badge)
![Mac](https://img.shields.io/badge/Mac-000000?logo=apple&logoColor=white&style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black&style=for-the-badge)

## 🛠️ Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/jadhavsharad/Apple-Music-to-Spotify.git
    cd Apple-Music-to-Spotify
    ```

2. Install the required libraries:
    ```bash
    pip install spotipy pandas openpyxl tenacity
    ```

## 🚀 Usage
1. Set up your Spotify Developer account and create an application to get your `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_REDIRECT_URI`. You can follow the steps [here](https://developer.spotify.com/documentation/general/guides/authorization/app-settings/).

2. Replace the placeholder values in the script with your actual Spotify API credentials and the path to your Apple Music XML library file.

3. Extract song names from your Apple Music XML library and save them to an Excel file:
    ```bash
    python extract_songs.py
    ```

4. Create a Spotify playlist from the Excel file:
    ```bash
    python create_spotify_playlist.py
    ```

## ⚙️ Configuration
Edit the following variables in the scripts as needed:

- `SPOTIPY_CLIENT_ID` : Your Spotify Client ID.
- `SPOTIPY_CLIENT_SECRET` : Your Spotify Client Secret.
- `SPOTIPY_REDIRECT_URI` : Your Spotify Redirect URI.
- `xml_file` : Path to your Apple Music XML library file.
- `excel_file` : Path to your output Excel file.

## 📦 Files
- `extract_songs.py`: Extracts song names from Apple Music XML library and saves them to an Excel file.
- `create_spotify_playlist.py`: Creates a Spotify playlist from the song names in the Excel file.

## 🤝 Contributing
We welcome contributions to enhance this project! If you have suggestions for improvements or find any issues, please feel free to open an issue or submit a pull request. Follow these steps to contribute:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
6. Feel free to check the [issues page](https://github.com/jadhavsharad/Apple-Music-to-Spotify/issues).

## 🔮 Upcoming Updates
- **GUI:** We are planning to add a graphical user interface to make the process even more user-friendly.

## 🙏 Acknowledgments
- [Spotipy](https://github.com/plamere/spotipy) for the Spotify Web API.
- [Pandas](https://pandas.pydata.org/) for data manipulation.
- [Tenacity](https://github.com/jd/tenacity) for retrying functions.

---

Made with ❤️ by [Sharad Jadhav](https://github.com/jadhavsharad)
