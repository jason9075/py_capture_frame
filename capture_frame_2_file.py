import cv2
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "source",
    help="video source")


def main():
    args = parser.parse_args()

    source = args.source

    camera = cv2.VideoCapture(source)
    for i in range(3):
        return_value, image = camera.read()
        cv2.imwrite('{}_{}.jpg'.format(source, i) , image)


if __name__ == '__main__':
    main()
