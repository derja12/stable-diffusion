import time
import keras_cv
from tensorflow import keras
import matplotlib.pyplot as plt
from PIL import Image

model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)
images = model.text_to_image("cute magical flying dog, fantasy art, "
    "golden color, high quality, highly detailed, elegant, sharp focus, "
    "concept art, character concepts, digital painting, mystery, adventure", batch_size=2)

def plot_images(images):
    plt.figure(figsize=(20, 20))
    for i in range(len(images)):
        ax = plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i])
        plt.axis("off")
        Image.fromarray(images[i]).save("test"+str(i)+".png")


plot_images(images)