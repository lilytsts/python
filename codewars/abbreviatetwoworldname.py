def abbrev_name(name):
    result_string = name.split()[0][0:1].capitalize() + '.' + name.split()[1][0:1].capitalize()
    return result_string
