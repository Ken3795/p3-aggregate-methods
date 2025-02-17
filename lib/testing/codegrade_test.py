import pytest
from enrollment import Student, Course, Enrollment
from datetime import datetime  # <-- Import datetime here

class TestStudent:

    def test_course_count(self):
        # Create courses
        course1 = Course("Math 101")
        course2 = Course("History 101")
        
        # Create a student and enroll in courses
        student = Student("Alice")
        student.enroll(course1)
        student.enroll(course2)
        
        # Test course count method
        assert student.course_count() == 2
    
    def test_aggregate_average_grade(self):
        # Create courses
        course1 = Course("Math 101")
        course2 = Course("History 101")
        
        # Create a student and enroll in courses
        student = Student("Alice")
        student.enroll(course1)
        student.enroll(course2)
        
        # Add grades to enrollments
        enrollment1 = student.get_enrollments()[0]
        enrollment2 = student.get_enrollments()[1]
        
        student.add_grade(enrollment1, 90)
        student.add_grade(enrollment2, 80)
        
        # Test average grade calculation
        assert student.aggregate_average_grade() == 85.0
    
    def test_aggregate_enrollments_per_day(self):
        # Clear previous enrollments to avoid carrying over from other tests
        Enrollment.clear_all_enrollments()

        # Create courses
        course1 = Course("Math 101")
        course2 = Course("History 101")

        # Create students and enroll
        student1 = Student("Alice")
        student2 = Student("Bob")

        student1.enroll(course1)
        student2.enroll(course1)
        student2.enroll(course2)

        # Aggregate enrollments by date
        enrollments_per_day = Enrollment.aggregate_enrollments_per_day()

        # Print the enrollments per day to see what's being returned
        print("Enrollments per day:", enrollments_per_day)

        # Assuming the current date is 2025-02-17, we expect 3 enrollments today.
        today = datetime.now().date()  # datetime is now imported correctly
        print(f"Today's date: {today}")

        # Assert that the enrollments for today match the expected value (3 in this case)
        assert enrollments_per_day[today] == 3
