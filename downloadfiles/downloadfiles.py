import pafy
text = input("would you like to download the video or the audio?")
url = "https://www.youtube.com/watch?v=ZZ5LpwO-An4&t=21s"

if text == ('video'):
    print ('please wait')
    video = pafy.new(url)
    best = video.getbest()
    best.download(quiet=False)


if text ==('audio'):
    print ('please wait')
    audio = pafy.new(url)
    best = audio.getbest()
    best.download(quiet=False)
else:
    print('no')



print("download complete")

