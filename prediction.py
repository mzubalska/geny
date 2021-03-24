# -*- coding: utf-8 -*-

def genScan(plik1):
    #input - wynik z serwisu genScan
	p = open(plik1,'r+')
	s = {}
	i = 0
	empty = 0
	gene = 0
	end = 0
 
	for line in p:
		tab = line.split()             
		if tab != []:
			empty = 0
			if gene == 0:
				gene = 1
				s[i] = []
				s[i] += [tab[2], int(tab[3])]
				end = tab[4]
			else:
				end = tab[4]
		else:
			empty += 1
			if empty == 2:
				s[i] += [int(end)]
				i += 1
				gene = 0
	p.close()
	return s #słownik, keys: nr genu, values:[(+/-), start genu, koniec genu]  
	
def geneMark(plik2):
    #input - wynik z serwisu geneMark
	p = open(plik2,'r+')
	s = {}
	gene = 0
	i = 0
 
	for line in p:
		tab = line.split()
		if tab != []:
			if gene == 0:
				gene = 1
				i = int(tab[0])
				s[i] = []
				s[i] += [tab[2], int(tab[4])]
				end = tab[5]
			else:
				end = tab[5]
		else:
			gene = 0
			s[i] += [int(end)]
	p.close()
	return s #słownik, keys: nr genu, values:[(+/-), start genu, koniec genu]

 
def porownanie(p1, p2, n1, n2, zakres):
    #prwnanie wynikow z dwuch serwisow,
    #dodaje informacje o wystepowaniu nazwy programu gdzie rowniez wykryto dany gen
	i=1
	j=1
     
	while i <= len(p1.keys()) and j <= len(p2.keys()):
		if p1[i][0] == p2[j][0]:
			if (abs(p1[i][1]-p2[j][1]) <= zakres) and (abs(p1[i][2] - p2[j][2]) <= zakres):
				p1[i] += [n2]
				p2[j] += [n1]
				i += 1
				j += 1
			else:
				if p1[i][2] < p2[j][2]:
					i += 1
				else:
					j += 1
		else:
			if p1[i][2] < p2[j][2]:
				i += 1
			else:
				j += 1
    
def zapis(p, metoda, output):
    #	output.write(metoda + '\n')
	output.write(metoda + ',' + ' ' + ',' + 'start' + ',' + 'end' + '\n')
 
	for i in p.keys():
		output.write("Gen " + str(i) + ',')
		for j in range(len(p[i])):
			output.write(str(p[i][j]))
			if j != (len(p[i])-1):
				output.write(',')
		output.write('\n')
  
	output.write('\n')    
	
def prediction( plik1, plik2, zakres):
      #input wyniki z serwisow (genScan,geneMark),o ile moga roznic sie koordynaty poczatku i konca genu by wciaz byly uznane za te same geny

	p1=genScan(plik1)
	p2=geneMark(plik2)
 
	porownanie(p1, p2, "genScan", "geneMark", zakres)
 
	output=open("prediction.csv",'w+')
 
	zapis(p1, "GENSCAN", output)
	zapis(p2, "GENEMARK", output)
 
	output.close()
	

	
prediction("genScan.txt", "geneMark.txt", 800)
