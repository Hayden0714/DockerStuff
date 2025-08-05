# Important Notes regarding the container process

# Build process simplified
1. Write the Dockerfile
2. To run the Dockerfile and add the image to your 'docker image ls' repository run something like
	a. docker build -t test/tcpserver .
	b. the only flag that the build command needs is a directory with a Dockerfile inside of it
	b. -t is what you are taggint the image as (the name of the image)

3. To run a container that you have put in to your docker image list
	a. docker run -d container/name:version
	b. -d runs the container in the detached mode, which I think is in the background

4. To see what is actually going on inside of the container, you can add /bin/bash to your run command to get a CLI within the container
	a. I think you may need to install this beforehand within the Dockerfile
