def study_schedule(permanence_period, target_time):
    if type(target_time) != int:
        return None

    period_counter = 0
    for student in permanence_period:
        start_study = student[0]
        end_study = student[1]

        if type(start_study) != int or type(end_study) != int:
            return None

        period = range(start_study, (end_study + 1))

        if target_time in period:
            period_counter += 1

    return period_counter
