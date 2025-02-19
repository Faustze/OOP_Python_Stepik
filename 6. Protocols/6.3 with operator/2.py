def non_closed_files(files: list):
    for file in files:
        if file.closed:
            continue
        yield file