from llama_index.llms.ollama import Ollama
import customtkinter as ctk
import os
from gtts import gTTS
import playsound


class app:
    def __init__(self):
        self.app = ctk.CTk()
        self.llm = Ollama(model="llama3.2")

        self.app.title("Chat Bot")
        self.app.geometry("400x500")
        self.app.configure(bg="white")
        self.main_programm()
        self.app.mainloop()
    
    def main_programm(self):
        self.chat_box = ctk.CTkTextbox(self.app, height=250, width=500)
        self.chat_box.pack(pady=20)
        self.chat_box.tag_config("bot", foreground="red")
        self.chat_box.tag_config("user", foreground="blue")
        self.chat_box.configure(state="disabled")

        self.message_box = ctk.CTkEntry(self.app, width=500)
        self.message_box.pack(pady=20)
        self.message_box.bind("<Return>", self.send_message)

    def send_message(self, event):
        message = self.message_box.get()
        self.message_box.delete(0, "end")
        self.chat_box.configure(state="normal")
        self.chat_box.insert("end", "You: " + message + "\n", "user")
        response = self.get_response(message)
        self.chat_box.insert("end", "Bot: " + str(response) + "\n", "bot")
        self.chat_box.configure(state="disabled")
        self.chat_box.see("end")
        
    def get_response(self, question):
        response = self.llm.complete(question)
        read_message().play_text(response)
        return response


class read_message():
    def play_text(self, message):
        self.message = message
        self.tts = gTTS(text=self.message, lang="en")
        self.tts.save("message.mp3")
        playsound.playsound("message.mp3")
        self.tts.close()
        os.remove("message.mp3")


if __name__ == "__main__":
    app = app()