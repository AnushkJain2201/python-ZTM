hihi = 'me me me'

print(hihi[0])
print(hihi[7])

# [start: stop]
print(hihi[1: 5])

# [start: stop: stepover]
print(hihi[1: 5: 2])

# [start:]
print(hihi[3:])

# [:stop]
print(hihi[:5])

# [::stepover]
print(hihi[::2])

# [-1] the negative index means start from the last
print(hihi[-1])

# [::-1] it will reverse the string
print(hihi[::-1])