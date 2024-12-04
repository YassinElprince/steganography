from PIL import Image

def string_to_bin(message):  # Convert each character in the message to ito binary 
    return ''.join(format(ord(char), '08b') for char in message)

def hide_message_in_image(image_path, secret_message, output_path):
    image = Image.open(image_path)
    binary_message = string_to_bin(secret_message) + '1111111111111110'  # Convert the secret message to binary and append a delimiter to mark the end
    data_index = 0   # Index to track the current bit of the message being hidden
    data_length = len(binary_message) # Total length of the binary message
    pixels = image.load()   # Load the pixel data of the image
    width, height = image.size   # Get the dimensions of the image

    for y in range(height):   # go over each pixel in the image
        for x in range(width):
            if data_index < data_length:   # Check if there are still bits to hide
                r, g, b = pixels[x, y]    # Get the RGB values of the current pixel
                r = (r & ~1) | int(binary_message[data_index])   # Modify the LSB of the red channel to hide the message bit and Set LSB to the message bit
                pixels[x, y] = (r, g, b)    # Update the pixel with the modified red value
                data_index += 1  # Move to the next bit of the message

    image.save(output_path)

def main():
    print("Welcome to the Image Message Hider!")
    image_path = input("Enter the path to the image: ")
    secret_message = input("Enter the secret message you want to hide: ")
    output_path = input("Enter the path to save the modified image: ")
    hide_message_in_image(image_path, secret_message, output_path)
    print(f"Message hidden in {output_path}")
    
if __name__ == "__main__":
    main()
