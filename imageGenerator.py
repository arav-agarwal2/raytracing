class Image:
    def __init__(self, height, width):
        self.data =  [[ [0,0,0] for element in range(width) ] for elem in range(height)]
        self.width = width
        self.height = height
    def __str__(self):
        header = "P3\n" + str(self.width) + " " + str(self.height) + "\n255\n"
        representation = header + " ".join(str(data) for row in self.data for pixel in row for data in pixel)
        return representation

    def chapOneFill(self):
        for rowid, row in enumerate(self.data):
            for colid, data in enumerate(row):
                self.data[rowid][colid] = [(colid*256)//self.width, ((self.width - rowid)*256)//self.height, 51]

if __name__ == "__main__":
    testImage = Image(100, 200)
    testImage.chapOneFill()
    print(testImage)
