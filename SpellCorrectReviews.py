import gzip

from SpellingCorrector import SpellingCorrector as SC

# This is our spelling corrector
corrector = SC.SpellingCorrector()



with gzip.open('/media/pat/sda3/toBeCorrected/very-pos-10.txt.gz', 'rb') as fin, gzip.open('/media/pat/sda3/toBeCorrected/corrected/very-pos-corrected-10.txt.gz', 'wb') as out:
	count = 0
	for review in fin:
		count += 1
		
		correct = [corrected for corrected in corrector.CorrectSpelling(review.strip())]
		
		out.write(' '.join(correct) + '\n')
		
		print count

# Split the data into 10k review chunks for 'parallelism'
'''
for i in range(4,40):
	with gzip.open('/media/pat/sda3/toBeCorrected/very-pos-' + str(i) + '.txt.gz','wb') as out:
		with gzip.open('/media/pat/sda3/very-pos.txt.gz', 'rb') as fin:
			counter = 0
			for review in fin:
				counter += 1
			
				if counter > 10000 * (i-2) and counter <= 10000 * (i-1):
					out.write(review)
		
					print counter
'''
