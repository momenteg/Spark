# Spark

## How to use Spark as jupyter's notebook kernel

Pre-requisites: 
* [get docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04) 
* pull the docker image: jupyter/pyspark-notebook: _sudo -s && docker pull jupyter/pyspark-notebook_

* launch the docker notebook: 
``` bash
docker run -it -p 8888:8888 -v `pwd`:/home/jovyan/work --rm --name jupyter jupyter/pyspark-notebook```

* open the browser and copy paste the address printed on the terminal (ex: http://localhost:8888/?token=...)