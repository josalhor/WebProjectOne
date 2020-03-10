# Run locally

First of all be logged on docker, otherwise you won't be able to build 

Ready for a lot of magic?

- "docker-compose up --build"

That command will run docker and django will be available on port 80

# On Docker Toolbox windows

- "docker-machine start default" -> Start Virtual Machine
- "docker-machine env" -> Configure Terminal
- "docker-machine ip default" -> Get IP of machine
- "docker-compose up --build" -> Start Django