# Got from https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
from __future__ import print_function
import sys
from vec3 import Vec3

def eprint(*args, **kwargs):
    """Print to stderror"""
    print(*args, file=sys.stderr, **kwargs)


class Image:
    def __init__(self, height, width):
        self.data =  [[ Vec3() for element in range(width) ] for elem in range(height)]
        self.width = width
        self.height = height
    def __str__(self):
        header = "P3\n" + str(self.width) + " " + str(self.height) + "\n255\n"
        representation = header + " ".join(pixel.color() for row in self.data for pixel in row)
        return representation

    def chapOneFill(self):
        for rowid, row in enumerate(self.data):
            eprint("Rendering the", rowid+1, "scanline of", self.height)
            for colid, data in enumerate(row):
                self.data[rowid][colid] = Vec3((colid)/self.width, ((self.width - rowid))/self.height, 0.2)
        eprint("Finished Rendering")

if __name__ == "__main__":
    testImage = Image(100, 200)
    testImage.chapOneFill()
    print(testImage)
