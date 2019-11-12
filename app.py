#Claire Tepesch
#Art Display Application

from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def show_image():
	#import data from text file generated from art database json
	with open('data.txt', 'r') as file:
		data = file.read().replace('\n', '')
	#split the text string into a list of strings, each containing the information about one art piece
	text = data.split('[')
	#parse through string and clean up the string
	for art in text:
		newstr = art.replace("\\", "")
		nextstr = newstr.replace(" , ", "\n")
	text.pop(0) #remove empty strings
	text.pop(0) #remove empty strings
	#choose one artpiece to display
	#create a random number to choose from the art pieces and display a random one
	rand = random.randint(0,100) #create random integer
	array = []
	for i in range(len(text)-1):
		content = str(text[rand]) #choose random piece of artwork for display
		content = content.split("\"") #split the art description into sections
		for line in content:
			line = line[:-1] #formatting: clean lines of extra characters
			line = line.replace("\"", "") #format string
			if len(line) > 10: #only display relevant information
				array.append(line)
			length = len(line)
			if "." in line and length<11 and not " " in line: #find image code
				num = line
		one = array[0] #header text for display
		two = array[-1] #footer text for display
		return render_template("base.html", user_image = "/static/ArtWorks/"+num+"_reduced.jpg", text = one, text2 = two)
		#TODO: create interactive feature in order for user to iterate between the different artworks
if __name__ == '__main__':
    app.run(debug=True)
