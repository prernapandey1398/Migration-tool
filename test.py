import shutil
import subprocess

# Copy the file
source_file = 'Users\\PRERNPAN\\Music\\New folder\\abc.txt'

# Initialize a Git repository (if not already initialized)
subprocess.run(['git', 'init'])

# Add the file to the staging area
shutil.copy(source_file, '.')

# Add the file to the staging area
subprocess.run(['git', 'add', '-A'])

# Commit the changes
subprocess.run(['git', 'commit', '-m', 'Upload file'])

# Set the remote repository URL
remote_url = 'https://github.com/prernapandey1398/Migration-tool.git'
subprocess.run(['git', 'remote', 'add', 'origin', remote_url])

# Push the changes to GitHub
subprocess.run(['git', 'push', '-u', 'origin', 'main'])


