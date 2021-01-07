import os
import numpy as np
from PIL import Image


def get_png_files(rootdir):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if ".png" in file:
                transparent(os.path.join(subdir, file))


def transparent(myimage):
    img = Image.open(myimage)
    img = img.convert("RGBA")

    imgnp = np.array(img)

    white = np.sum(imgnp[:, :, :3], axis=2)
    # measure exact color with gimp or sth. like that!
    white_mask = np.where(white == 240 * 3, 94.8, 0)

    alpha = np.where(white_mask, 0, imgnp[:, :, -1])

    imgnp[:, :, -1] = alpha

    img = Image.fromarray(np.uint8(imgnp))

    img.save(myimage.replace("plots", "transparent"), "PNG")


def main():
    get_png_files("../../data/listenability-tools/plots/conversationTypes/markertypes/")


if __name__ == '__main__':
    main()