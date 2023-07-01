import subprocess

def copy_files_to_bitbucket(local_files, bitbucket_repo):
    # Change directory to the local repository
    subprocess.run(['cd', 'C://Users//PRERNPAN//Music//New folder'], check=True)

    # Initialize a Git repository if it doesn't exist
    subprocess.run(['git', 'init'], check=True)

    # Add the files to the repository
    subprocess.run(['git', 'add'] + local_files, check=True)

    # Commit the changes
    subprocess.run(['git', 'commit', '-m', 'Initial commit'], check=True)

    # Set Git username
    subprocess.run(['git', 'config', '--global', 'user.name', 'PRERNA PANDEY'], check=True)

    # Set Git email
    subprocess.run(['git', 'config', '--global', 'user.email', 'pandeyprerna1998@gmail.com'], check=True)

    # Add the Bitbucket repository as a remote
    subprocess.run(['git', 'remote', 'add', 'bitbucket', bitbucket_repo], check=True)

    # Push the files to the Bitbucket repository
    subprocess.run(['git', 'push', '-u', 'bitbucket', 'master'], check=True)

# Usage example
local_files = ['abc.txt', 'def.txt']
bitbucket_repo = 'https://github.com/prernapandey1398/Migration-tool.git'
copy_files_to_bitbucket(local_files, bitbucket_repo)
