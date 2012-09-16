#!usr/bin/python

print """
	Mencari Tahun kabisat
	Kelompok I
"""

def kabisat():
	"mencari tahun Kabisat"
	tahun = input("Tahun Kabisat ? ")
	if tahun % 4 == 0 and tahun % 100 ==0 and tahun % 400 <> 0:
		print "salah"
	else:
		print tahun, "adalah tahun Kabisat"
	kabisat()

if __name__ == "__main__":
	kabisat()
