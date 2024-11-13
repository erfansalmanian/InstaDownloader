"""
Developed by Erfan Salmanian on 11.11.2024
https://github.com/erfansalmanian
This script downloads images or videos from Instagram without any additional files such as text
"""

import sys
import os
import instaloader


def download_instagram():
    print(
        "\n"
        "\t"
        ".:: Welcome to InstaDownloader! ::."
        "\t"
        "\n"
        "\n"
        " - Developed by Erfan Salmanian"
        "\n"
    )

    # Initialize Instaloader with minimal settings
    SETTINGS = instaloader.Instaloader(
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=False,
        post_metadata_txt_pattern="",  # No text files saved
    )

    while True:
        link = input("Enter your Instagram link (or 'e' to exit): ")
        if link.lower() == "e":
            sys.exit("\n" "\t" ".:: Goodbye! ::." "\t" "\n")

        try:
            shortcode = link.split("/")[-2]  # Extract shortcode from URL
            post = instaloader.Post.from_shortcode(SETTINGS.context, shortcode)

            user_choice = input("Image or Video? (I,V): ").lower()
            if user_choice == "e":
                sys.exit("\n" "\t" ".:: Goodbye! ::." "\t" "\n")
            # Download logic based on user choice
            if user_choice in ["v", "video"] and post.is_video:
                os.makedirs("videos", exist_ok=True)
                os.chdir("videos")
                print("Downloading video...")
                SETTINGS.download_post(post, target="your_videos")
                os.chdir("..")
                print("Download complete :)")

            elif user_choice in ["i", "image"] and not post.is_video:

                os.makedirs("images", exist_ok=True)
                os.chdir("images")
                print("Downloading image...")
                SETTINGS.download_post(post, target="your_pictures")
                os.chdir("..")
                print("Download complete :)")

            else:
                print("Invalid content type or input. Try again.")
        except Exception as e:
            print(f"Error: {e}. Check the link and try again.")


download_instagram()
