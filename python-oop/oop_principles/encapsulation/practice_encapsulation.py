# Utility functions
def is_valid_grade(grade: float) -> bool:
    return 0.0 <= grade <= 100.00


class Student:
    def __init__(self, name: str = '', student_id: int =0) -> None:
        self._id: int = student_id
        self._name: str = name
        self._grades: list[float] = []

    # Getters
    @property
    def id(self) -> int:
        return self._id
    @property
    def name(self) -> str:
        return self._name
    @property
    def grades(self) -> list[float]:
        return self._grades.copy()

    # Setters
    @id.setter
    def id(self, new_id: int) -> None:
        self._id = new_id
    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name
    @grades.setter
    def grades(self, new_grade: float) -> None:
        if not is_valid_grade(new_grade):
            raise ValueError(f"Grade {new_grade} must be between 0 and 100")
        self._grades.append(new_grade)

    def current_gpa(self) -> float:
        num_of_grades = len(self._grades)
        if num_of_grades == 0:
            return 0.0
        sum_of_grades = sum(self._grades)
        return sum_of_grades / num_of_grades

# Test cases
if __name__ == "__main__":
    # Test 1: Create a student and set basic info
    student1 = Student("Alice", 123)
    print(f"Student: {student1.name}, ID: {student1.id}")

    # Test 2: Add valid grades
    student1.grades = 85.0
    student1.grades = 92.0
    student1.grades = 78.0
    print(f"Grades: {student1.grades}")
    print(f"GPA: {student1.current_gpa()}")

    # Test 3: Try to add invalid grade (should raise ValueError)
    try:
        student1.grades = -10.0
    except ValueError as e:
        print(f"Error: {e}")

    # Test 4: Try to add another invalid grade
    try:
        student1.grades = 150.0
    except ValueError as e:
        print(f"Error: {e}")

    # Test 5: Check that grades list cannot be modified directly
    grades_copy = student1.grades
    grades_copy.append(100.0)  # This modifies the copy, not the original
    print(f"Grades after attempted modification: {student1.grades}")

    # Test 6: Student with no grades
    student2 = Student("Bob", 456)
    print(f"Student2 GPA (no grades): {student2.current_gpa()}")

    # Test 7: Add one grade
    student2.grades = 95.0
    print(f"Student2 GPA (one grade): {student2.current_gpa()}")
