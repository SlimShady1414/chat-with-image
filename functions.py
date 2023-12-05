from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

def get_image_caption(image_path):

    """
    generates a short caption for the inputted image
    inputs the image path and generates a caption
    """

    image = Image.open(image_path).convert('RGB')
    model_name = 'Salesforce/blip-image-captioning-large'
    device = "cpu"  #can use cuda if gpu is available

    processor = BlipProcessor.from_pretrained(model_name)
    model = BlipForConditionalGeneration.from_pretrained(model_name).to(device)

    inputs = processor(image,return_tensors='pt').to(device) #image to normal transformation
    output = model.generate(**inputs,max_new_tokens=20)

    caption = processor.decode(output[0],skip_special_tokens=True)

    return caption


def detect_objects(image_path):
    pass

if __name__ == '__main__':
    image_path = '/home/adhinandanj/Downloads/wallpaperflare.com_wallpaper.jpg'
    caption = get_image_caption(image_path)
    print(caption)