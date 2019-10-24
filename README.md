# prank_ls
Simple prank replacement for ls command 

When executed as root, it creates a list with all running process and kills 2 of them on each execution with the exception of systemd and it's own process.
When executed as a normal user, there's no action. 

NOTE: Never to be executed on production servers
