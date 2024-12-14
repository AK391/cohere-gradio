import gradio as gr
import cohere_gradio

gr.load(
    name='command-r7b-12-2024',
    src=cohere_gradio.registry,
).launch()