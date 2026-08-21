"""
File: mirror_lake.py
Name: Summer
----------------------------------
This program reads the image "mt-rainier.jpg" and generates
a new image that creates a mirror-lake effect.

The effect is produced by placing an inverted copy of the
original image directly beneath it, simulating a reflection
on the surface of a lake.
"""


from simpleimage import SimpleImage


def reflect(filename):
    """
    Create a vertically reflected image by copying the original image
    and placing its mirror image below it.
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height*2)
    for y in range(img.height):
        for x in range(img.width):
            img_pixel = img.get_pixel(x, y)
            b_img.set_pixel(x, y, img_pixel)
            b_img.set_pixel(x, b_img.height-1-y, img_pixel)

    return b_img


def main():
    """
    Show the original image and the vertically reflected image.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
