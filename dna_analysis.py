# Name: Matthew Schult
# Evergreen Login: schmat18
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


#---------------------------------------------------------------------------------
# cmd cd to this file then type "python dna_analysis.py data\\sample_1.fasq"
#---------------------------------------------------------------------------------


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0


#####My Work######

at_count=0
gCount=0
cCount=0
tCount=0
aCount=0
sumCount=0
totalCount=0
seqLength=0
atcgRatio=0.0
gcClassification=""
##################


# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    #if bp == 'C' or bp == 'G':
        # increment the count of gc
        #gc_count = gc_count + 1
    if bp =='C':
        cCount = cCount+1
        
    elif bp=='G':
        gCount =gCount+1
        
    elif bp=='T':
        tCount=tCount+1
        
    elif bp=='A':
        aCount=aCount+1


at_count= (aCount + tCount)
gc_count= (gCount + cCount)
# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count


at_content = float(at_count) / total_count

sumCount= (gCount + cCount + tCount + aCount)

atcgRatio= float(at_content/gc_content)

seqLength=total_count
if(gc_content >0.6):
    gcClassification = "High GC Classification"
elif(gc_content> 0.4):
    gcClassification = "Moderate GC Classification"
else:
    gcClassification = "Low GC Classification"
    
# Print the answer
print 'GC-content:', gc_content
print 'AT-content:',at_content
print 'gCount:',gCount
print 'cCount:',cCount
print 'tCount:',tCount
print 'aCount:',aCount
#print 'cgCount:',gc_count
#print 'atCount:',at_count
print 'sumCount:',sumCount
print 'totalCount:',total_count
print 'seqLength:',seqLength
print 'at/cgRatio:',atcgRatio
print 'gcClassification:',gcClassification