# chat-with-image

This is a Streamlit application that allows users to ask questions about an uploaded image and receive responses from a conversational AI agent. The agent uses the OpenAI GPT-3.5 Turbo model to generate answers based on the provided image and user input.

## Installation

1. Clone the repository and change to project directory

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Obtain an OpenAI API key.

4. Replace the placeholder API key in the main.py file with your actual OpenAI API key:

```python
llm = ChatOpenAI(
     openai_api_key='YOUR_API_KEY',
     temperature=0,
     model_name="gpt-3.5-turbo"
 )
``` 

5. Run the streamlit application

```bash
streamlit run main.py
```


# tools

The application utilizes the following custom tools:

    ->ImageCaptionTool: Generates a textual caption for the uploaded image.

    ->ObjectDetectionTool: Performs object detection on the uploaded image and identifies the objects present.


# references

This project uses the OpenAI GPT-3.5 Turbo model. [OpenAI](https://openai.com/)

The LangChain library is used for managing the conversational AI agent and tools. [LangChain](https://github.com/hwchase17/langchain)

The Streamlit library is used for building the interactive user interface. [Streamlit](https://docs.streamlit.io/)

HuggingFace Transformers libraries used :

[Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large) and [facebook/detr-resnet-50](https://huggingface.co/facebook/detr-resnet-50)

