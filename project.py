import numpy as np
from pydub import AudioSegment
from pydub.playback import play


# Define the list of file paths for the songs
playlist = [
   "/home/keshavardhan/Downloads/playlist/IMG_0568.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0569.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0572.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0574.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0575.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0566.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0565.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0563.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0562.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0561.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0560.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0559.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0558.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0557.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0556.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0555.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0553.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0567.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0570.mp3",
   "/home/keshavardhan/Downloads/playlist/IMG_0571.mp3"
  
   # Add file paths for the rest of the songs
]

# Load the songs
songs =[AudioSegment.from_file(file) for file in playlist]

# Shuffle the songs
np.random.shuffle(songs)


 # Initialize playlist index and repeat flag
index = 0
repeat = False

# Playlist loop
while True:
    # Get the current song
    song = songs[index]
    
    # Print the current song
    print("Now playing:", song)
    
    play(song)
    
    # Ask for user input
    user_input = input("Press Enter to continue or 'r' to replay: ")
    
    # Check if the user wants to replay the song
    if user_input == 'r':
        repeat = True
    else:
        repeat = False
    
    # Play the song again if repeat flag is True
    if repeat:
        continue
    
    # Move to the next song
    index += 1
    
    # Restart from the beginning if the end of the playlist is reached
    if index == len(songs):
        index = 0
