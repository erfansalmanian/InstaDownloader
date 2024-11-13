## InstaDownloader ##
InstaDownloader is a simple Python script to download images or videos from Instagram without additional files like text or metadata. Developed by Erfan Salmanian.


## Features ##
Supports Images and Videos: Users can select to download either images or videos.
Minimalist Storage: No extra files or metadata are saved.


## Requirements ##
This script uses the Instaloader library. Install it by running:
pip install instaloader

## Usage ##
Run the Script: Execute the script and follow the prompts.
Enter the Instagram Link: Provide the link of the Instagram post you want to download.
Choose Media Type: Select if you want to download an image (I for Image) or a video (V for Video).
Download Location: The downloaded content is saved in images or videos folders within the script’s working directory.


## Example Execution ##
python instadownloader.py

## Example: ##
Enter your Instagram link (or 'e' to exit): https://www.instagram.com/p/CODE/
Image or Video? (I,V): I
Downloading image...
Download complete :)


## Error Handling ##
If the script cannot process the provided link, it displays an error message. Ensure the link is correct and points to a public post.


## License ##
This project is free to use and distribute without any licensing restrictions.

## Author ##
Developed by Erfan Salmanian - [GitHub](https://github.com/erfansalmanian)