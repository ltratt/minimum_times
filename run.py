#! /usr/bin/env python3.7

import os, sys, time

if len(sys.argv) != 4:
    sys.stderr.write("run.py <version of program> <#iterations> <output file>\n")
    sys.exit(1)

if os.path.exists(sys.argv[3]):
    sys.stderr.write("Error: '%s' already exists.\n" % sys.argv[3])
    sys.exit(1)

os.system("cd %s && cargo build --release" % sys.argv[1])
with open(sys.argv[3], "w") as f:
    for _ in range(int(sys.argv[2])):
        before = time.time()
        if os.system("%s/target/release/%s" % (sys.argv[1], sys.argv[1])) != 0:
            sys.stderr.write("Error: Couldn't run 'count_%s'.\n" % sys.argv[1])
            sys.exit(1)
        after = time.time()
        f.write(str(after - before) + "\n")
        f.flush()
