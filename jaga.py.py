fi = open('jagasis.txt', 'r')
lines = fi.readlines()

numbers = []
for el in lines:
    numbers.append(int(el))

j_sum = numbers [1]
m_sum = numbers [2] + numbers[3] + numbers[4] + numbers [5] + numbers [6] + numbers [7]

i = 1
while i < 8:
    m_sum = m_sum + numbers [1]
    i += 1
    
print(j_sum)
print(m_sum)

