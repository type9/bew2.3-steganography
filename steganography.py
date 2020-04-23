from PIL import Image 

def decode_image(file_location):
    encoded_image = Image.open(file_location)
    encoded_pixels = encoded_image.load()

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    decoded_pixels = decoded_image.load()

    black = (0, 0, 0)
    white = (255, 255, 255)

    for x in range(x_size): # for row
        for y in range(y_size): # for each pixel in each row
            r_val = bin(encoded_pixels[x, y][0]) # gets r channel value
            if r_val[-1] == '0':
                decoded_pixels[x, y] = black
            else:
                decoded_pixels[x, y] = white
            

    decoded_image.save("images/decoded_image.png")

def encode_image(text):
    

if __name__ == '__main__':
    decode_image('images/encoded_sample.png')