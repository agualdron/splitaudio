# splitaudio
SplitAudio is a python program to split an audio file (.wav files initially) in tracks from a list of names and times.

The common scenario is when you have for example an audio of a live event and want to split the audio into smaller parts, for instance songs...

# Dependencies
First of all it needs python, It was programmed in 2.7.11.
SplitAudio uses the python **soundfile** library to split the audio data and the program **avconv** to convert the audio files to different formats such as mp3, ogg and aiff.

#How to use?
SplitAudio is a command line oriented programm, to use it just execute the command giving the audio file and a text file which contains the list of names and times.

         splitaudio --input <input_file.wav> --list <list_of_names.txt>  <...>
         
## More options 
SplitAudio have the following Arguments:

- --input        (-i)       <input_file.wav>      : input file, should be a wav file.
- --list         (-l)       <list_of_names>       : a text file with the list of names and times.
- --format       (-f)       <mp3 | aiff | ogg>    : the output audio format. default is wav
- --keep-wav     (-k)                             : keep the sliced .wav files if other format is configured
- --help         (-h)                             : display help
- --verbose      (-v)                             : print messages


## The Format for the list
The list sould have a very simple format:

         <track number>. <Name> <minutes:seconds>

         < ## >. < Name > < mm:ss >

Example:

    3. Hello (Buddy) 8:07
    
    
#How to Install?

## Make sure you have python

## Installing dependencies

## Make it executable form everywhere

## Enjoy !!
