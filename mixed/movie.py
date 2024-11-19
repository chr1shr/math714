#!/usr/bin/python3
import os
import sys

# Total jobs
tot=257

# Available slots
P=8
pid=[None]*(P+1)

# Set thread number and queue status
t=1
queue=P==1

# Loop over the jobs
for i in range(0,tot):
    print("Job %d to slot %d"%(i,t))

    # Fork a child process to run a simulation
    j=os.fork()
    if j==0:
        os.system("../../utils-gp/bitmap_field -u 6 spinodal.odr/u.%d spinodal.odr/fr_%04d.png -1 1 >/dev/null" %(i,i))
        os._exit(0)
    pid[t]=j

    # If we've reached the maximum number of slots, then wait for one job to
    # finish
    if queue:

        # Find which slot is now available
        npid=os.wait()[0]
        t=1
        while pid[t]!=npid:
            t+=1
            if t>P:
                print("PID return error")
                sys.exit()

    # Otherwise, move onto the next slot
    else:
        t+=1
        queue=t>=P

# Wait for all remaining jobs to finish
if queue:
    for i in range(P-1):
        os.wait()
else:
    for i in range(t-1):
        os.wait()

# Create movie using FFmpeg in the H.265/HEVC format
os.system("ffmpeg -r 30 -y -i spinodal.odr/fr_%4d.png -preset veryslow -c:v libx265 -crf 17 -pix_fmt yuv420p -tag:v hvc1 -movflags faststart spinodal.mov")
