from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=T0YV1YqaUEw&t=3s&ab_channel=BishopRobertBarron')

print(f"The title is {yt.title} and link to thumbnail is: {yt.thumbnail_url}")

stream = yt.streams.filter(only_audio=True)
stream.download()
