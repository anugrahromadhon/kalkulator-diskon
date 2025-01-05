import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class DiscountCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Discount Calculator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Label Judul
        title_label = tk.Label(self.root, text="Discount Calculator", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Frame untuk Input
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10)

        # Input Harga Asli
        ttk.Label(input_frame, text="Original Price (Rp):", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.original_price = ttk.Entry(input_frame, font=("Arial", 12))
        self.original_price.grid(row=0, column=1, padx=10, pady=5)

        # Input Diskon (%)
        ttk.Label(input_frame, text="Discount (%):", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.discount_percent = ttk.Entry(input_frame, font=("Arial", 12))
        self.discount_percent.grid(row=1, column=1, padx=10, pady=5)

        # Tombol Hitung
        calculate_button = ttk.Button(self.root, text="Calculate", command=self.calculate_discount)
        calculate_button.pack(pady=10)

        # Output Harga Diskon
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

    def calculate_discount(self):
        try:
            # Ambil input dari pengguna
            original_price = float(self.original_price.get())
            discount_percent = float(self.discount_percent.get())

            # Validasi input
            if original_price < 0 or discount_percent < 0 or discount_percent > 100:
                raise ValueError("Invalid input values")

            # Hitung harga setelah diskon
            discount_amount = original_price * (discount_percent / 100)
            final_price = original_price - discount_amount

            # Tampilkan hasil
            self.result_label.config(text=f"Final Price: Rp {final_price:,.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for price and discount.")

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = DiscountCalculator(root)
    root.mainloop()
