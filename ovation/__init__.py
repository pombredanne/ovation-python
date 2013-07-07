import os
import glob

jars_directory = os.path.join(os.path.dirname(__file__), 'jars')
CLASSPATH = []
for jar_path in glob.iglob(os.path.join(jars_directory, "*.jar")):
    CLASSPATH.append(jar_path)

os.environ["CLASSPATH"] = os.path.pathsep.join(CLASSPATH)

from jnius import autoclass


# Common references outside the us.physion.ovation namespace
Sets = autoclass("com.google.common.collect.Sets")
Maps = autoclass("com.google.common.collect.Maps")

Map = autoclass("java.util.Map")

URL = autoclass("java.net.URL")
URI = autoclass("java.net.URI")

File = autoclass("java.io.File")

DateTime = autoclass("org.joda.time.DateTime")
DateTimeZone = autoclass("org.joda.time.DateTimeZone")

TimeUnit = autoclass("java.util.concurrent.TimeUnit")
