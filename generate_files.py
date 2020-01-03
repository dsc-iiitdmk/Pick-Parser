from pdf_to_png import *
import spacy
import io

def generate_summary(base_path,resume_file,model_path,text_file_name,summary_file_name):
	generate_images_and_text_from_pdf(base_path+"/"+resume_file,base_path)
	nlp = spacy.load(model_path)
	f = io.open(base_path+"/"+text_file_name,"r",encoding="utf-8")
	text = f.read()
	fw = io.open(base_path+"/"+summary_file_name,"w",encoding="utf-8")
	doc_to_test = nlp(text)
	d = {}
	for ent in doc_to_test.ents:
		d[ent.label_]=[]
	for ent in doc_to_test.ents:
		d[ent.label_].append(ent.text)

	for i in set(d.keys()):
		fw.write("\n\n")
		fw.write(i +":"+"\n")
		for j in set(d[i]):
			fw.write(j.replace('\n','')+"\n")
	f.close()
	fw.close()


#base_path = "resumes/ashu"

#generate_images_and_text_from_pdf(base_path+"/ashu.pdf",base_path)

#nlp = spacy.load("model/") 

#print("Model : ",nlp)

#f = io.open(base_path+"/out_text.txt","r",encoding="utf-8")
#text = f.read()
#print(text)

#fw = io.open(base_path+"/summary_text.txt","w",encoding="utf-8")
#doc_to_test=nlp(text)
#d={}
#for ent in doc_to_test.ents:
#    d[ent.label_]=[]
#for ent in doc_to_test.ents:
#    d[ent.label_].append(ent.text)

#for i in set(d.keys()):

#    fw.write("\n\n")
#    fw.write(i +":"+"\n")
#    for j in set(d[i]):
#        fw.write(j.replace('\n','')+"\n")

#f.close()
#fw.close()

