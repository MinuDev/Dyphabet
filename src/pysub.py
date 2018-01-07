import sys
import os
from pathlib import Path

# This class represents the whole subtitle file
class SubFile:
    def __init__(self, filename=None):
        if filename == None:
            if __name__ == "__main__":
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
            self.items = subs
        elif (extension == ".vtt"):
            import pyvtt
            subs = pyvtt.open(filename)
            self.items = subs
        elif (extension == ".lrc"):
            import pylrc
            subs = pylrc.open(filename)
            self.items = subs
        else:
            if (__name__ == "__main__"):
                print("The format %s is not supported yet." % extension)
            else:
                raise ValueError("The format %s is not supported" % extension)

# This if checks if the file is being used as a script or as a module
if __name__ == "__main__":
    print("Welcome to pysub!\n")
    if len(sys.argv) == 2:
        file = SubFile(sys.argv[1])
        # We display this information to check if the file has been parsed succesfully
        text = file.items[0].text
        print("The first section's text is \"%s\"" % text)
        try:
            start = file.items[0].start
            print("Its start is %s" % start)
        except AttributeError:
            pass
        try:
            end = file.items[0].end
            print("Its end is %s" % end)
        except AttributeError:
            pass
        try:
            timestamp = file.items[0].timestamp
            print("Its timestamp is %s" % timestamp)
        except AttributeError:
            pass
    else:
        print("Using this script as an standalone tool is only for testing if it works correctly with your subtitle file.\nUsage: pysub.py filename")
        sys.exit(1)
