import subprocess as sp


sp.run(['pycodestyle', '.'])
sp.run(['chmod', '+x', 'runtests.sh'])
sp.run(['./runtests.sh'])
