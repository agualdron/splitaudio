#!/usr/bin/python

import soundfile as sf
#import sounddevice as sd
import os

import os.path
import sys, getopt

version="0.1"

def sliceAudio(iFilename, names, times, verbose_en):
	#open aduio
	data, fs = sf.read(iFilename)
	
	times.append(len(data)*fs)
	
	# calculate time laps
	for i in range(len(times)-1):
		startPoint = times[i]*fs
		endPoint = times[i+1]*fs
		
		# write slice audio file
		sf.write(names[i]+'.wav', data[startPoint:endPoint], fs)
		
		if verbose_en == True:
			print names[i]+'.wav'

def getNamesAndTimes(iFile):
	times = []
	names = []
	with open(iFile, 'r') as list_file:
		for line in list_file:
			line = line.replace('.', '-')
			line = line.replace(',', ' ')
			line = line.replace(')', '-')
			line = line.replace('(', '-')
			line = line.strip()
			# find the ':' to identify the time
			
			
			
			idx = line.find(':')
			
			if len(line)>6:		# one leter for the name and 00:00
				if idx == -1:
					times.append(0)
					names.append(line.strip())
				else:
					if line.count(':')==1:						
						sec = int(line[idx-2:idx])*60+int(line[idx+1:idx+3])
						times.append(sec)
						names.append(line[0:idx-2].strip())
					elif line.count(':')==2:
						sec = int(line[idx-2:idx])*3600+int(line[idx+1:idx+3]*60)+int(line[idx+4:idx+7])
						times.append(sec)
						names.append(line[0:idx-2].strip())
						
				
	return names,times
	
def convert2fmt(names, fmt, keep_wav, verbose_en):
	#Convert to mp3
	for name in names:
		if verbose_en == True:
			cmd = 'avconv -i '+'"'+name+'.wav'+'" '+'"'+name+'.'+fmt+'"'
			print cmd
		else:
			cmd = 'avconv -i '+'"'+name+'.wav'+'" '+'"'+name+'.'+fmt+'"'+' -v quiet'
		os.system(cmd)
		#print cmd
		if verbose_en == True:
			print '******************************************************'
			print name+'.'+fmt, 'Created'
			print '******************************************************'
		if keep_wav == False:
			cmd = 'rm '+'"'+name+'.wav'+'" '
			#print cmd
			os.system(cmd)
			if verbose_en == True:
				print name+'.'+'wav', 'Removed'
				print '******************************************************'
	
def showHelp():
	print "----------------------------------------------SPLIT AUDIO-----------------------------------------------"
	print "splitaudio is a python program to split audio into tracks"
	print "from a list of names and times."
	print " "
	print "Usage:"
	print "         splitaudio --input <input_file.wav> --list <list_of_names.txt>  ..."
	print " "
	print "Arguments:"
	print ".......Options.......   .....Arguments.....   .............Description.................................."
	print "  Long          Short" 
	print "--input        -i       <input_file.wav>      : input file, should be a wav file."
	print "--list         -l       <list_of_names>       : a text file with the list of names and times."
	print "--format       -f       <mp3 | aiff | ogg>    : the output audio format. default is wav"
	print "--keep-wav     -k                             : keep the sliced .wav files if other format is configured"
	print "--help         -h                             : display help"
	print "--verbose      -v                             : print messages"
	print " "
	print "Format of the lines in list: "
	print "   <track number>. <Name> <minutes:seconds>"
	print "   <##>. <Name> <mm:ss>"
	print "   Example:"
	print "            3. Hello (Buddy) 8:07"
	print " "
	print " "

#iFilename = 'Man From Another Time - Seasick Steve (full album)-dyb6ymIaWjc.wav'

if __name__ == "__main__":
	
	# identify the arguments
	# --input  		-i	<input_file.wav> 			: input file, should be a wav file.
	# --list   		-l	<list_of_names>  			: a text file with the list of names and times.
	# --format		-f	<mp3 | aiff | ogg>			: the output audio format. default is wav
	# --keep-wav	-k								: keep the sliced .wav files if other format is configured
	# --help		-h	<argument>					: display help
	# --verbose		-v								: print messages
	
	argv = sys.argv[1:]
	
	short_opt = "i:l:f:khv"
	long_opt  = ['input=', 'list=', 'format=', 'keep-wav', 'help', 'verbose']
	supported_formats = ['mp3', 'aiff', 'ogg']
	
	iaudiofile = ''
	ilistfile  = ''	
	au_format  = ''
	keep_wav_en= False
	help_en    = False
	verbose_en = False
	
	#parse arguments
	try:
		opts, args = getopt.getopt(argv, short_opt, long_opt)
	except getopt.GetoptError:
		print "error in command"
		print "splitaudio --input <input_file.wav> --list <list_of_names.txt>"
		sys.exit(2)
	
	#get configurations form arguments
	for opt, arg in opts:
		if opt in ("-i", "--input"):
			if os.path.isfile(arg) and os.access(arg, os.R_OK):
				iaudiofile = arg
			else:
				print "error when trying to access "+arg
				print "Either file is missing or is not readable"
				sys.exit(2)
		elif opt in ('-l', '--list'):
			if os.path.isfile(arg) and os.access(arg, os.R_OK):
				ilistfile = arg
			else:
				print "error when trying to access "+arg
				print "Either file is missing or is not readable"
				sys.exit(2)
		elif opt in ('-f', '--format'):
			if arg in supported_formats:
				au_format = arg
			else:
				print "format not supported"
				sys.exit(2)
		elif opt in ('-k', '--keep-wav'):
			keep_wav_en = True
		elif opt in ('-h', '--help'):
			help_en = True
		elif opt in ('-v', '--verbose'):
			verbose_en = True
	
	#help		
	if help_en == True:
		showHelp()
		
	if iaudiofile=='' or ilistfile=='':
		showHelp()
		sys.exit(1)
	
	# files
	if verbose_en == True:
		print "Input Audio File    : "+iaudiofile
		print "Output List of Names: "+ilistfile
	
	print "Getting the Names and times form the list..."
	names, times = getNamesAndTimes(ilistfile)
	
	if verbose_en == True:
		print "Time [sec]       Name"
		for k in range(0, len(names)):
			print "  ", str(times[k]).ljust(10), "  ", names[k]
	
	print 'Slicing audio and creating .wav files'
	sliceAudio(iaudiofile, names, times, verbose_en)	
	
	if au_format != '':
		print 'Converting .wav to', '.'+au_format, 'format'
		convert2fmt(names, au_format, keep_wav_en, verbose_en)
	

#print 'getting the name list and times'
#names, times = getNamesAndTimes('list.txt')
#print 'slicing audio and crating wav files'
#sliceAudio(iFilename, names, times)
#print 'converting to mp3 and removing wav'
#convert2fmt(names, 'mp3')
