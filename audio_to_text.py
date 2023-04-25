import openai
# from pydub import AudioSegment
import os
openai.api_key = "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"

MP3_file = "audio\cutVer.mp3"
file_name = os.path.basename(MP3_file)
file_name = (file_name.split('.'))[0]

audio_file= open(MP3_file, "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)

with open(f'script/{file_name}.txt', 'w') as f:
    f.write(f"{transcript.text} \n")
print("script generated")

with open("script\cutVer.txt", 'r') as f:
    script_text = f.read()

chat = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant that can help me summerize the content of a podcast script."},
        {"role": "user", "content": f"Summerize the content of the podcast, list the summary in point form, keep it detailed and clear.This is the script of the podcast: {script_text}" }

    ]
)
print(chat.choices[1].message.content)
# audio = AudioSegment.from_mp3(MP3_file)

# # PyDub handles time in milliseconds
# ten_minutes = 10 * 60 * 1000

# first_10_minutes = audio[:ten_minutes]

# first_10_minutes.export("result_10mins", format="mp3")