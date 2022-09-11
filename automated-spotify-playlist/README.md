# Automated Spotify Playlist
A Python Script to create a Spotify playlist of songs on a particular date on the Billboard Hot 100 website using the Spotipy library and by scraping the Billboard Hot 100 website using Beautiful Soup.

## Tools
- [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/)
- [Spotify for Developers](https://developer.spotify.com/)
- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)

## Screenshots
![Screenshot cmd](https://user-images.githubusercontent.com/87208681/150687233-20bc0842-57cd-428a-9107-334b65ec215f.png)
![Screenshot Spotify](https://user-images.githubusercontent.com/87208681/150687240-a143a399-ac38-4079-b1f6-811e06567603.png)

## Environment Variables
To run this project, you will need to add the following environment variables to your .env file

`SPOTIFY_CLIENT_ID` `SPOTIFY_CLIENT_SECRET`

Refer to the [env template](https://github.com/sejalabrol/automated-spotify-playlist/blob/main/.env.template)

## Run Locally
Clone the project
```bash
  git clone https://github.com/sejalabrol/automated-spotify-playlist
```
Go to the project directory
```bash
  cd automated-spotify-playlist
```
Create a .env file and enter environment variables
```bash
  cp .env.template .env
```
[Create a virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) (optional but recommended) 
```bash
  python -m venv venv
  source venv/Scripts/activate
```
Install dependencies
```bash
  pip install -r requirements.txt
```
Run the project
```bash
  python main.py
```
