import flask
from generate_files import *
from flask import request
import io

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/',methods=['GET'])
def home():
	return "Welcome to CrackHire Resume Parsing Portal."

@app.route('/parse',methods=['GET'])
def parse_resume():
	base_path = request.args.get('dir')
	file_name = base_path+".pdf"
	base_path = "resumes/"+base_path
	print(base_path,file_name)
	model_path = "model/"
	text_file_name = "out_text.txt"
	summary_file_name = "summary_text.txt"
	generate_summary(base_path,file_name,model_path,text_file_name,summary_file_name)
	f = io.open(base_path+"/"+summary_file_name,"r",encoding="utf-8")
	text = f.read()
	return text


app.run(host="127.0.0.1",port=3001)
