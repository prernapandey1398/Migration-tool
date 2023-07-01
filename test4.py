import subprocess

def upload_folder_to_github(folder_path, repo_url, username, email):
    # Change directory to the folder path
    subprocess.run(['cd', folder_path], shell=True)

    # Initialize a new Git repository
    subprocess.run(['git', 'init'], shell=True)

    # Set the repository configuration
    subprocess.run(['git', 'config', 'user.name', username], shell=True)
    subprocess.run(['git', 'config', 'user.email', email], shell=True)

    # Add all files in the folder to the repository
    subprocess.run(['git', 'add', '.'], shell=True)

    # Commit the changes
    subprocess.run(['git', 'commit', '-m', 'Upload folder'], shell=True)

    # Add the remote repository
    subprocess.run(['git', 'remote', 'add', 'origin', repo_url], shell=True)

    # Push the changes to the remote repository
    subprocess.run(['git', 'push', '-u', 'origin', 'master'], shell=True)

    print('Folder uploaded to GitHub successfully.')

# Usage example
folder_path = r'C:\Users\PRERNPAN\Music\New folder\abc.txt'
repo_url = 'https://github.com/prernapandey1398/Migration-tool.git'
username = 'prernapandey1398'
email = 'pandeyprerna1998@gmail.com'

upload_folder_to_github(folder_path, repo_url, username, email)
