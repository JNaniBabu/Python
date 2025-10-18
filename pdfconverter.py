import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

class ImageToPDFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to PDF Converter")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        
        self.image_paths = []

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(
            self.root, text="📄 Image to PDF Converter",
            font=("Arial", 16, "bold")
        )
        self.title_label.pack(pady=20)

        self.select_btn = tk.Button(
            self.root, text="Select Images", command=self.select_images,
            width=20, bg="#0078D7", fg="white", font=("Arial", 11)
        )
        self.select_btn.pack(pady=20)

        self.list_frame = tk.Frame(self.root)
        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side="right", fill="y")

        self.image_listbox = tk.Listbox(
            self.list_frame, yscrollcommand=self.scrollbar.set,
            width=50, height=10
        )
        self.image_listbox.pack(side="left", fill="both", expand=True)
        self.scrollbar.config(command=self.image_listbox.yview)

      
        self.convert_btn = tk.Button(
            self.root, text="Convert to PDF", command=self.convert_to_pdf,
            width=20, bg="#28A745", fg="white", font=("Arial", 11)
        )

    def select_images(self):
        files = filedialog.askopenfilenames(
            title="Select Image Files",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
        )

        if files:
            self.image_paths = list(files)
           
            self.image_listbox.delete(0, tk.END)
            for f in self.image_paths:
                filename = f.split("/")[-1] if "/" in f else f.split("\\")[-1]
                self.image_listbox.insert(tk.END, filename)

            self.title_label.pack_forget()
            self.select_btn.pack_forget()

            self.list_frame.pack(fill="both", expand=True, padx=20, pady=10)
            self.convert_btn.pack(pady=10)
        else:
            messagebox.showinfo("No Selection", "No images selected!")

    def convert_to_pdf(self):
        if not self.image_paths:
            messagebox.showwarning("No Images", "Please select images first.")
            return
        
        output_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save PDF As"
        )

        if not output_path:
            return

        try:
            images = [Image.open(img).convert("RGB") for img in self.image_paths]
            first_image, rest_images = images[0], images[1:]
            first_image.save(output_path, save_all=True, append_images=rest_images)

            messagebox.showinfo("Success", f"✅ PDF saved successfully:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToPDFConverterApp(root)
    root.mainloop()
