#### Pre steps (for private installations):
- Customize the `TaskWorkerConfig.py` in order to prepare the image with the correct configuration:
  - Set Task Worker name:                                     `config.TaskWorker.name`
  - Enter Grid host certificate DN:                           `config.MyProxy.serverdn`
  - If needed, modify host name for the fronted :             `config.TaskWorker.resturl`
- Edit `install_TW.sh` to set which repo will be used for the build: `export REPO`


#### Set TW version
`TW_VERSION=3.3.2003.rc4`

#### Build image 
`docker build . -t mytaskworker:$TW_VERSION --build-arg TW_VERSION=$TW_VERSION`

#### Run given image 
`docker run --name CRABTWv1 -d -ti --privileged --net host -v /etc/grid-security/:/etc/grid-security/  -v /data/certs/:/data/certs/  -v /etc/vomses:/etc/vomses  mytaskworker:$TW_VERSION`

#### Enter in a container
`docker exec -it CRABTWv1 /bin/bash`
