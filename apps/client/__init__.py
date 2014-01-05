# This is a cheeky hack.  By making this a Python module, and providing
# a static/ directory, Django will pick up the compiled artifacts within
# and serve them as static files (or: will collect them using 
# collectstatic).  When I figure out a better way of accomplishing this,
# I won't need this file.