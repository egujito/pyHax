if you don't want the python console to show up in the executable
pass the argument "--noconsole" to pyinstaller
the binary file will also be huge because of the dependencies
This would be:

pyinstaller <other content in builder.bat> --noconsole
