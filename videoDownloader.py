from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

#Title of the Video
print("Title: ",yt.title)
#Number of Views
print("Views: ", yt.views)
#Description of Video
print("Description: \n", yt.description)
#Ratings of Video
print("Ratings: ",yt.rating)
#Streams of Video
print("Streams", yt.streams.filter(progressive=True))

youtubeSave = yt.streams.get_highest_resolution()
print("Video Downlaoding...")
youtubeSave.download('F:\Video_Exp')
print("Video Downlaoded!")