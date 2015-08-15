def simple_random(n, fp):
    '''
    with replacement

    If data are appended to the file during the function call,
    the appended data are ignored for the sampling.
    '''
    file_start = fp.tell()
    file_end = fp.seek(0, 2)
    
    lines_emitted = 0
    for i in count():
        fp.seek(randint(file_start, file_end))
        fp.readline()
        line = fp.readline()
        if len(line) > 0 and line[-1] == '\n':
            yield line
            lines_emitted += 1

        if lines_emitted == n:
            break
        if lines_emitted == 0 and i > 1000:
            raise EnvironmentError('It appears that this file contains no line breaks.')

def systematic(n, fp, offset = 0, repetitions = 1):
    file_start = fp.tell()
    file_end = fp.seek(0, 2)
    interval = int((file_end - file_start) / n)
    if interval == 0:
        interval = 1

    for repetition in range(repetitions):
        offset_adjustment = randint(0, interval)
        for base_offset in range(file_start, file_end, interval):
            offset = base_offset + offset_adjustment
            fp.seek(offset)
            fp.readline()
            line = fp.readline()
            
            if len(line) > 0 and line[-1] == '\n':
                yield line
