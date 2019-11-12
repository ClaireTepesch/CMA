#Claire Tepesch
#Art Display Application

from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def show_image():
	#import data from text file
	with open('data.txt', 'r') as file:
		data = file.read().replace('\n', '')
	#split the text string into a list of strings, each containing the information about one art piece
	text = data.split('[')
	#parse through the art and clean up the string
	for art in text:
		newstr = art.replace("\\", "")
		nextstr = newstr.replace(" , ", "\n")
	text.pop(0) #clean extraneous information
	text.pop(0) #"
	#choose one artpiece to display
	#TODO: create a random number to choose from the art pieces and display a random one
	rand = random.randint(0,90) #create random integer
	content = str(text[0]) #choose art piece for display
	edited = ""
	for i in range(len(text)-1):
		content = str(text[rand]) #choose random piece of artwork for display
		content = content.split("\"")
		for line in content:
			line = line[:-1] #formatting: clean lines of extra characters
			line = line.replace("\"", "")
			edited = edited + line
			length = len(line)
			try:
				float(line)
				if length > 5:
					num = line #extract number for the art piece image
					print(num)
			except ValueError:
				pass
		relevantInfo = edited[6:-1]  # portion of information to display
		relevantInfo = relevantInfo.replace(",", "\n")
		#TODO: Render each image with the appropriate data
		return render_template("base.html", user_image = "/static/ArtWorks/"+num+"_reduced.jpg", text = relevantInfo)
		#TODO: create interactive feature for iterating between the different artworks
if __name__ == '__main__':
    app.run(debug=True)
