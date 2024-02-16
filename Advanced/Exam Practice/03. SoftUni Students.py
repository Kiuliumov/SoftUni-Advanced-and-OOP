# unit test
def softuni_students(*args, **kwargs):
    courses = {}
    not_found = []

    for course_data in kwargs.items():
        course_id = course_data[0]
        course = course_data[1]
        if course_id not in courses:
            courses[course_id] = course

    student_data = []

    for data in args:
        course_id = data[0]
        username = data[1]

        if course_id in courses.keys():
            student_data.append(
                f"*** A student with the username {username} has successfully finished the course {courses[course_id]}!")
        else:
            not_found.append(username)
    student_data.sort()
    if not_found:
        not_found = sorted(not_found)
        invalid_students_msg = ", ".join(not_found)
        student_data.append(f"!!! Invalid course students: {invalid_students_msg}")

    return '\n'.join(student_data)
