def time_in_seconds(time):
    hh, mm, ss = time.split(':')
    return int(hh) * 3600 + int(mm) * 60 + int(ss)


def seconds_to_time(seconds):
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%i:%02i:%02i" % (hours, minutes, seconds)


#referesh 24 hours

def time_in_seconds(time):
    hh, mm, ss = time.split(':')
    return int(hh) * 3600 + int(mm) * 60 + int(ss)


def seconds_to_time(seconds):
    day = seconds // (24 * 3600) # if you need a day add it in the print
    seconds = seconds % (24 * 3600)
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return "%i:%02i:%02i" % (hours, minutes, seconds)

