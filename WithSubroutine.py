# Developer: Engr. Tufail Mabood
# WhatsApp: +923440907874
# Note: Incase if you are using this script and having problems, ask me on WhatsApp and i will guide youa accordingly.

## It may did not work with latest version of Python 3.x
## Import required libraries
import os
import re
from abaqus import *
from abaqusConstants import *

# Get current working directory
current_dir = os.getcwd()

# Get the only .inp file
# You need to keep main working .inp file
inp_files = sorted([f for f in os.listdir(current_dir) if f.endswith('.inp')])

# You need to keep all the .for files, which you modified for this script before running the jobs
for_files = sorted([f for f in os.listdir(current_dir) if f.endswith('.for')])

# Validation
if not inp_files:
    raise Exception("No .inp files found in current directory.")
if len(inp_files) > 1:
    raise Exception("More than one .inp file found. This script expects only ONE.")
if not for_files:
    raise Exception("No .for files found in current directory.")

# Use the single .inp file
# It will search the first one .inp file, so i will recommend you to keep only 1 file
inp_file = inp_files[0]
inp_path = os.path.join(current_dir, inp_file)
base_inp = os.path.splitext(inp_file)[0]

# Loop over all .for files
for for_file in for_files:
    for_path = os.path.join(current_dir, for_file)
    base_for = os.path.splitext(for_file)[0]

    # Safe job name (If the .inp name is simple, you will not face any problem, i.e, like keeping them without spaces: Let say FCont.inp or FC.inp)
    job_name = base_inp + '_' + base_for
    safe_name = re.sub('[^A-Za-z0-9_]', '_', job_name)
    if not safe_name[0].isalpha():
        safe_name = 'job_' + safe_name

    print "Creating job:", safe_name

    # Create the job
    mdb.JobFromInputFile(name=safe_name,
        inputFileName=inp_path,
        type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None,
        memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE,
        userSubroutine=for_path,
        scratch='', resultsFormat=ODB,
        parallelizationMethodExplicit=DOMAIN, numDomains=1,
        activateLoadBalancing=False, multiprocessingMode=DEFAULT,
        numCpus=1)

    # Submit and wait
    print "Submitting job:", safe_name
    mdb.jobs[safe_name].submit(consistencyChecking=OFF)
    print "Waiting for job to finish:", safe_name
    mdb.jobs[safe_name].waitForCompletion()
    print "Finished job:", safe_name
