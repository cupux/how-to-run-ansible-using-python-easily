from subprocess import call # this gives python acces to the terminal to run the code below


# so lets explain this code step by step
# "ansible-playbook" this calls the ansible playbook to run this code
# "-i". This is mostly used when you have defined your custom hosts. if you have used the defualt hosts given from the ansible doc you do not need this
# "/home/your_path/hosts" this is to show the path to the custom host you have created( which we will do in chapter 2). But with this, since the hosts will be equated to an ip. you can only write hosts 
# --extra-vars=name=define your variable here. This is to define the variable name." 
# /home/your_path/example_one.yml this is the path to your yml file.
# TODO: you can add more variables to the yml file, you can also use format method to define the variables. feel free to use any method

call(["ansible-playbook", "-i", "/home/your_path/hosts", "--extra-vars=name=cupux" ,
 "/home/your_path/example_one.yml" ])


 
sub_domain = "jkm.hostleyghana.com"
call(["ansible-playbook", "-i", "/home/hostley/hostley/hosts", "--extra-vars=sub_domain=jkm.hostleyghana.com" ,
 "/home/hostley/hostley/sshscript.yml" ])