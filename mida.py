import shlex, subprocess

output,error = subprocess.Popen(['mpc', 'current'],stdout = subprocess.PIPE, stderr= subprocess.PIPE).communicate()
#Another way to get output
#output = subprocess.Popen(args,stdout = subprocess.PIPE).stdout
print output
