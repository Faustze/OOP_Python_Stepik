def log_for(logfile, date_str):
    with (
        open(logfile, encoding='utf-8') as file_in,
        open(f'log_for_{date_str}.txt', 'w', encoding='utf-8') as file_out
    ):
        for line in file_in:
            d, *info = line.strip().split(maxsplit=1)
            if d == date_str:
                print(''.join(info), file=file_out)