import os
from pytube import YouTube
import pytube.exceptions as pytube_exceptions
import assemblyai as aai
from decouple import config

# Replace with your Assembly AI API key
aai.settings.api_key = config('ASSEMBLYAI_API_KEY')


def download_audio_from_youtube(youtube_url, output_path):
    try:
        # Use Pytube to download the audio from YouTube
        yt = YouTube(youtube_url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        if not audio_stream:
            raise Exception("No audio streams available for this video.")
        
        audio_file = audio_stream.download(output_path=output_path)
        return audio_file
    
    except pytube_exceptions.VideoUnavailable:
        print(f"The video {youtube_url} is unavailable.")
    except pytube_exceptions.AgeRestrictedError:
        print("The video is age-restricted and cannot be downloaded.")
    except pytube_exceptions.PytubeError as e:
        print(f"An error occurred while downloading the video: {e}")


def transcribe_audio_with_assemblyai(audio_file_path):
    # Upload the local audio file to Assembly AI for transcription
    transcriber = aai.Transcriber()
    config = aai.TranscriptionConfig(auto_highlights=True)
    transcript = transcriber.transcribe(audio_file_path, config=config)

    # Print highlights from the transcription
    for result in transcript.auto_highlights.results:
        print(f"Highlight: {result.text}, Count: {result.count}, Rank: {result.rank}")

# Step 1: Download the YouTube audio
youtube_url = "https://www.youtube.com/watch?v=qp0HIF3SfI4&t=31s&ab_channel=TED"  # Replace with your YouTube video URL
output_path = "./audio"  # Directory to save the audio file
audio_file = download_audio_from_youtube(youtube_url, output_path)

# Step 2: Transcribe the audio file
transcribe_audio_with_assemblyai(audio_file)
