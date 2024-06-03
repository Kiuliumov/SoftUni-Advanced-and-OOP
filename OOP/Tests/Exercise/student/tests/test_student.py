from unittest import TestCase, main

from project.student import Student

class TestStudent(TestCase):

    def setUp(self):
        self.student = Student('TestStudent')

    def test_init(self):
        self.assertEqual(self.student.name, 'TestStudent')
        self.assertEqual(self.student.courses, {})

    def test_class_constructor_with_empty_name(self):
        student = Student('')
        self.assertEqual(student.name, '')
        self.assertEqual(student.courses, {})

    def test_enroll_if_new_course_added_with_notes_y(self):
        result = self.student.enroll('TestCourse', ['Here are some test notes.', 'This is a test.', 'This is another test', 'This is another test'], 'Y')
        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual(self.student.courses, {'TestCourse': ['Here are some test notes.', 'This is a test.', 'This is another test', 'This is another test']})

    def test_enroll_if_new_course_added_with_notes_empty_string(self):
        result = self.student.enroll('TestCourse', ['Here are some test notes.', 'This is a test.', 'This is another test', 'This is another test'])
        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual(self.student.courses, {'TestCourse': ['Here are some test notes.', 'This is a test.', 'This is another test', 'This is another test']})

    def test_enroll_if_new_course_added_without_notes(self):
        result = self.student.enroll('TestCourse', (), 'N')
        self.assertEqual('Course has been added.', result)
        self.assertEqual(self.student.courses, {'TestCourse': []})

    def test_enroll_if_existing_course_added(self):
        self.student.enroll('TestCourse', ['Here are some test notes.', 'Test', 'Test this', 'Test', 'Test this'], 'Y')
        result = self.student.enroll('TestCourse', ['Here are some test notes.', 'This is a test.', 'This is another test', 'This is another test'])
        self.assertEqual('Course already added. Notes have been updated.', result)
        self.assertEqual(self.student.courses, {'TestCourse': ['Here are some test notes.', 'Test', 'Test this', 'Test', 'Test this', 'Here are some test notes.', 'This is a test.', 'This is another test', 'This is another test']})

    def test_enroll_with_empty_notes_and_add_course_notes_y(self):
        result = self.student.enroll('NewCourse', [], 'Y')
        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual(self.student.courses, {'NewCourse': []})

    def test_enroll_with_empty_notes_and_add_course_notes_empty_string(self):
        result = self.student.enroll('NewCourse', [])
        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual(self.student.courses, {'NewCourse': []})

    def test_enroll_with_empty_notes_and_add_course_notes_n(self):
        result = self.student.enroll('AnotherCourse', [], 'N')
        self.assertEqual('Course has been added.', result)
        self.assertEqual(self.student.courses, {'AnotherCourse': []})

    def test_add_notes_if_not_exists_course(self):
        with self.assertRaises(Exception) as contx:
            self.student.add_notes('TestCourse1', 'Here are some')
        self.assertEqual('Cannot add notes. Course not found.', str(contx.exception))

    def test_add_notes_if_exists_course(self):
        self.student.courses = {'TestCourse1': ['Here is a note']}
        self.student.add_notes('TestCourse1', 'Here is a note')
        self.assertEqual(self.student.courses, {'TestCourse1': ['Here is a note', 'Here is a note']})

    def test_add_empty_string_as_notes(self):
        self.student.courses = {'TestCourse1': ['Here is a note']}
        self.student.add_notes('TestCourse1', '')
        self.assertEqual(self.student.courses, {'TestCourse1': ['Here is a note', '']})

    def test_leave_course_if_not_exists(self):
        with self.assertRaises(Exception) as contx:
            self.student.leave_course('TestCourse1')
        self.assertEqual('Cannot remove course. Course not found.', str(contx.exception))

    def test_leave_course_if_exists(self):
        self.student.courses = {'TestCourse1': []}
        result = self.student.leave_course('TestCourse1')
        self.assertEqual('Course has been removed', result)
        self.assertEqual(self.student.courses, {})


    def test_leave_course_when_no_courses_exist(self):
        self.student.courses = {}
        with self.assertRaises(Exception) as contx:
            self.student.leave_course('NonExistentCourse')
        self.assertEqual('Cannot remove course. Course not found.', str(contx.exception))

if __name__ == '__main__':
    main()
