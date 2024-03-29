import subprocess

class ShellCmdException(Exception):
    """Exception raised when a shell command fails"""

class ShellCmd:
    def __init__(self, command):
        self.command = command

    def __or__(self, other):
        # Combine the commands to emulate piping
        combined_command = f"{self.command} | {other.command}"
        return self.__class__(combined_command)

    def __call__(self):
        # Run the combined command and return the output
        result = subprocess.run(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            raise ShellCmdException(result.stderr.decode('utf-8'))
        return result.stdout.decode('utf-8').strip()

# Usage
ls = ShellCmd("ls")
grep_py = ShellCmd("grep .py$")

# This will emulate `ls | grep .py` in the shell
piped_command = ls | grep_py
print(piped_command())

