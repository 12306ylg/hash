import subprocess as sp
threadnum = 1
with open("matched", "r") as f:
    matched = f.read()

for thread in range(threadnum):
    print("created process:", thread)
    ret = sp.Popen(["python", "hash.py", str(thread)])
    # Wait for the process to finish before continuing
    ret.wait()

while True:
    with open("matched", "r") as f:
        if matched != f.read():
            print("has a matched hash!")
            
            matched=f.read()
            break  # Exit the loop once a match is found
