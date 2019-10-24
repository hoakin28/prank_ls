# prank_ls
Simple prank replacement for ls command 

Installer.sh - renames ls to zap and copies the rogue ls to the path.

ls.py - It's not a rewrite of the ls command, it's just a wrapper that still needs the command to properly function, so the installer.sh renames the command and the script uses that new name to invoke ls. 

When executed as root, it creates a list with all running process and kills 2 of them on each execution with the exception of systemd and it's own process.
When executed as a normal user, there's no action. 

NOTE: Never to be executed on production servers
