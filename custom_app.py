import gradio as gr
import cohere_gradio

gr.load(
    name='gpt-4-turbo',
    src=cohere_gradio.registry,
    title='OpenAI-Gradio Integration',
    description="Chat with gpt-4-turbo model.",
    examples=["Explain quantum gravity to a 5-year old.", "How many R are there in the word Strawberry?"]
).launch()