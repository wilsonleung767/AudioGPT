# import openai
import os
from Split_audio import split_audio
# openai.api_key = "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"
def audio_to_text(mp3_file):
# mp3_file = 'audio/podcast/podcast.mp3'
    split_audio(mp3_file,10)
    file = os.path.basename(mp3_file)
    file_name = os.path.splitext(file)[0]

    # file_name = 'podcast'
    audio_folder = f'audio/{file_name}'
    audio_files = os.listdir(audio_folder)
    print(audio_files)
    for i , file in enumerate(audio_files):
        # check if the file is an audio file
        if file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".ogg"):
            audio_for_translation = open(f'{audio_folder}/{file}', "rb")
            # transcript = openai.Audio.translate("whisper-1", file)
        # Create a new folder when there is no existing folder
        
        script_folder_path = f'script/{file_name}'
        file_inside_folder = os.path.basename(file)
        file_inside_name = os.path.splitext(file_inside_folder)[0]
        if not os.path.exists(script_folder_path):
            os.makedirs(script_folder_path)
        with open(f'{script_folder_path}/{file_inside_name}_S{i}.txt', 'w') as f:
            f.write(f"yes \n")
        print(f"script {i} generated")
audio_to_text('audio/podcast.mp3')        
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