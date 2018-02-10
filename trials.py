lines = ['name,age,reason', 'Richard Phillips Feynman, 69, for their fundamental work in quantum electrodynamics (QED) with deep-ploughing consequences for the physics of elementary particles\n', "Shin'ichirō Tomonaga, 73, for their fundamental work in quantum electrodynamics (QED) with deep-ploughing consequences for the physics of elementary particles\n", 'Julian Schwinger, 76, for their fundamental work in quantum electrodynamics (QED) with deep-ploughing consequences for the physics of elementary particles\n', 'Rudolf Ludwig Mössbauer, 82, for his researches concerning the resonance absorption of gamma radiation and his discovery in this connection of the effect which bears his name\n', 'Erwin Schrödinger, 73, for the discovery of new productive forms of atomic theory\n', 'Paul Dirac, 82, for the discovery of new productive forms of atomic theory\n', 'Maria Skłodowska-Curie, 66, for their joint researches on the radiation phenomena discovered by Professor Henri Becquerel\n', 'Pierre Curie, 46, for their joint researches on the radiation phenomena discovered by Professor Henri Becquerel\n']
stlines = []
for i in lines:
    stlines.append(i.strip())

#     print(stlines)

# Split each line based on the delimiter (which, in this case, is the comma)
# HINT: ref [4]

splines = []
for i in stlines:
    splines.append(i.split(","))

#     print(splines)

# Separate the header from the data
# HINT: ref [5]

header = splines[0]
splines = splines[1:len(lines)]

# Find "age" within the header
# (i.e., calculating the column index for "age")
# HINT: ref [6]

print('column index for "age" : ', header.index('age'))

# Calculate the number of data rows and columns
# HINT: [7]
num_data_rows = len(splines)
num_data_cols = len(splines[0])

# Sum the "age" values
# HINT: ref [8]

sum = 0
for i in splines:
    sum += int(i[1])

# Calculate the average age
avg_age = sum / len(splines)

# Print the results
# `format`: ref [9]
print("Number of rows of data: {}".format(num_data_rows))
print("Number of cols: {}".format(num_data_cols))
print("Average Age: {}".format(avg_age))