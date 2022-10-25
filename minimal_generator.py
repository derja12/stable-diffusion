import keras_cv
from tensorflow import keras
from PIL import Image

model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)
images = model.text_to_image("cute magical flying dog, fantasy art, "
    "golden color, high quality, highly detailed, elegant, sharp focus, "
    "concept art, character concepts, digital painting, mystery, adventure", batch_size=1)

def save_images(images):
    for i in range(len(images)):
        Image.fromarray(images[i]).save("test"+str(i)+".png")

save_images(images)