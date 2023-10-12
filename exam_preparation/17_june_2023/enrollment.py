def gather_credits(needed_credits, *args):
    courses = []
    success = False
    current_credits = 0

    for course_info in args:
        course_name = course_info[0]
        course_credits = int(course_info[1])

        if course_name in courses:
            continue

        current_credits += course_credits
        courses.append(course_name)

        if current_credits >= needed_credits:
            success = True
            break

    if success:
        return f"Enrollment finished! Maximum credits: {current_credits}.\nCourses: {', '.join(sorted(courses))}"
    else:
        return f"You need to enroll in more courses! You have to gather {abs(needed_credits - current_credits)} credits more."


print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
