import os
import re
import SCons

def myEmitter(target, source, env):
    print("running emitter")
    source.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/pythonCp.py')
    return (target, source)

def myScannerFunction(node, env, path):
    implicitDependencies = []

    print("running scanner for %s" % node)
    nodeFile = open("%s" % node)
    for line in nodeFile.readlines():
        mo = re.match("^\s*:dependson:\s*(?P<file>\S+)", line)
        if mo:
            implicitDependencies.append(mo.group('file'))
            print("implicit dependencies found: %s" % implicitDependencies)
    return implicitDependencies

def generate(env):
    kScanner = SCons.Scanner.Scanner(function = myScannerFunction,
                                     recursive = 1,
                                     skeys = ['.k'])
    print("adding KBuilder to environment")
    env['BUILDERS']['KBuilder'] = SCons.Builder.Builder(action = "/usr/bin/python3.9 ${SOURCES[0]} ${SOURCES[1]} $TARGET",
                                                        emitter = myEmitter,
                                                        source_scanner = kScanner,
                                                        )

def exists(env):
    return True
