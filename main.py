from pytube import YouTube

input = input("Enter the link of the video: ")
url = YouTube(input)

video = url.streams.filter(progressive=True).order_by('resolution').desc().first()
video.download()

print("Video downloaded successfully")
