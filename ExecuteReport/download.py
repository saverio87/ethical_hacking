import requests

def download(url):
  get_response = requests.get(url)
  file_name = url.split("/")[-1]
  # Creates a list, and each element in the list is a part of the
  # url separated by to forward slashes. We use -1 because we want
  # the last element of the list
  with open(file_name, "wb") as out_file:
    #everything within this block is going to be executed while
    # the file is open
    out_file.write(get_response.content)





download('https://c402277.ssl.cf1.rackcdn.com/photos/7749/images/story_full_width/HI_204718.jpg')