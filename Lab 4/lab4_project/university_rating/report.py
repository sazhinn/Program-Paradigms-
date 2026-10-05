def format_average(value):
    return "—" if value is None else f"{value:.2f}"


def format_rating(rows):
    lines = ["Рейтинг группы"]
    for position, row in enumerate(rows, start=1):
        average = format_average(row["average"])
        letter = row["letter"] or "—"
        lines.append(
            f"{position}. {row['name']}: {average} — {row['status']}, оценка {letter}"
        )
    return "\n".join(lines)
