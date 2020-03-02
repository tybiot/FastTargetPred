#!/usr/bin/env python3

# Script written in Python3.
# This script converts the CSV file that contains fingerprints generated by MayChemTools into a binary file readable by FastTargetPred.
# The first column represents the "CompoundID" of the molecules.
# In the MayaChemTools CSV file, the fingerprint must be written in hexadecimal format (option -b HexadecimalString).
# Check the MayaChemTools manual to ensure you properly format the CSV file.

import sys, os, codecs

input_filename = sys.argv[1]
output_filename = os.path.splitext(input_filename)[0] + ".bfp"
output_listname = os.path.splitext(input_filename)[0] + ".id"

infile   = open(input_filename)
outlist  = open(output_listname, "w")
outfile  = open(output_filename, "wb")

# read 
line = infile.readline()
line = infile.readline()

while line:
	rawMolID = line.split(",")[0]
	MolID    = rawMolID.replace('"','')
	rawFP    = line.split("Ascending;",1)[1]
	raw2FP   = rawFP.replace('"\n','')

	lenid = len(MolID).to_bytes(1, byteorder='big', signed=True)
	outlist.write(MolID+"\n")
	outfile.write(lenid)
	outfile.write(codecs.encode(MolID, 'ascii'))
	outfile.write(codecs.decode(raw2FP, 'hex'))
	line     = infile.readline()
infile.close()
outlist.close()
