def students_credits(*args):
    course_with_credits = {}
    all_credits = 0
    for rough_info in args:
        info = rough_info.split('-')
        course_name = info[0]
        credits_student = int(info[1])
        max_test_points = int(info[2])
        students_points = int(info[3])

        percentage_of_result = students_points / max_test_points
        credits_he_gets = percentage_of_result * credits_student
        all_credits += credits_he_gets

        course_with_credits[course_name] = credits_he_gets

    result = []

    if all_credits >= 240:
        result.append(f"Diyan gets a diploma with {all_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {240 - all_credits:.1f} credits more for a diploma.")

    sorted_course = dict(sorted(course_with_credits.items(), key=lambda kvp: -kvp[1]))

    for course, current_credits in sorted_course.items():
        result.append(f'{course} - {current_credits:.1f}')

    return '\n'.join(result)


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
