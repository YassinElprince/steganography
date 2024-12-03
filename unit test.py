import unittest
from PIL import Image


def string_to_bin(message):
    return ''.join(format(ord(char), '08b') for char in message)

# Unit test class
class TestStringToBin(unittest.TestCase):
    
    def test_normal_string(self):
        self.assertEqual(string_to_bin("AB"), "0100000101000010")  # 'A' -> 01000001, 'B' -> 01000010

    def test_empty_string(self):
        self.assertEqual(string_to_bin(""), "")  # An empty string should return an empty string

    def test_string_with_spaces(self):
        self.assertEqual(string_to_bin("A B"), "010000010010000001000010")  # 'A' -> 01000001, ' ' -> 00100000, 'B' -> 01000010
    
    def test_string_with_numbers(self):
        self.assertEqual(string_to_bin("123"), "001100010011001000110011")  # '1' -> 00110001, '2' -> 00110010, '3' -> 00110011

    def test_string_with_multiple_spaces(self):
        self.assertEqual(string_to_bin("A  B"), "01000001001000000010000001000010")  # 'A' + space + space + 'B'
    
    def test_mixed_string(self):
        self.assertEqual(string_to_bin("A1!"), "010000010011000100100001")  # 'A' -> 01000001, '1' -> 00110001, '!' -> 00100001




def hide_message_in_image(image_path, secret_message, output_path):
    image = Image.open(image_path)
    binary_message = string_to_bin(secret_message) + '1111111111111110'  # Using a delimiter to mark the end
    data_index = 0
    data_length = len(binary_message)

    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            if data_index < data_length:
                r, g, b = pixels[x, y]
                # Modify the least significant bit of the red channel
                r = (r & ~1) | int(binary_message[data_index])  # Set LSB to the message bit
                pixels[x, y] = (r, g, b)
                data_index += 1

    image.save(output_path)

class TestHideMessageInImage(unittest.TestCase):

    def setUp(self):
        # Create a temporary image for testing
        self.image_path = 'test_image.png'
        self.output_path = 'output_image.png'
        self.secret_message = "Hi"
        
        # Create a simple white image
        img = Image.new('RGB', (10, 10), color='white')
        img.save(self.image_path)

    def test_hide_message_in_image(self):
        # Hide the message in the image
        hide_message_in_image(self.image_path, self.secret_message, self.output_path)
        
    
if __name__ == '__main__':
    unittest.main()