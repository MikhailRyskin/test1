in_file = open('numbers.txt', 'r')
summ = 0
for line in in_file:
    summ += int(line)
in_file.close()

out_file = open('answer.txt.', 'w')
out_file.write(str(summ))
out_file.close()
