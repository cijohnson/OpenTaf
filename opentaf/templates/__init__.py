"""OpenTaf templates
"""


def clone(template, values, filename):
    data = template.safe_substitute(values)
    with open(filename, 'w') as fd:
        fd.write(data)
