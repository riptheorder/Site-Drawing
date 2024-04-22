## The code for the project

### swmapstorhino_Mac.py 
- This python file translates the "trackpoints" .csv from SWMaps into point files for Rhino import. 
- The path parsing makes it so it works on mac, but won't work on windows. 
- For trackpoints files with multiple paths, the first point of the first path will be defined as the origin (0,0,0) and the subsequent paths will be offset relative to that point.