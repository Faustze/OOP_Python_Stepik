def print_file_content(filename: str):
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            print(f.read())
    except Exception as e:
        print(e)
