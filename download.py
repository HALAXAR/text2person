import requests

# Function to download an image from a URL
def download_image(url, filename):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a file in write-binary mode and save the content
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {filename}")
    else:
        print(f"Failed to retrieve image. Status code: {response.status_code}")

# Example usage
image_url = "https://d9jy2smsrdjcq.cloudfront.net/generations/0-c9a0eed7-84a1-4761-b2e3-3e6da04b6d9c.png"  # Replace with the actual image URL
filename = "downloaded_image.jpg"  # The name to save the image as

download_image(image_url, filename)
