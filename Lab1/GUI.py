import tkinter as tk
from tkinter import scrolledtext


class FashionAgentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fashion Sale Chatbot")
        self.root.geometry("500x600")

        # Khung chat
        self.chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="normal", font=("Arial", 11))
        self.chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Khung button tương tác
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Gửi lời chào đầu tiên
        self.add_message("Agent", "Xin chào 👋! Bạn muốn tư vấn thời trang cho Nam hay Nữ?")
        self.show_buttons(["Nam", "Nữ"], self.choose_gender)

    def add_message(self, sender, message):
        """Hiển thị tin nhắn"""
        self.chat_window.insert(tk.END, f"{sender}: {message}\n")
        self.chat_window.see(tk.END)

    def clear_buttons(self):
        """Xóa toàn bộ button hiện tại"""
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def show_buttons(self, options, command):
        """Hiển thị button để lựa chọn"""
        self.clear_buttons()
        for option in options:
            btn = tk.Button(self.button_frame, text=option, width=15, command=lambda opt=option: command(opt))
            btn.pack(side=tk.LEFT, padx=5)

    def choose_gender(self, gender):
        self.add_message("Bạn", gender)
        self.clear_buttons()

        self.gender = gender
        self.add_message("Agent", f"Bạn cần tư vấn trang phục cho dịp nào?")
        self.show_buttons(["Đi làm", "Đi chơi", "Tiệc"], self.choose_event)

    def choose_event(self, event):
        self.add_message("Bạn", event)
        self.clear_buttons()

        self.event = event
        suggestion = self.get_suggestion(self.gender, self.event)
        self.add_message("Agent", f"Gợi ý: {suggestion}")
        self.add_message("Agent", "Bạn có muốn xem sản phẩm sale không?")
        self.show_buttons(["Có", "Không"], self.show_sale)

    def show_sale(self, choice):
        self.add_message("Bạn", choice)
        self.clear_buttons()

        if choice == "Có":
            self.add_message("Agent", "🎉 Danh sách sản phẩm sale hôm nay:")
            if self.gender == "Nam":
                self.add_message("Agent", "- Áo sơ mi trắng: 199k\n- Quần tây đen: 299k\n- Giày da: 499k")
            else:
                self.add_message("Agent", "- Váy công sở: 299k\n- Áo khoác nhẹ: 399k\n- Giày cao gót: 459k")
            self.add_message("Agent", "Bạn có muốn đặt mua không?")
            self.show_buttons(["Mua ngay", "Để sau"], self.end_chat)
        else:
            self.add_message("Agent", "Cảm ơn bạn đã ghé shop ❤️")
            self.show_buttons(["Bắt đầu lại"], self.restart_chat)

    def end_chat(self, choice):
        self.add_message("Bạn", choice)
        self.clear_buttons()

        if choice == "Mua ngay":
            self.add_message("Agent", "Đơn hàng của bạn đã được ghi nhận 🛒. Shop sẽ liên hệ với bạn sớm!")
        else:
            self.add_message("Agent", "Không sao, hẹn gặp lại bạn lần sau 😊")

        self.show_buttons(["Bắt đầu lại"], self.restart_chat)

    def restart_chat(self, _):
        self.clear_buttons()
        self.add_message("Agent", "Xin chào 👋! Bạn muốn tư vấn thời trang cho Nam hay Nữ?")
        self.show_buttons(["Nam", "Nữ"], self.choose_gender)

    def get_suggestion(self, gender, event):
        """Rule đơn giản gợi ý trang phục"""
        if gender == "Nam":
            if event == "Đi làm":
                return "Áo sơ mi + quần tây + giày da."
            elif event == "Đi chơi":
                return "Áo thun + quần jeans + sneaker."
            elif event == "Tiệc":
                return "Vest + sơ mi trắng + giày tây."
        else:  # Nữ
            if event == "Đi làm":
                return "Váy công sở hoặc sơ mi + chân váy."
            elif event == "Đi chơi":
                return "Áo croptop + quần jeans + sneaker."
            elif event == "Tiệc":
                return "Đầm dài + giày cao gót + clutch."
        return "Xin lỗi, tôi chưa có gợi ý cho trường hợp này."


# Khởi chạy app
if __name__ == "__main__":
    root = tk.Tk()
    app = FashionAgentApp(root)
    root.mainloop()
