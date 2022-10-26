# acm Fall 2022 - Stable Diffusion

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
