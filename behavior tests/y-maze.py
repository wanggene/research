# y-maze test for ms model study
# total entrance
def tot_entr(seq):
	t_entr = len(seq) + 1
	return t_entr

# maximum alternation	
def max_alter(seq):
	m_alter = len(seq) -2
	return m_alter
	
# Spontaneous alternation
def spo_alter(seq):
	x = str(seq)
	re = 0
	i = (len(x)-1)
	while i > 1:
		if x[i] == x[i-1]:
			if x[i] == x[i-2]:
				re = re + 1
		i = i - 1
	return re		

# Repeated entrance 	
def rep_entr(seq):
	x = str(seq)
	re = 0
	i = 0
	while i < (len(x)-1):
		if x[i] == x[i+1]:
			re = re + 1
		i = i + 1
	return re

# the test py scripts for y-maze test results analysis, 
# the code is still under test
n = 0
sum_rep_en = 0
sum_spo_al = 0
while True:
	y =raw_input ('what is the sequence: ')
	total_en = tot_entr(y)
	max_al= max_alter(y)
	repeated_en = rep_entr(y)
	spo_al= spo_alter(y)
	
	sum_rep_en = sum_rep_en + repeated_en
	sum_spo_al = sum_spo_al + spo_al
	
	if y == 'done': break
	
	n = n + 1
	print 'THE RESULTS FOR TRAIL ID ', n
	print 'SEQUENCE IS: ', y
	print 'THE TOTAL ARM = ', total_en
	print 'THE MAX ENTR = ', max_al
	print 'THE REP ENTR = ', repeated_en
	print 'THE SPO ALTER = ', spo_al
	print '_______________________________________'
	
	
print '***********'
print 'Total trail No is: ', n
print 'Average repeated entrance is: ', sum_rep_en/n
print 'Average spontaneous alternation is: ', sum_spo_al/n
print 'Done'
