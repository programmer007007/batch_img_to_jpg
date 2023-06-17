from PIL import Image
import pillow_avif
import os

# Specify the directory containing the images
directory = "."

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if not filename.endswith((".jpg", ".jpeg",".py")):  # Skip files already in JPG format
        filepath = os.path.join(directory, filename)

        # Open the image file
        try:
            with Image.open(filepath) as image:              
                # Convert the image to JPG format
                jpg_filename = os.path.splitext(filename)[0] + ".jpg"
                jpg_filepath = os.path.join(directory, jpg_filename)
                image.convert("RGB").save(jpg_filepath, "JPEG")
                print(f"Converted {filename} to {jpg_filename}")
                # Delete the original file
                os.remove(filepath)
        except OSError:
            print(f"Cannot convert {filename}")
