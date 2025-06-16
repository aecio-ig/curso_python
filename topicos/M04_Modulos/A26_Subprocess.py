import subprocess

cmd = ['ping', '127.0.0.1']

proc = subprocess.run(cmd, capture_output=True, text=True, encoding='cp850', shell=True)

# print(proc)
# print(proc.args)
# print(proc.stderr)
print(proc.stdout)
