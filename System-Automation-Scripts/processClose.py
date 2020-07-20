"""
When using system for general purposes, users do not need some
processes such as mysql, apache etc which are installed during
development and some other backends running unnecessarily in
background. These processes can be stopped for that login.

This script ends these running services only for that login session.

Note:- These processes will run normally when user logins again and
this script only stops the mentioned running services.
"""

# Base library to access system
import os

# List of services user wishes to close on login.
# REMOVE the existing and add your own desired services as strings.
services = ["mysql", "mongod", "docker"]   # Sample

# Execute "$ sudo service ## stop" command
for i in services:
    os.system("sudo service " + i + " stop")

# Print the total services stopped
print(str(len(services)) + " services stopped.")
