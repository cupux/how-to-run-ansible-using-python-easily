from subprocess import call


call(["ansible-playbook", "-i", "/home/your_path/hosts", "--extra-vars=sub_domain=share.more.com" ,
 "/home/your_path/sshscript.yml" ])



# When this is finishes running your ssl will be installed successfully