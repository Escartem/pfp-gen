from PIL import Image
from time import sleep
from random import randint
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--show", action="store_true", help="Generate and show the image")
parser.add_argument("--save", action="store_true", help="Generate and save the image in the app directory")
args = parser.parse_args()


class Picture:
    def __init__(self):
        self.img = Image.new('RGB', (420, 420), "white")
        self.pixels = self.img.load()

        self.offset_x = 22.5
        self.offset_y = 22.5

    def fill_rect(self, x, y, width, height, color):
        for px in range(width):
            for py in range(height):
                self.pixels[x+px, y+py] = color

    def gen(self, size):
        size = size
        color = (randint(0, 255), randint(0, 255), randint(0, 255))

        # generate line 2 and 4
        for y in range(5):
            c = randint(0, 1)
            if c == 1:
                self.fill_rect(size+self.offset_x, y*size+self.offset_y, size, size, color)
                self.fill_rect(3*size+self.offset_x, y*size+self.offset_y, size, size, color)

        # generate line 1 and 5
        for y in range(5):
            c = randint(0, 1)
            if c == 1:
                self.fill_rect(self.offset_x, y*size+self.offset_y, size, size, color)
                self.fill_rect(4*size+self.offset_x, y*size+self.offset_y, size, size, color)

        # generate line 3
        for y in range(5):
            c = randint(0, 1)
            if c == 1:
                self.fill_rect(2*size+self.offset_x, y*size+self.offset_y, size, size, color)

    def main(self):
        self.gen(75)
        if args.show:
            self.img.show()
            print("Done !")
        if args.save:
            self.img.save('generated' + str(randint(100, 999)) + '.png')
            print("Saved image !")
        sleep(3)
        exit()


if (not args.show) and (not args.save):
    print("No arguments specified")
    print("Please select at least one !")
    sleep(3)
    exit()
else:
    pic = Picture()
    pic.main()
