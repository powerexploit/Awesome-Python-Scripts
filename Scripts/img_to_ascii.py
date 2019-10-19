from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import argparse

char_map = " `'\".,:;i!~-+]{|1\\rxucoz6?UCL0O*#W&B@$$"


class Picture:
    def __init__(self, filename, resolution):
        # loading image
        img = Image.open(filename)
        img = img.resize((resolution * round(img.size[0] / img.size[1]), resolution))
        self.image = img
        self.width, self.height = img.size

        # enhance image for cleaner result
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
        self.image = ImageEnhance.Contrast(self.image).enhance(2)

        # required matrices
        self.char_matrix = []
        self.rgb_matrix = []

        # output image
        self.output = Image.new('RGB', (self.width * 10, self.height * 10))

    def generate(self):
        # make 2d array of pixels
        rgb_matrix = list(self.image.getdata())
        self.rgb_matrix = [rgb_matrix[j:j + self.width] for j in range(0, len(rgb_matrix), self.width)]
        # rgb values to intensity values
        intensity_matrix = [[.21 * p[0] + .72 * p[1] + .07 * p[2] for p in pixel_row] for pixel_row in self.rgb_matrix]
        # intensity values to characters
        self.char_matrix = [[char_map[int(i * (len(char_map) - 1) / 255)] for i in i_row] for i_row in intensity_matrix]

    def draw_color(self):
        draw = ImageDraw.Draw(self.output)

        for y in range(self.height):
            for x in range(self.width):
                draw.text((x * 10, y * 10), self.char_matrix[y][x], fill=self.rgb_matrix[y][x])

    def draw_bw(self):
        draw = ImageDraw.Draw(self.output)

        for y in range(self.height):
            for x in range(self.width):
                draw.text((x * 10, y * 10), self.char_matrix[y][x], fill=(255, 255, 255))

    def save_image(self, path):
        self.output.save(path + '.jpg')

    def save_text(self, path):
        string = ""
        for row in self.char_matrix:
            line = [p + p + p for p in row]
            string += ''.join(line) + '\n'

        text_file = open(path + '.txt', "w")
        text_file.write(string)
        text_file.close()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="input file")
    ap.add_argument("-c", "--color", action='store_true', help="color/greyscale")
    ap.add_argument("-r", "--resolution", type=int, default=120, help="output resolution")
    ap.add_argument("-t", "--txt", action='store_true', help="also save as text")
    ap.add_argument("-o", "--output", default='output', help="output file")
    args = vars(ap.parse_args())

    pic = Picture(args["input"], args["resolution"])

    pic.generate()

    if args["color"]:
        pic.draw_color()
    else:
        pic.draw_bw()

    pic.save_image(args["output"])
    if args["txt"]:
        pic.save_text(args["output"])