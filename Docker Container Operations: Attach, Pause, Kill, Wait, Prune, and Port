Docker Container Management Notes
1. docker attach
Purpose

Connects your terminal to the main process of a running container.

Syntax
docker attach <container-name>

Example:

docker attach html-container

To detach without stopping the container:

Ctrl + P, then Ctrl + Q
Interview Question

Q: What is the difference between docker attach and docker exec?

Answer:

docker attach connects to the main process of the container.
docker exec starts a new process (like /bin/bash) inside the running container.
docker exec is preferred for administration and troubleshooting.
2. docker kill
Purpose

Immediately stops a running container by sending a signal (default: SIGKILL).

Syntax
docker kill <container-name>

Example:

docker kill html-container

Stop multiple containers:

docker kill container1 container2
Difference Between docker stop and docker kill
docker stop	docker kill
Gracefully stops the container (SIGTERM, then SIGKILL if needed).	Immediately terminates the container (SIGKILL).
Gives the application time to shut down cleanly.	Forces the container to exit immediately.
Interview Question

Q: When would you use docker kill?

Answer:
When a container becomes unresponsive and cannot be stopped gracefully using docker stop.

3. docker wait
Purpose

Waits until one or more containers stop running and then prints their exit code.

Syntax
docker wait <container-name>

Example:

docker wait html-container

Example output:

0

Exit code meanings:

Exit Code	Meaning
0	Successful execution
1	General error
125	Docker command failed
126	Command cannot execute
127	Command not found
Interview Question

Q: What is the purpose of docker wait?

Answer:
It blocks until the specified container exits and then returns its exit status. It's useful in scripts and automation.

4. docker pause
Purpose

Temporarily suspends all processes inside a running container.

Syntax
docker pause <container-name>

Example:

docker pause html-container

Verify:

docker ps

Status:

Up (Paused)
Interview Question

Q: What happens when a container is paused?

Answer:
All processes are frozen. The container remains in memory but does not execute any work until it is unpaused.

5. docker unpause
Purpose

Resumes a paused container.

Syntax
docker unpause <container-name>

Example:

docker unpause html-container
Interview Question

Q: What is the difference between stopping and pausing a container?

Stop	Pause
Container is terminated.	Processes are suspended.
Must be started again.	Can be resumed instantly.
Memory is released.	Memory is retained.
6. docker container prune
Purpose

Removes all stopped containers.

Syntax
docker container prune

Example:

docker container prune

Docker asks for confirmation:

WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N]

Skip confirmation:

docker container prune -f
Interview Question

Q: What does docker container prune remove?

Answer:
It removes only stopped containers. Running containers are not affected.

7. docker port
Purpose

Displays the port mappings of a running container.

Syntax
docker port <container-name>

Example:

docker port html-container

Output:

80/tcp -> 0.0.0.0:8080

Meaning:

Container Port: 80
Host Port: 8080
Example

Run a container:

docker run -d -p 8080:80 --name html-container html-demo

Check mapping:

docker port html-container

Output:

80/tcp -> 0.0.0.0:8080
Interview Question

Q: How do you check which host port is mapped to a container?

Answer:

docker port <container-name>
Quick Command Summary
Command	Purpose
docker attach <container>	Attach to the main process of a running container.
docker kill <container>	Forcefully stop a running container immediately.
docker wait <container>	Wait for a container to stop and return its exit code.
docker pause <container>	Suspend all processes in a running container.
docker unpause <container>	Resume a paused container.
docker container prune	Remove all stopped containers.
docker port <container>	Display the host-to-container port mappings.
Most Common Interview Question

Q: What is the difference between docker stop, docker kill, and docker pause?

Answer:

docker stop: Gracefully stops the container by sending SIGTERM, then SIGKILL if it doesn't exit within the timeout.
docker kill: Immediately terminates the container by sending SIGKILL (or another specified signal).
docker pause: Freezes all processes inside the container without stopping it. The container can later be resumed with docker unpause.
