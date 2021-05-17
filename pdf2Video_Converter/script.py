# Import libraries
from PIL import Image
import pytesseract
from mutagen.mp3 import MP3
import sys
from moviepy.editor import VideoFileClip
import moviepy.editor as mpe
from gtts import gTTS
from pdf2image import convert_from_path
import os



def pdf2text(PDF_file):

	# Getting all pages of Pdf
	pages =convert_from_path(PDF_file, 500)

	
	image_counter=1

	print("Converting to images......")
	for page in pages:

		
		filename="page_"+str(image_counter)+".jpg"


		page.save(filename, 'JPEG')


		image_counter=image_counter + 1



	filelimit=image_counter-1

	mtext=""


	print("Extracting Text.......")
	for i in range(1, filelimit + 1):

		
		filename="page_"+str(i)+".jpg"

		mtext+=str(((pytesseract.image_to_string(Image.open(filename)))))

		
	# replacing the text like arg-ument (which are included in new line with hyphen with word)
	mtext=mtext.replace('-\n', '')

	# Deleting Image files 
	for i in range(1, filelimit + 1):
		filename="page_"+str(i)+".jpg"
		os.remove(filename)

	return mtext


def text2video(mtext,video_file):

	language = 'en'
	
	# Converting text to audio
	myobj = gTTS(text=mtext, lang=language, slow=False)
	
	myobj.save("output.mp3")

	audio = MP3("output.mp3")

	# duration of audio file in seconds
	audio_length=int(audio.info.length)
		
		
	videoclip = VideoFileClip(video_file)

	# Clipping orignal video according to the length of video	
	videoclip = videoclip.subclip(0, audio_length)

	background_music = mpe.AudioFileClip("output.mp3")

	
	new_clip = videoclip.set_audio(background_music)
	new_clip.write_videofile("final.mp4")
	os.remove("output.mp3")



if __name__ == "__main__":
	# Getting name of pdf file
	PDF_file = sys.argv[1]

	# Getting name of video file
	video_file=sys.argv[2]

	# Extracting Text from Pdf
	text=pdf2text(PDF_file)

	# Converting text to video
	text2video(text,video_file)
