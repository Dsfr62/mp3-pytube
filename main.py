import pytube

# modify the list below
urls = [
    "https://www.youtube.com/watch?v=3CgXIfmxRJs", 
]

for url in urls:
    yt = pytube.YouTube(url)
    streams = yt.streams.filter(only_audio=True, file_extension="mp4")
    stream = streams.get_by_itag(140)
    stream.download(output_path="output/")
    print(f"${yt.title} downloaded with success!\n")

print("\nfinished!\n")