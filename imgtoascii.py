from PIL import Image

# Function to convert the image to ASCII characters
def image_to_ascii(image):
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    width, height = image.size
    aspect_ratio = height/width
    new_width = 100
    new_height = aspect_ratio * new_width * 0.55
    resized_image = image.resize((new_width, int(new_height)))
    grayscale_image = resized_image.convert("L")
    pixels = grayscale_image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 25]
    ascii_str_len = len(ascii_str)
    ascii_img=""
    for i in range(0, ascii_str_len, new_width):
        ascii_img += ascii_str[i:i+new_width] + "\n"
    return ascii_img

# Ask the user for the image path
img_path = input("Please enter the path to the image: ")

try:
    # Open the image from the provided path
    img = Image.open(img_path)
    ascii_image = image_to_ascii(img)
    print(ascii_image)

except FileNotFoundError:
    print(f"No file found at {img_path}. Please check the path and try again.")
except Exception as e:
    print(f"An error occurred: {e}")
