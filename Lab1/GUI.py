import tkinter as tk
from Backend import GetCommentsFromFakeAI

class ChatroomGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AI Chat Box For Fashion")
        self.geometry("450x550")
        self.configure(bg="#2D3B48")
        
        self.current_stage = "gender"  # State variable to track conversation stage
        self.user_input: list[str] = []

        # Chat display frame (1st pack)
        self.chat_frame = tk.Frame(self, bg="#2D3B48")
        self.chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Scrollbar for the chat display
        self.chat_scrollbar = tk.Scrollbar(self.chat_frame)
        self.chat_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Text widget for chat history
        self.chat_display = tk.Text(self.chat_frame, wrap="word", bg="#192A3E", fg="white", font=("Helvetica", 12),
                                     yscrollcommand=self.chat_scrollbar.set, state="disabled", bd=0)
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.chat_scrollbar.config(command=self.chat_display.yview)

        # Button frame (2nd pack)
        self.button_frame = tk.Frame(self, bg="#2D3B48")
        self.button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Initial AI message
        self.add_message("Hi! i am your Fashion AI Assistent.\nPlease choose your gender so i can create an outfit for you!", "AI")
        
        # Call the method to create the initial gender buttons
        self.update_buttons()

    def add_message(self, message: str, sender):
        """Adds a message to the chat display."""
        self.chat_display.config(state="normal")
        if sender == "user":
            self.user_input.append(message.replace(" ", ""))
            self.chat_display.tag_configure("user", justify="right")
            self.chat_display.insert(tk.END, "User: " + message + "\n\n", "user")
        else:
            self.chat_display.tag_configure("ai", justify="left")
            self.chat_display.insert(tk.END, "AI: " + message + "\n\n", "ai")
        self.chat_display.see(tk.END)
        self.chat_display.config(state="disabled")

    def update_buttons(self):
        """Clears existing buttons and creates new ones based on the current stage."""
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        if self.current_stage == "gender":
            buttons = ["Male", "Female"]
        elif self.current_stage == "occasion":
            buttons = ["Date", "Family Meeting", "Holiday", "School", "Wedding", "Other"]
        elif self.current_stage == "color":
            buttons = ["Black", "White", "Blue", "Red", "Green", "Yellow"]
        else:
            buttons = ["Start Over"]

        for btn_text in buttons:
            button = tk.Button(self.button_frame, text=btn_text, bg="#C4C4C4", fg="black", 
                               font=("Helvetica", 12, "bold"), command=lambda text=btn_text: self.send_message(text))
            button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
    
    def reset_conversation(self):
        """Resets the conversation to the beginning."""
        self.user_input.clear()
        self.chat_display.config(state="normal")
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state="disabled")
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