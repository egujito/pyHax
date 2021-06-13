if you don't want the python console to show up in the executable
pass the argument "--noconsole" to pyinstaller
the binary file will also be huge because of the dependencies

This would be:

pyinstaller <other content in builder.bat> --noconsole

After running the script go to "dist" folder
There you can find the standalone executable.

If you see more files than one in this folder it means
you didnt pass "--onefile" to pyinstaller
