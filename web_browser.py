#function to listen to voice commands and then return a corresponding string 
def listen(chunk_size=2048):
	import speech_recognition as sr
	# obtain audio from the microphone  
	r = sr.Recognizer()  
	with sr.Microphone(chunk_size=chunk_size) as source:  
		print("Please wait. Calibrating microphone...")  
		# listen for 3 seconds and create the ambient noise energy level  
		r.adjust_for_ambient_noise(source, duration=3)  
		#Instead of printing "SAY OUT LOUD"
		print("Say something!")  
		audio = r.listen(source)
		# recognize speech using Google  
		try:  
			text = r.recognize_google(audio)
			if(text!=None):
				return text
			else:
				listen(chunk_size)
		except sr.UnknownValueError:  
			print("Google could not understand audio") 
			listen(chunk_size)
		except sr.RequestError as e:  
			print("Google error; {0}".format(e)) 
			listen(chunk_size) 


#function to run google search from command line
def googleSearch():
	import webbrowser as wb
	from google import search
	from urlparse import urlparse

	urllist = []
	query = listen()
	print query
	for j in search(query, tld="co.in", num=9, stop=1, pause=2):
		urllist.append(j)

	for i in range(0,len(urllist)):
		url = urlparse(urllist[i])
		output_text = url.netloc+url.path
		#SPEAK LOUD
		print output_text
		print "Visit this URL? (Yes/No)"
		ans = listen(256)
		print ans
		if(ans=='yes'):
			wb.open_new(urllist[i])
			break



googleSearch()
