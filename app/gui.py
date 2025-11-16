import tkinter as tk
from tkinter import messagebox

from storage import StudentStorageVM
from vm_utils_VM import VMHelper, validate_VM_student


class StudentApp:
    def __init__(self, root):
        self.root = root

  
        self.storage = StudentStorageVM("students_VM.txt")
        self.helper = VMHelper()  # saját VM-es osztály példánya

        self.title_label = tk.Label(
            root,
            text="Diákjegy-kezelő (VM)",
            font=("Arial", 18, "bold")
        )
        self.title_label.pack(pady=10)


        self.name_label = tk.Label(root, text="Diák neve:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root, width=35)
        self.name_entry.pack(pady=4)


        self.grade_label = tk.Label(root, text="Jegy (1–5):")
        self.grade_label.pack()

        self.grade_entry = tk.Entry(root, width=10)
        self.grade_entry.pack(pady=4)


        self.add_button = tk.Button(
            root,
            text="Hozzáadás",
            command=self.add_student
        )
        self.add_button.pack(pady=6)


        self.student_listbox = tk.Listbox(root, width=45, height=10)
        self.student_listbox.pack(pady=10)


        self.delete_button = tk.Button(
            root,
            text="Kijelölt törlése",
            command=self.delete_selected
        )
        self.delete_button.pack(pady=5)


        self.average_button = tk.Button(
            root,
            text="Átlag számítása",
            command=self.show_average
        )
        self.average_button.pack(pady=5)


        self.save_button = tk.Button(
            root,
            text="Mentés fájlba",
            command=self.save_data
        )
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(
            root,
            text="Betöltés fájlból",
            command=self.load_data
        )
        self.load_button.pack(pady=5)

    def add_student(self):

        name = self.name_entry.get()
        grade_text = self.grade_entry.get()

        ok, error, grade = validate_VM_student(name, grade_text)
        if not ok:
            messagebox.showerror("Hiba", error)
            return

        name = name.strip()
        self.storage.add_student(name, grade)


        display_text = self.helper.format_student(name, grade)
        self.student_listbox.insert(tk.END, display_text)

        self.name_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)

    def delete_selected(self):

        selected = self.student_listbox.curselection()

        if not selected:
            messagebox.showwarning("Figyelmeztetés", "Nincs kijelölt elem!")
            return

        index = selected[0]
        self.student_listbox.delete(index)
        self.storage.delete_student(index)

    def show_average(self):

        avg = self.storage.calculate_average()

        if avg is None:
            messagebox.showinfo("Átlag", "Nincs jegy a listában!")
        else:
            messagebox.showinfo("Átlag", f"A jegyek átlaga: {avg:.2f}")

    def save_data(self):

        self.storage.save_to_file()
        messagebox.showinfo("Mentve", "Adatok mentve a fájlba!")

    def load_data(self):

        students = self.storage.load_from_file()

        self.student_listbox.delete(0, tk.END)

        for name, grade in students:
            display_text = self.helper.format_student(name, grade)
            self.student_listbox.insert(tk.END, display_text)

        messagebox.showinfo("Betöltve", "Adatok betöltve!")
