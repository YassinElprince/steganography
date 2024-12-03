from PIL import Image

def string_to_bin(message):
    return ''.join(format(ord(char), '08b') for char in message)

def hide_message_in_image(image_path, secret_message, output_path):
    image = Image.open(image_path)
    binary_message = string_to_bin(secret_message) + '1111111111111110' 
    data_index = 0
    data_length = len(binary_message)

    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            if data_index < data_length:
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_message[data_index])  
                pixels[x, y] = (r, g, b)
                data_index += 1

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
