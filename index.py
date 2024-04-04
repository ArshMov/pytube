from pytube import YouTube

yt = YouTube('Link')

yt.streams.filter(mime_type="video/mp4", resolution="360p", progressive=True).first().download()

print(yt.title)
print(yt.description)
print(yt.author)
print(yt.views)
print(yt.thumbnail_url)
