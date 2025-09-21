import customtkinter
import tkinter as tk
import os
from Backend import GetCommentsFromFakeAI

# Use the absolute path to ensure files are found regardless of where the script is executed.
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the cherry.json file
theme_path = os.path.join(script_dir, "cherry.json")
customtkinter.set_default_color_theme(theme_path)

class ChatroomGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("AI Chat Box For Fashion")
        self.geometry("450x550")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.current_stage = "gender"  # State variable to track conversation stage
        self.user_input: list[str] = []

        # Chat display frame (1st pack)
        self.chat_frame = customtkinter.CTkFrame(self)
        self.chat_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.chat_frame.grid_rowconfigure(0, weight=1)
        self.chat_frame.grid_columnconfigure(0, weight=1)
        
        # Text widget for chat history with built-in scrollbar
        self.chat_display = customtkinter.CTkTextbox(self.chat_frame, wrap="word", font=("Helvetica", 12), state="disabled", corner_radius=0)
        self.chat_display.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Button frame (2nd pack)
        self.button_frame = customtkinter.CTkFrame(self)
        self.button_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=1)
        
        # Initial AI message
        self.add_message("Hi! i am your Fashion AI Assistent.\nPlease choose your gender so i can create an outfit for you!", "AI")
        
        # Call the method to create the initial gender buttons
        self.update_buttons()

    def add_message(self, message: str, sender):
        """Adds a message to the chat display."""
        self.chat_display.configure(state="normal")
        if sender == "user":
            self.user_input.append(message.replace(" ", ""))
            self.chat_display.insert(tk.END, "User: " + message + "\n\n")
        else:
            self.chat_display.insert(tk.END, "AI: " + message + "\n\n")
        self.chat_display.see(tk.END)
        self.chat_display.configure(state="disabled")

    def update_buttons(self):
        """Clears existing buttons and creates new ones based on the current stage."""
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        # Reset column weights for a clean layout
        for col in range(4):
            self.button_frame.grid_columnconfigure(col, weight=0)

        if self.current_stage == "gender":
            buttons = ["Male", "Female"]
            # Distribute buttons evenly
            self.button_frame.grid_columnconfigure(0, weight=1)
            self.button_frame.grid_columnconfigure(1, weight=1)
            for i, btn_text in enumerate(buttons):
                button = customtkinter.CTkButton(self.button_frame, text=btn_text, command=lambda text=btn_text: self.send_message(text))
                button.grid(row=0, column=i, sticky="ew", padx=5, pady=5)

        elif self.current_stage == "occasion":
            buttons = ["Date", "Family Meeting", "Holiday", "School", "Wedding", "Other"]
            for i, btn_text in enumerate(buttons):
                row = i // 3
                col = i % 3
                self.button_frame.grid_columnconfigure(col, weight=1)
                button = customtkinter.CTkButton(self.button_frame, text=btn_text, command=lambda text=btn_text: self.send_message(text))
                button.grid(row=row, column=col, sticky="ew", padx=5, pady=5)

        elif self.current_stage == "color":
            buttons = ["Black", "White", "Blue", "Red", "Green", "Yellow"]
            for i, btn_text in enumerate(buttons):
                row = i // 3
                col = i % 3
                self.button_frame.grid_columnconfigure(col, weight=1)
                button = customtkinter.CTkButton(self.button_frame, text=btn_text, command=lambda text=btn_text: self.send_message(text))
                button.grid(row=row, column=col, sticky="ew", padx=5, pady=5)
        
        else:
            buttons = ["Start Over"]
            self.button_frame.grid_columnconfigure(0, weight=1)
            button = customtkinter.CTkButton(self.button_frame, text=buttons[0], command=lambda text=buttons[0]: self.send_message(text))
            button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
                
    
    def reset_conversation(self):
        """Resets the conversation to the beginning."""
        self.user_input.clear()
        self.chat_display.configure(state="normal")
        self.chat_display.delete("1.0", tk.END)
        self.chat_display.configure(state="disabled")
        self.current_stage = "gender"
        self.add_message("Hi! i am your Fashion AI Assistent.\nPlease choose your gender so i can create an outfit for you!", "AI")
        self.update_buttons()

    def send_message(self, message):
        """Processes the user's button click and updates the conversation state."""
        if message == "Start Over":
            self.reset_conversation()
            return
            
        self.add_message(message, "user")

        if self.current_stage == "gender":
            self.add_message("What is the occasion for your outfit?", "AI")
            self.current_stage = "occasion"
        elif self.current_stage == "occasion":
            self.add_message("What color do you have in mind?", "AI")
            self.current_stage = "color"
        elif self.current_stage == "color":
            
            self.add_message(message= "Thank you! Here is your fashion recommendation.", sender= "AI")
            self.add_message(message= GetCommentsFromFakeAI(self.user_input), sender= "AI")
            self.add_message(message= "Now, you can start over.", sender= "AI")

            self.current_stage = "done"
        
        # Update the buttons based on the new stage
        self.update_buttons()