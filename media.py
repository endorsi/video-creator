# developed as a video creator

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.audio.AudioClip import concatenate_audioclips
from moviepy.video.fx.resize import resize

from moviepy.video.tools.drawing import circle

VideoFileClip.resize = resize
ImageClip.resize = resize

# resolution
w = 1024
h = 1024

size = w,h

# sources
video = VideoFileClip("D:\\upload\\video.mp4").subclip(0,6).add_mask()
video = video.resize(size)

foto1 = (ImageClip("D:\\upload\\foto1.png").set_duration(3))
foto1 = foto1.resize(size)

foto2 = (ImageClip("D:\\upload\\foto2.png").set_duration(3))
foto2 = foto2.resize(size)

foto3 = (ImageClip("D:\\upload\\fotoend.jpg").set_duration(2))
foto3 = foto3.resize(size)

num = video.duration + 3

numfin = num+3

# creating the video
videofinal = CompositeVideoClip([
                            foto1, # starts at t=0
                            video.set_start(3),
                            foto2.set_start(num),
                            foto3.set_start(numfin)])

background_audio_clip = AudioFileClip("D:\\upload\\audio.mp3").subclip(0,3)
bg_music = concatenate_audioclips([background_audio_clip,
                                      video.audio])

videofinal = videofinal.set_audio(bg_music)

videofinal.write_videofile("D:\\upload\\final.mp4")