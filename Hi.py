import os,time,platform
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    import oldp
elif bit=='32bit':
    import oldp
