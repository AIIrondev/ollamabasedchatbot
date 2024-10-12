from llama_index.llms.ollama import Ollama
import tkinter as tk

llm = Ollama(model="llama3.2")
response = llm.complete("Why is the sky blue?")
print(response)

class app:
    def __init__(self):
        self.llm = Ollama(model="llama3.2")


    def get_response(self, question):
        response = self.llm.complete(question)
        return response