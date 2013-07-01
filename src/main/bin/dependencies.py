#!/usr/bin/env python

import sys
import subprocess
import os
import os.path
import unittest

    
def dependency_list(pom_path='pom.xml', mvn_opts=""):
    output_path = "maven.classpath.txt"
    subprocess.check_call(["mvn", "-f", pom_path, mvn_opts, "dependency:build-classpath", "-Dmdep.outputFile={0}".format(output_path)])
    
    with open(os.path.join("../../", output_path)) as f:
        classpath = f.read()
    
    return classpath.split(os.pathsep)
    

JAR_PREFIXES = ["ovation-", "cloud-file-cache", "joda-time"]
def jar_list(dependencies=[]):

    for f in dependencies:
        jar = os.path.basename(f)
        for prefix in JAR_PREFIXES:
            if jar.startswith(prefix):
                yield f

    
def include_list(dependencies=[]):
    jars = set(jar_list(dependencies))
    print(jars)
    for f in dependencies:
        if f not in jars:
            yield f



class TestDependencyLists(unittest.TestCase):

    dep_list = ["foo.jar", "bar/baz/cloud-file-cache.jar", "bar/baz/ovation-core.jar", "bar/baz/ovation-query.jar"]
            
    def test_jar_list_includes_ovation(self):
        self.assertIn("bar/baz/ovation-core.jar", list(jar_list(self.dep_list)))
        self.assertIn("bar/baz/ovation-query.jar", list(jar_list(self.dep_list)))
        
    def test_jar_list_includes_cloud_file_cache(self):
        self.assertIn("bar/baz/cloud-file-cache.jar", list(jar_list(self.dep_list)))
        
    def test_jar_list_excludes_others(self):
        self.assertNotIn("foo.jar", list(jar_list(self.dep_list)))
        
    def test_include_list_excludes_ovation(self):
        self.assertNotIn("bar/baz/ovation-core.jar", list(include_list(self.dep_list)))
        self.assertNotIn("bar/baz/ovation-query.jar", list(include_list(self.dep_list)))
        
    def test_include_list_excludes_cloud_file_cache(self):
        self.assertNotIn("bar/baz/cloud-file-cache.jar", list(include_list(self.dep_list)))
        
    def test_inclue_list_includes_others(self):
        self.assertIn("foo.jar", list(include_list(self.dep_list)))

    
    
if __name__ == '__main__':
    unittest.main()