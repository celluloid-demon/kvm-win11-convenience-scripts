from urllib.request import urlretrieve

OUT = "frogger.7z"
URL = (

		"https://archive.org/download/froggerusarerelease19980310.7z/"
		"Frogger%20%28USA%29%20%28Rerelease%29%20%2819980310%29.7z"
	
	)

def main():

	urlretrieve(URL, OUT)

main()
