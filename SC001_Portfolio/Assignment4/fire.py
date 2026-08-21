"""
File: fire.py
Name: Summer
---------------------------------
This file contains a function called highlight_fires,
which detects pixels that are identified as fire and
highlights them to make the fire areas easier to observe.
"""


from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    Highlight fire areas in the image by turning red pixels stronger
    and converting other pixels to grayscale.
    """
    img = SimpleImage(filename)
    for pixel in img:
        avg = (pixel.red+pixel.blue+pixel.green)//3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.blue = 0
            pixel.green = 0
        else:
            pixel.blue = avg
            pixel.red = avg
            pixel.green = avg
    return img


def main():
    """
    Display the original image and the fire-highlighted image.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
