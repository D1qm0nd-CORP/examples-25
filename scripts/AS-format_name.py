def format_name(full_name):
    parts = full_name.split()
    if len(parts) == 3:
        name, patronymic, surname = parts
        return f"{surname} {name[0]}.{patronymic[0]}."
    else:
        raise Exception("Некорректные данные")

print(format_name(input()))
