import sys
import os
from pathlib import Path

# This class represents the whole subtitle file
class File:
    def __init__(self, filename=None):
        # This is a list that will later contain all the sections of the file
        self.sections = []

        if filename == None:
            raise ValueError("The filename argument cannot be None")

        file = Path(filename)
        if not file.is_file():
            if (__name__ == "__main__"):
                print("The filename argument doesn't point to a file")
                sys.exit(1)
            else:
                raise ValueError("The filename argument doesn't point to a file")
        # We get the extension from the filename:
        name, extension = os.path.splitext(filename)

        # We check the extension and use the right module for handling that format
        if (extension == ".srt"):
            import pysrt
            subs = pysrt.open(filename)
            for sub in subs:
                self.sections.append(Section(sub.start, sub.end, None, sub.text))
        elif (extension == ".vtt"):
            import pyvtt
            subs = pyvtt.open(filename)
            for sub in subs:
                self.sections.append(Section(sub.start, sub.end, None, sub.text))
        elif (extension == ".lrc"):
            import pylrc
            subs = pylrc.open(filename)
            for sub in subs:
                self.sections.append(Section(None, None, sub.timestamp, sub.text))
        else:
            if (__name__ == "__main__"):
                print("The format %s is not supported yet." % extension)
            else:
                raise ValueError("The format %s is not supported" % extension)

# This class represents a section in the file. Each section has a timestamp, text and index
class Section:
    def __init__(self, start=None, end=None, timestamp=None, text=None):
        self.start = start
        self.end = end
        self.timestamp = timestamp
        self.text = text

# This if checks if the file is being used as a script or as a module
if __name__ == "__main__":
    print("Welcome to pysub!\n")
    if len(sys.argv) == 2:
        file = File(sys.argv[1])
        # We display this information to check if the file has been parsed succesfully
        text = file.sections[0].text
        start = str(file.sections[0].start)
        end = str(file.sections[0].end)
        timestamp = str(file.sections[0].timestamp)
        print("The first section's text is %s" % text)
        if start != "None":
            print("Its start is %s" % start)
        if end != "None":
            print("Its end is %s" % end)
        if timestamp != "None":
            print("Its timestamp is %s" % timestamp)
    else:
        print("Using this script as an standalone tool is only for testing if it works correctly with your subtitle file.\nUsage: pysub.py filename")
        sys.exit(1)
