import numpy as np
import matplotlib.pyplot as plt

filename = "/users/didarsedghi/Desktop/Mossbauer Experiment/Iron Sample/Different Passes (Iron) (NEW)/550 pass ascii (i) NEW.asc"
fobj = open(filename, "r")
file_content = fobj.read()
print(file_content)
print(type(file_content))
print("Length of file string: ", len(file_content))

file_content = file_content.split()
print()
print("List: ", file_content)
print(type(file_content))
for i in range(0, 39):
    print(file_content[i])
print()
print()

print(file_content[1], file_content[3], type(file_content[1]))
print()

int_file = []

for i in file_content:
    int_file.append(float(i))

print(int_file[0], int_file[1], type(int_file[0]))



print()
print("Transformed list: ", int_file)

print()
print()
print()

channel = []
count = []


# Separate channel numbers.
for i in range(len(int_file)):
    if i == 0 or i % 2 == 0:
        channel.append(int_file[i])

print("Channel = ", channel)
print()

# Separate count numbers.
for j in range(len(int_file)):
    if j % 2 != 0:
        count.append(int_file[j])

print("Counts =", count)


# Defining a function that represents mean formula.
new_count = np.array(count)
print("Array of counts: ", new_count, type(new_count))
print(np.mean(new_count))

# Plotting counts as a function of channel
x_channel = channel
y_count = count

# mean 
y = [16.104 for i in x_channel]


plt.title("550 pass Iron sample")
plt.xlabel("Channels")
plt.ylabel("Total Counts")
plt.plot(x_channel, y_count, "o", color="r")
plt.plot(x_channel, y, "+")
plt.show()




















