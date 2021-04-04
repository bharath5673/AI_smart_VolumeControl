from moviepy.editor import *

# clip = (VideoFileClip("output.mp4").subclip((3.65),(4.0))
#         .resize(0.3))
clip = (VideoFileClip("output.mp4").subclip((6.5),(9.0)))
# clip = (VideoFileClip("output.mp4"))       
clip.write_gif("output2.gif")