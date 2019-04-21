import cv2
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "source",
    help="video source")


def main():
    args = parser.parse_args()

    source = args.source

    camera = cv2.VideoCapture(0)
    for i in range(3):
        return_value, image = camera.read()
        cv2.imwrite('c_{}.jpg'.format(i), cv2.resize(image, (640, 360)))


if __name__ == '__main__':
    main()
