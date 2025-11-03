###CTMAKERPYTHN
# Make Container
# View Running Container
# Stop Running Container

# Imports
import re
import subprocess
import time


# Queries
query1 = 'Would you like to run a container? (y/n):'
query2 = 'Would you like to view running containers? (y/n):'
query3 = 'Would you like to stop all running containers? (y/n):'

# Main Logic
query_list = [query1, query2, query3]
for query in query_list:
    user_input = input(query)
    if re.match("^y|^Y", user_input):
        if query == query1:
            subprocess.Popen('podman run -dti ubuntu bash', shell=True)
            time.sleep(1)

        elif query == query2:
            subprocess.Popen('podman ps', shell=True)
            time.sleep(2)
            input("\nPress Enter to continue...")

        elif query == query3:
            print("\n")
            subprocess.Popen('podman kill -a', shell=True)
            time.sleep(1)
            subprocess.Popen('echo All Running Containers Stopped', shell=True)

    elif re.match("^n|^N", user_input):
        print("Nothing Happens.")
        
    else:
        print("Error. Please Try Again.")