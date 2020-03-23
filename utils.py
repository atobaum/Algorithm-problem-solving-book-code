def parse(inputs):
    inputs = inputs.split('\n')
    inputs.reverse()
    return [[int(i) for i in l.split()] for l in inputs]
