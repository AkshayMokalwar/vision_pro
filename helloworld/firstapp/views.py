from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from pathlib import Path
from django.conf import settings 
import datetime
import shutil
# Create your views here.
def home_view(request):
	# date =datetime.datetime.now()
	# print("**********")
	# print()
	if(request.method == 'GET'):
		render(request,'index(2).html')
	elif(request.method == 'POST'):
		uploadedfile=request.FILES["up_img"]
		print("1"*20)
		print(uploadedfile.name)
		print(uploadedfile.size)
		fs=FileSystemStorage();
		
		filename=fs.save(uploadedfile.name, uploadedfile)
		# file = default_storage.open(file_name)
		uploaded_file_urls = fs.url(filename)
		print("2"*20)
		
		print(filename)
		print("3"*20)
		
		print(uploaded_file_urls)

		record={'im_url':uploaded_file_urls,'im_name':filename}
		# mydb=psycopg2.connect(host="localhost",user="postgres",password="12345",database="Nikhil")
		# mycursor=mydb.cursor()
		# mycursor.execute('INSERT INTO public.tbl(imagename, image_url)VALUES (%s, %s);',(filename,uploaded_file_urls))
		# mydb.commit()
		# mydb.close()
		out_flag=start_ml(filename)
		if(out_flag):
			print("ml model run successfull !!!!")
			return render(request,'prev.html',{'im_name':filename})
		msg="Not worked !! please start again!!!"
		return render(request,'index(2).html',{'m':msg})
	return render(request,'index(2).html')
def start_ml(flname):
	# fs=FileSystemStorage();

	# input image folder ="C:\Users\AkshaySSD\helloworld\statics\media\images_uploaded\"
	# output image folder ="C:\Users\AkshaySSD\helloworld\statics\media\output\"

	# file = fs.open(flname)
	# print(settings.BASE_DIR)

	# for copying image from images_uploaded to output folder
	input_path =r"C:\Users\AkshaySSD\helloworld\statics\media\images_uploaded\{}".format(flname)
	target =r"C:\Users\AkshaySSD\helloworld\statics\media\output\{}".format(flname)
	
	shutil.copyfile(input_path, target)


	#C:\Users\AkshaySSD\helloworld\statics\media\output

	print('folder created: {}'.format(input_path))
	
	
	#----------------------------------------------------- start here ---------------------------------------
	# use input_path as for the input image
	# store the image in C:\Users\AkshaySSD\helloworld\statics\media\output\ with same name
	# return the True If the ml-code success full
	# else return False
	

	return False