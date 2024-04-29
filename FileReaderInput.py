def read_data_from_file(file_path):
    lines = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                lines.append(line.strip())
    except IOError as e:
        print("Error reading file:", e)
    return lines