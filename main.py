import urllib

def read_me():
  document = open("TEST-readme-function.txt", "r") #path to where the document is saved
  content_of_file = document.read()
  document.close
  check_curse_words(content_of_file)

def check_curse_words(text_to_check):
  offended_liberal = urllib.urlopen("http://www.wdylike.appspot.com/?q="+(text_to_check))
  output = offended_liberal.read()
  offended_liberal.close()
  if "true" in output:
    print ("WARNING: Profanity ALERT!!!")
  elif "false" in output:
    print ('No curse words found.')
  else:
    print ("Could not scan document, please try again.")

read_me()
