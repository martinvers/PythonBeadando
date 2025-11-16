class StudentStorageVM:
    def __init__(self, filename: str):

        self.filename = filename
        self.students: list[tuple[str, int]] = []

    def add_student(self, name: str, grade: int) -> None:

        self.students.append((name, grade))

    def delete_student(self, index: int) -> None:

        if 0 <= index < len(self.students):
            self.students.pop(index)

    def calculate_average(self):

        if not self.students:
            return None
        total = sum(grade for _, grade in self.students)
        return total / len(self.students)

    def save_to_file(self) -> None:

        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                for name, grade in self.students:
                    f.write(f"{name};{grade}\n")
        except Exception as e:
            print(f"Hiba mentés közben: {e}")

    def load_from_file(self):

        self.students = []
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(";")
                    if len(parts) != 2:
                        continue
                    name = parts[0]
                    try:
                        grade = int(parts[1])
                    except ValueError:
                        continue
                    self.students.append((name, grade))
        except FileNotFoundError:

            pass
        except Exception as e:
            print(f"Hiba betöltés közben: {e}")

        return self.students
