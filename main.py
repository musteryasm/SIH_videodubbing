import moviepy.editor as mp
import speech_recognition as sr
from googletrans import Translator

def convert_video_to_audio(video_path):
    clip = mp.VideoFileClip(video_path)
    audio_path = "audio.wav"
    clip.audio.write_audiofile(audio_path)
    return audio_path

def convert_audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        return text

def save_text_to_file(text, file_path):
    with open(file_path, 'w') as file:
        file.write(text)

def translate_to_marathi(english_text):
    translator = Translator()
    marathi_text = translator.translate(english_text, src='en', dest='mr').text
    return marathi_text

video_path = "/content/sample_data/sample.mp4"
txt_file_path = "output.txt"
output2_txt_file_path = "output2.txt"

audio_path = convert_video_to_audio(video_path)

text = convert_audio_to_text(audio_path)

save_text_to_file(text, txt_file_path)
marathi_text = translate_to_marathi(text)
save_text_to_file(marathi_text, output2_txt_file_path)

print(f'Text saved to {txt_file_path} and {output2_txt_file_path}')
