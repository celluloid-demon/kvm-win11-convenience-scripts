import requests

URL = "https://archive.org/download/froggerusarerelease19980310.7z/Frogger%20%28USA%29%20%28Rerelease%29%20%2819980310%29.7z"

def get_archive(url, destination="downloaded_file.7z"):

	try:

		response = requests.get(url)

		if response.status_code == 200:

			with open(destination, 'wb') as file:

				file.write(response.content)

			print(f"Download successful. File saved as '{destination}'")

		else:

			print(f"Failed to download. Status code: {response.status_code}")

	except Exception as e:

		print(f"An error occurred: {e}")

def main():

	get_archive(URL)

if __name__ == "__main__":

	main()
