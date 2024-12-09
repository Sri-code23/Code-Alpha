import subprocess
import os

class GitAutomation:
    def __init__(self):
        #self.repo_path = repo_path
        pass

    def cd(self):
        subprocess.run(['py','--version'], shell=True)

    def popen_method(self):
        subprocess.run(['git','--version'])

    def create_repository(self, repo_name):
        subprocess.run(['git', 'init', repo_name], cwd=os.path.dirname(self.repo_path))

    def add_all(self):
        subprocess.run(['git', 'add', '.'], cwd=self.repo_path)
    
    def commit(self, message):
        subprocess.run(['git', 'commit', '-m', message], cwd=self.repo_path)

    def push(self, remote='origin', branch='main'):
        subprocess.run(['git', 'push', remote, branch], cwd=self.repo_path)

    def pull(self, remote='origin', branch='main'):
        subprocess.run(['git', 'pull', remote, branch], cwd=self.repo_path)

    def create_branch(self, branch_name):
        subprocess.run(['git', 'branch', branch_name], cwd=self.repo_path)

    def checkout_branch(self, branch_name):
        subprocess.run(['git', 'checkout', branch_name], cwd=self.repo_path)

    def merge_branch(self, branch_name):
        subprocess.run(['git', 'merge', branch_name], cwd=self.repo_path)

    def delete_branch(self, branch_name):
        subprocess.run(['git', 'branch', '-d', branch_name], cwd=self.repo_path)

def main():
    repo_path = '/path/to/your/repo'
    git_automation = GitAutomation(repo_path)

    while True:
        print("0. Create Repository")
        print("1. Add all files")
        print("2. Commit changes")
        print("3. Push changes")
        print("4. Pull changes")
        print("5. Create branch")
        print("6. Checkout branch")
        print("7. Merge branch")
        print("8. Delete branch")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            git_automation.add_all()
        elif choice == '0':
            repo_name=input("enter the repo name: ")
            git_automation.create_repository(repo_name)
        elif choice == '2':
            message = input("Enter commit message: ")
            git_automation.commit(message)
        elif choice == '3':
            git_automation.push()
        elif choice == '4':
            git_automation.pull()
        elif choice == '5':
            branch_name = input("Enter branch name: ")
            git_automation.create_branch(branch_name)
        elif choice == '6':
            branch_name = input("Enter branch name: ")
            git_automation.checkout_branch(branch_name)
        elif choice == '7':
            branch_name = input("Enter branch name: ")
            git_automation.merge_branch(branch_name)
        elif choice == '8':
            branch_name = input("Enter branch name: ")
            git_automation.delete_branch(branch_name)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    cdo=GitAutomation()
    cdo.cd()
    cdo.popen_method()
    