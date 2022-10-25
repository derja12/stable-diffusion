import keras_cv
import sys
import argparse
from tensorflow import keras
from PIL import Image

# PROMPT = "cute magical flying dog, fantasy art, golden color, high quality, highly detailed, elegant, sharp focus, concept art, character concepts, digital painting, mystery, adventure"
PROMPT = "rock concert, metal concert, realistic, photography, stadium arena, closeup, band, guitarist, sharp focus"

def main(argv):
    args = parse_args(argv)
    model = keras_cv.models.StableDiffusion(img_width=args.width, img_height=args.height)
    images = model.text_to_image(PROMPT, batch_size=args.batch)
    save_images(images, args.file)

def save_images(images, filename):
    for i in range(len(images)):
        Image.fromarray(images[i]).save("{}-{}.png".format(filename, i))

def parse_args(argv):
    parser = argparse.ArgumentParser(prog=argv[0], description='stable diffusion generator (using tensorflow/keras')
    parser.add_argument('--batch', '-b', default=3, type=int, help="number of images to create (default = 3)")
    parser.add_argument('--file', '-f', default="my_image", type=str, help="string that file names will be generated based on (ie. '--file my_image' generates 'my_image-1.png, my_image-2.png, ...) (default = my_image)")
    parser.add_argument('--height', '-H', default=512, type=int, help="height of image, required to be multiple of 128 (rounds to nearest if given invalid number) (default = 512)")
    parser.add_argument('--width', '-w', default=512, type=int, help="width of image, required to be multiple of 128 (rounds to nearest if given invalid number) (default = 512)")

    return parser.parse_args(argv[1:])

if __name__ == "__main__":
    main(sys.argv)