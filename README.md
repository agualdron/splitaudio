# splitaudio
A python program to split an audio file in tracks from a list of names and times.

# Dependencies
The program uses the soundfile library to split the audio data.
The program uses avconv in command line to convert the audio files to different formats such as mp3, ogg and aiff.

print "----------------------------------------------SPLIT AUDIO-----------------------------------------------"

splitaudio is a python program to split audio into tracks"
from a list of names and times."

#Usage
         splitaudio --input <input_file.wav> --list <list_of_names.txt>  <...>
         
##Arguments
.......Options.......   .....Arguments.....   .............Description..................................
  Long          Short"
--input        -i       <input_file.wav>      : input file, should be a wav file.
--list         -l       <list_of_names>       : a text file with the list of names and times.
--format       -f       <mp3 | aiff | ogg>    : the output audio format. default is wav
--keep-wav     -k                             : keep the sliced .wav files if other format is configured
--help         -h                             : display help
--verbose      -v                             : print messages
 
Format of the lines in list: 
   <track number>. <Name> <minutes:seconds>
   <##>. <Name> <mm:ss>
   Example:
    3. Hello (Buddy) 8:07
