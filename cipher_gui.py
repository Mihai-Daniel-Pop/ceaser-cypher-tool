import tkinter as tk
from tkinter import ttk, messagebox
from cesar import implement_caesar_cipher


class CaesarCipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher")
        self.root.geometry("500x450")
        self.root.resizable(False, False)

        # Colors
        self.bg_color = "#f0f4f8"
        self.accent_color = "#6366f1"
        self.text_color = "#1e293b"
        self.card_color = "#ffffff"

        self.root.configure(bg=self.bg_color)

        self.style = ttk.Style()
        self.style.configure("Card.TFrame", background=self.card_color)
        self.style.configure("Title.TLabel", font=("Segoe UI", 20, "bold"), foreground=self.accent_color)
        self.style.configure("Subtitle.TLabel", font=("Segoe UI", 10), foreground="#64748b")
        self.style.configure("Input.TLabel", font=("Segoe UI", 11), foreground=self.text_color, background=self.card_color)

        self.create_widgets()

    def create_widgets(self):
        card = ttk.Frame(self.root, style="Card.TFrame", padding=30)
        card.place(relx=0.5, rely=0.5, anchor="center")

        title = ttk.Label(card, text="Caesar Cipher", style="Title.TLabel", background=self.card_color)
        title.pack(pady=(0, 5))

        subtitle = ttk.Label(card, text="Encrypt and decrypt your messages", style="Subtitle.TLabel", background=self.card_color)
        subtitle.pack(pady=(0, 25))

        msg_label = ttk.Label(card, text="Message:", style="Input.TLabel")
        msg_label.pack(anchor="w", pady=(0, 5))

        self.message_entry = tk.Entry(card, font=("Segoe UI", 12), width=35,
                                       relief="solid", borderwidth=1,
                                       highlightthickness=2, highlightcolor=self.accent_color)
        self.message_entry.pack(fill="x", pady=(0, 15), ipady=8)
        self.message_entry.insert(0, "")

        # Key input
        key_frame = ttk.Frame(card, style="Card.TFrame")
        key_frame.pack(fill="x", pady=(0, 15))

        key_label = ttk.Label(key_frame, text="Shift Key (1-25):", style="Input.TLabel")
        key_label.pack(side="left")

        self.key_var = tk.IntVar(value=3)
        self.key_spinbox = tk.Spinbox(key_frame, from_=1, to=25, textvariable=self.key_var,
                                       width=5, font=("Segoe UI", 12), relief="solid",
                                       borderwidth=1)
        self.key_spinbox.pack(side="right")

        btn_frame = ttk.Frame(card, style="Card.TFrame")
        btn_frame.pack(fill="x", pady=(0, 20))

        self.encrypt_btn = tk.Button(btn_frame, text="Encrypt", font=("Segoe UI", 11, "bold"),
                                      bg=self.accent_color, fg="white",
                                      activebackground="#4f46e5", activeforeground="white",
                                      relief="flat", cursor="hand2",
                                      command=self.encrypt)
        self.encrypt_btn.pack(side="left", expand=True, fill="x", padx=(0, 10), ipady=10)

        self.decrypt_btn = tk.Button(btn_frame, text="Decrypt", font=("Segoe UI", 11, "bold"),
                                      bg="#e2e8f0", fg=self.text_color,
                                      activebackground="#cbd5e1", activeforeground=self.text_color,
                                      relief="flat", cursor="hand2",
                                      command=self.decrypt)
        self.decrypt_btn.pack(side="right", expand=True, fill="x", ipady=10)

        result_label = ttk.Label(card, text="Result:", style="Input.TLabel")
        result_label.pack(anchor="w", pady=(0, 5))

        self.result_text = tk.Text(card, font=("Segoe UI", 12), width=35, height=3,
                                    relief="solid", borderwidth=1,
                                    wrap="word", state="disabled",
                                    bg="#f8fafc", fg=self.text_color)
        self.result_text.pack(fill="x", pady=(0, 10))

        self.copy_btn = tk.Button(card, text="Copy to Clipboard", font=("Segoe UI", 10),
                                   bg="#10b981", fg="white",
                                   activebackground="#059669", activeforeground="white",
                                   relief="flat", cursor="hand2",
                                   command=self.copy_result)
        self.copy_btn.pack(fill="x", ipady=8)

        self.root.bind("<Return>", lambda e: self.encrypt())

    def encrypt(self):
        self.process_message(decrypt=False)

    def decrypt(self):
        self.process_message(decrypt=True)

    def process_message(self, decrypt=False):
        message = self.message_entry.get()
        if not message:
            messagebox.showwarning("Empty Message", "Please enter a message to process.")
            return

        key = self.key_var.get()
        result = implement_caesar_cipher(message, key, decrypt=decrypt)

        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert("1.0", result)
        self.result_text.config(state="disabled")

    def copy_result(self):
        result = self.result_text.get("1.0", tk.END).strip()
        if result:
            self.root.clipboard_clear()
            self.root.clipboard_append(result)
            self.root.update()


if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherGUI(root)
    root.mainloop()
