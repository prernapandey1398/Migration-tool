import shutil
import subprocess

# Copy the file
source_file = 'C:/Users/PRERNPAN/Music/New folder/abc.txt'
destination_dir = 'C:/Users/PRERNPAN/Music/sam'
shutil.copy(source_file, destination_dir)

# Change directory to the destination directory
subprocess.run(['cd', destination_dir], shell=True)

# Initialize a Git repository (if not already initialized)
subprocess.run(['git', 'init'], check=True)

# Add the file to the staging area
subprocess.run(['git', 'add', '-A'], check=True)

# Commit the changes
subprocess.run(['git', 'commit', '-m', 'Upload file'], check=True)

# Set the remote repository URL
remote_url = 'https://github.com/prernapandey1398/Migration-tool.git'
subprocess.run(['git', 'remote', 'add', 'origin', remote_url], check=True)

# Push the changes to GitHub
subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)
