import os
import sys
import webbrowser
f_path = r'C:\users\SaberH\home\www\/' + sys.argv[2] 
# check if the command is create
if sys.argv[1] == "create":
	# check if the folder type is html
	if sys.argv[2] == "html":
		if os.path.exists(f_path):
			print("Error folder already exists , Try different name .")
		else:
			# Create main folder
			os.makedirs(f_path, mode=0o777, exist_ok=False)
			# create css folder
			os.makedirs(f_path + "\css", mode=0o777, exist_ok=False)
			# create js folder
			os.makedirs(f_path + "\js", mode=0o777, exist_ok=False)
			# create html file
			f_html = open(f_path + "\index.html", "w+")
			f_html.write("<!DOCTYPE html>\n<html>\n<head>\n<title>%s</title>\n<link rel='stylesheet' href='css/style.css'>\n</head>\n<body>\n\n<h1>Hello World</h1>\n<script src='js/client.js'></script>\n</body>\n</html>" % sys.argv[2])
			f_html.close()
			# create css file
			f_css = open(f_path + "\css\style.css", "w+")
			f_css.write("body {\n	margin: 0;\n	padding: 0;\n}")
			f_css.close()
			# create js file
			f_js = open(f_path + "\js\client.js", "w+")
			f_js.close()
			# navigate to site.
			webbrowser.open("http://localhost/www/" + sys.argv[2])
	elif sys.argv[2] == "node":
		print("still working on it , check back later .")
	else:
		print("Unkown folder type.")
else:
	print("Use command <create> to create html folders for now. ")
