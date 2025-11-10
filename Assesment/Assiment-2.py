import os
import tkinter as tk
from tkinter import messagebox, filedialog



class Post:
    def __init__(self, username, title, content):
        self.username = username.strip()
        self.title = title.strip()
        self.content = content.strip()

    def filename(self):
        
        safe_username = "".join(c for c in self.username if c.isalnum() or c in ('_', '-'))
        safe_title = "".join(c for c in self.title if c.isalnum() or c in ('_', '-'))
        return f"{safe_username}_{safe_title}.txt"

    def save(self):
       
        if not self.username or not self.title or not self.content:
            raise ValueError("All fields must be filled out before saving.")
        
        file_path = os.path.join("posts", self.filename())
        os.makedirs("posts", exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"Author: {self.username}\n")
            f.write(f"Title: {self.title}\n\n")
            f.write(self.content)
        return file_path



class MiniBlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MiniBlog - Python Desktop App")
        self.root.geometry("600x500")
        self.root.config(bg="#f4f4f9")

        self.create_widgets()
        self.refresh_post_list()

    def create_widgets(self):
 
        tk.Label(self.root, text="📝 MiniBlog", font=("Arial", 20, "bold"), bg="#f4f4f9", fg="#333").pack(pady=10)

 
        tk.Label(self.root, text="Your Name:", bg="#f4f4f9").pack(anchor="w", padx=20)
        self.entry_name = tk.Entry(self.root, width=40)
        self.entry_name.pack(padx=20, pady=5)

      
        tk.Label(self.root, text="Post Title:", bg="#f4f4f9").pack(anchor="w", padx=20)
        self.entry_title = tk.Entry(self.root, width=40)
        self.entry_title.pack(padx=20, pady=5)

      
        tk.Label(self.root, text="Content:", bg="#f4f4f9").pack(anchor="w", padx=20)
        self.text_content = tk.Text(self.root, height=8, width=70)
        self.text_content.pack(padx=20, pady=5)

  
        btn_frame = tk.Frame(self.root, bg="#f4f4f9")
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="💾 Save Post", command=self.save_post, bg="#4CAF50", fg="white", width=15).pack(side="left", padx=5)
        tk.Button(btn_frame, text="🔄 Refresh Posts", command=self.refresh_post_list, bg="#2196F3", fg="white", width=15).pack(side="left", padx=5)

  
        tk.Label(self.root, text="Saved Posts:", bg="#f4f4f9").pack(anchor="w", padx=20, pady=(10, 0))
        self.listbox_posts = tk.Listbox(self.root, height=8, width=70)
        self.listbox_posts.pack(padx=20, pady=5)
        self.listbox_posts.bind('<<ListboxSelect>>', self.view_post)

   
        self.text_view = tk.Text(self.root, height=8, width=70, state='disabled', bg="#eef2f3")
        self.text_view.pack(padx=20, pady=10)

    def save_post(self):
        """Handle Save Post button click."""
        username = self.entry_name.get()
        title = self.entry_title.get()
        content = self.text_content.get("1.0", tk.END)

        try:
            post = Post(username, title, content)
            file_path = post.save()
            messagebox.showinfo("Success", f"Post saved successfully:\n{file_path}")
            self.entry_title.delete(0, tk.END)
            self.text_content.delete("1.0", tk.END)
            self.refresh_post_list()
        except ValueError as e:
            messagebox.showwarning("Validation Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")

    def refresh_post_list(self):
        """Refresh the list of saved posts."""
        self.listbox_posts.delete(0, tk.END)
        os.makedirs("posts", exist_ok=True)
        for filename in os.listdir("posts"):
            if filename.endswith(".txt"):
                self.listbox_posts.insert(tk.END, filename)

    def view_post(self, event):
        """Display selected post in the text area."""
        try:
            selected = self.listbox_posts.get(self.listbox_posts.curselection())
            file_path = os.path.join("posts", selected)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.text_view.config(state='normal')
            self.text_view.delete("1.0", tk.END)
            self.text_view.insert(tk.END, content)
            self.text_view.config(state='disabled')
        except IndexError:
            pass  
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found!")
        except Exception as e:
            messagebox.showerror("Error", str(e))



if __name__ == "__main__":
    root = tk.Tk()
    app = MiniBlogApp(root)
    root.mainloop()
