import assemblyai as aai
import os
from decouple import config

# Replace with your Assembly AI API key
aai.settings.api_key = config('ASSEMBLYAI_API_KEY')

def transcribe_audio_and_save_to_txt(audio_file_path, output_txt_file):
    # Create a Transcriber object
    transcriber = aai.Transcriber()

    # Check if the file exists
    if not os.path.exists(audio_file_path):
        print(f"Error: The file {audio_file_path} does not exist.")
        return

    # Transcribe the local audio file
    transcript = transcriber.transcribe(audio_file_path)

    if transcript.status == aai.TranscriptStatus.error:
        print(f"Transcription failed: {transcript.error}")
    else:
        # Write the transcription to a .txt file
        with open(output_txt_file, "w") as f:
            f.write(transcript.text)
        print(f"Transcription saved to {output_txt_file}")

# Prompt the user for the input audio file and output file name
audio_file_name = input("Enter the name of the audio file (e.g., 'audio/file.mp3'): ")
output_txt_file = input("Enter the name for the output transcription file (e.g., 'transcription.txt'): ")

# Ensure the input audio file is in the 'audio' folder
audio_file_path = f"./audio/{audio_file_name}"

# Transcribe the audio and save the result
transcribe_audio_and_save_to_txt(audio_file_path, output_txt_file)
