from time import sleep

# Initializing the variable x
x = 0

# Pretty format gotten from here: https://www.youtube.com/watch?v=5uVXbb1ymVs
while True:
# Creating a .txt file to check elapsed time in case of power outages
# Which means that it is dynamically showing the info in only one line, cool huh?
    f = open('stopwatch.txt', 'w+')
    f.write('Current Time(Fuck Cuba)')
    f.write('\n')
    f.write('--------------------------')
    f.write('\n')
# Appending to the variable x each second
    x += 1
    m, s = divmod(x, 60)
    h, m = divmod(m, 60)
# Mission Accomplished.
    print(str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2))
# Writing the output to the .txt file
    f.write(str(str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)))
# Closing the .txt file
    f.close()
# This is what makes every append to become an actual second, which allow us to track the time effectively
    sleep(1)


