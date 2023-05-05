import openai
import os
import time
from Split_audio import split_audio
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("API_KEY")


def audio_to_text(mp3_file):
    start_time = time.time()
# mp3_file = 'audio/podcast/podcast.mp3'
    split_audio(mp3_file,10)
    file = os.path.basename(mp3_file)
    file_name = os.path.splitext(file)[0]

    # file_name = 'podcast'
    audio_folder = f'audio/splitted_audio/{file_name}'
    audio_files = os.listdir(audio_folder)
    
    for i , file in enumerate(audio_files):
        # check if the file is an audio file
        if file.endswith(".mp3") or file.endswith(".mp4") or file.endswith(".wav") or file.endswith(".ogg"):
            audio_for_translation = open(f"{audio_folder}/{file}", "rb")
            transcript = openai.Audio.translate("whisper-1", audio_for_translation)
        # Create a new folder when there is no existing folder
        script_folder_path = f'script/{file_name}'
        # file_inside_folder = os.path.basename(file)
        # file_inside_name = os.path.splitext(file_inside_folder)[0]

        if not os.path.exists(script_folder_path):
            os.makedirs(script_folder_path)

        with open(f'{script_folder_path}/{file_name}.txt', 'a') as f:
            f.write(f"{transcript.text}")
        print(f"Script Generated")

    end_time = time.time()
    print(f"Audio Translation Time Used: {end_time - start_time} s")

audio_to_text('audio/rid_acne_talk.mp3')        


# with open("script\cutVer.txt", 'r') as f:
#     script_text = f.read()

# chat = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "system", "content": "You are a helpful assistant that can help me summerize the content of a podcast script."},
#         {"role": "user", "content": f"Summerize the content of the podcast, list the summary in point form, keep it detailed and clear.This is the script of the podcast: {script_text}" }

#     ]
# )
# print(chat.choices[1].message.content)