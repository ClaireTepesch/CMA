from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def show_image():
	with open('data.txt', 'r') as file:
		data = file.read().replace('\n', '')
	text = data.split('[')
	for art in text:
		newstr = art.replace("\\", "")
		nextstr = newstr.replace(" , ", "\n")
	# print(newstr,"\n")
	text.pop(0)
	text.pop(0)
	content = str(text[0])
	for i in range(len(text)-1):
		content = str(text[i])
		print("here")
		content = content.split("\"")
		for line in content:
			line = line[:-1]
			length = len(line)
			try:
				float(line)
				if length > 5:
					num = line
					print(num)
			except ValueError:
				pass
		return render_template("base.html", user_image = "/static/ArtWorks/"+num+"_reduced.jpg", text = content)

if __name__ == '__main__':
    app.run(debug=True)
