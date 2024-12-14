# `cohere-gradio`

is a Python package that makes it very easy for developers to create machine learning apps that are powered by Cohere's API.

# Installation

You can install `cohere-gradio` directly using pip:

```bash
pip install cohere-gradio
```

That's it! 

# Basic Usage

Just like if you were to use the `cohere` API, you should first save your Cohere API key to this environment variable:

```bash
export COHERE_API_KEY=<your token>
```

Then in a Python file, write:

```python
import gradio as gr
import cohere_gradio

gr.load(
    name='command',
    src=cohere_gradio.registry,
).launch()
```

Run the Python file, and you should see a Gradio Interface connected to the model on Cohere!

![ChatInterface](chatinterface.png)

# Customization 

Once you can create a Gradio UI from a Cohere endpoint, you can customize it by setting your own input and output components, or any other arguments to `gr.Interface`. For example, the screenshot below was generated with:

```python
import gradio as gr
import cohere_gradio

gr.load(
    name='command',
    src=cohere_gradio.registry,
    title='Cohere-Gradio Integration',
    description="Chat with Cohere's Command model.",
    examples=["Explain quantum gravity to a 5-year old.", "How many R are there in the word Strawberry?"]
).launch()
```
![ChatInterface with customizations](chatinterface_with_customization.png)

# Composition

Or use your loaded Interface within larger Gradio Web UIs, e.g.

```python
import gradio as gr
import cohere_gradio

with gr.Blocks() as demo:
    with gr.Tab("Command"):
        gr.load('command', src=cohere_gradio.registry)
    with gr.Tab("Command-Light"):
        gr.load('command-light', src=cohere_gradio.registry)

demo.launch()
```

# Under the Hood

The `cohere-gradio` Python library has two dependencies: `cohere` and `gradio`. It defines a "registry" function `cohere_gradio.registry`, which takes in a model name and returns a Gradio app.

# Supported Models in Cohere

All chat API models supported by Cohere are compatible with this integration. For a comprehensive list of available models and their specifications, please refer to the [Cohere Models documentation](https://docs.cohere.com/docs/models).

-------

Note: if you are getting a 401 authentication error, then the Cohere API Client is not able to get the API token from the environment variable. This happened to me as well, in which case save it in your Python session, like this:

```python
import os

os.environ["COHERE_API_KEY"] = ...
```