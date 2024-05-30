import re
import certifi
import ssl
from pytube import YouTube

# Function to check if the provided URL is a valid YouTube URL
def is_valid_youtube_url(url):
    youtube_regex = re.compile(
        r'^(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    return youtube_regex.match(url)

# Main function to execute the script
def main():
    link = input("Enter the video link here --> ")

    if is_valid_youtube_url(link):
        try:
            # Ensure SSL certificates are correctly used
            import ssl
            import certifi
            ssl._create_default_https_context = ssl._create_unverified_context

            # Create the YouTube object using the provided link
            y_tube = YouTube(link)
            
            # Print the title and description of the video
            print(f'Video Title --> {y_tube.title}')
            print(f'Video Description --> {y_tube.description}')
            
            # Check the quality, sound, and resolution of the video
            stream = y_tube.streams.filter(progressive=True)
            video = list(enumerate(stream))
            for i in video:
                print(i)
            
            print("============================")
            index = int(input("Enter the index of the desired stream ==> "))
            stream[index].download()
            print("Successfully Downloaded")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid YouTube URL. Please enter a valid link.")

if __name__ == "__main__":
    main()
