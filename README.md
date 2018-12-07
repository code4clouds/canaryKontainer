# Purpose

Provide a sample code that prints the git tag version on a web server.  The idea is to build the containers using Dockerhub automated builds to create the images which then will be used in canary deployment tests.

You can find the prebuild docker containers here:
https://hub.docker.com/r/code4clouds/canarykontainer/

# Usage

Download and execute the container using the following command:

``` bash
docker run -p 5000:5000 code4clouds/canarykontainer:1.1
```

Point your favorite browser to: http://localhost:5000 that should display the same version as the container tag.

