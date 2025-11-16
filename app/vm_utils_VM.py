class VMHelper:


    def format_student(self, name: str, grade: int) -> str:

        return f"{name} – {grade}"


def validate_VM_student(name: str, grade_text: str):

    name = name.strip()
    grade_text = grade_text.strip()

    if not name:
        return False, "A név nem lehet üres!", None

    if not grade_text:
        return False, "A jegy nem lehet üres!", None

    if not grade_text.isdigit():
        return False, "A jegy csak szám lehet!", None

    grade = int(grade_text)
    if not 1 <= grade <= 5:
        return False, "A jegy 1 és 5 közötti egész szám legyen!", None

    return True, None, grade
