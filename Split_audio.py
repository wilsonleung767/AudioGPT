from pydub import AudioSegment
import os
import math

def split_audio( mp3_file, minute_interval):
    file_name = os.path.basename(mp3_file)
    filename = os.path.splitext(file_name)[0]
    audio = AudioSegment.from_mp3(mp3_file)

    # PyDub handles time in milliseconds
    minute_interval = minute_interval * 60 * 1000
    segment_10_mins = audio[:minute_interval]
    # Calculate the number of segments
    num_segments = math.ceil(len(audio)/minute_interval)
    # Split the audio into segments
    segments = [audio[i*minute_interval:(i+1)*minute_interval] for i in range(num_segments)]

    

    # Create a new folder when there is no existing folder
    folder_path = f'audio/{filename}'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Generating splited audio
    for i, segment in enumerate(segments):
        segment.export(f"{folder_path}/{filename}_A{i}.mp3", format="mp3")

    print("Audio splitted")

