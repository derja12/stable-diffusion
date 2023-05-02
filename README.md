# ACM Fall 2022 - Stable Diffusion

## Dependancys
* Python3
* Python3 Libraries (can be installed using pip)
  * Tensorflow
  * Tensorflow_datasets
  * Keras_cv

## Creating a model
In order to create your own model, either of the following:
### Use the minimal_generator python file by running the following
```bash
python3 minimal_generator.py
```
The minimal_generator python file _does not_ use flags to customize generation. In order to change prompt, batch_size, filename, 
or image_sizing, you must edit hardcoded values in the file.

### Use the generator python file by running the following
```bash
python3 generator.py -f FILENAME -b IMAGE_COUNT -h IMAGE_HEIGHT -w IMAGE_WIDTH
```
The generator python file uses flags to customize generation. In order to change batch_size, filename, 
or image_sizing, define the respective flags when running the above command. Run the command with `-h` to see 
the options in more detail. Changing the prompt still requires editing hardcoded file values, specifically the global `PROMPT` value.

## Resources/Tutorial links
* [Tutorial](https://keras.io/guides/keras_cv/generate_images_with_stable_diffusion/)
* [Stable Diffusion API](https://keras.io/api/keras_cv/models/stable_diffusion/)
* [Stable Diffusion Illustration](https://jalammar.github.io/illustrated-stable-diffusion/)
* [Video explaining AI Image Generation](https://www.youtube.com/watch?v=1CIpzeNxIhU)
* Prompt Stuff
    * [Prompt discussion/Examples](https://strikingloo.github.io/stable-diffusion-vs-dalle-2)
    * [Prompt Guide](https://www.howtogeek.com/833169/how-to-write-an-awesome-stable-diffusion-prompt/)
    * [List of 100 prompts](https://mpost.io/best-100-stable-diffusion-prompts-the-most-beautiful-ai-text-to-image-prompts/)
