from PIL import Image

# Create a simple 10x10 black and white image
img = Image.new('L', (10, 10), color=255)  # Create a white image
for x in range(10):
    for y in range(10):
        if (x + y) % 2 == 0:
            img.putpixel((x, y), 0)  # Set pixel to black

img.save('input_image.png')  # Save the image
