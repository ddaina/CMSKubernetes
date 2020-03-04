#### Set TW version
`TW_VERSION=3.3.2003.rc4`

#### Build image 
`docker build . -t crabTW:$TW_VERSION --build-arg TW_VERSION=${TW_VERSION}`

#### Run given image 
`docker run --name CRABTWv1 -d -ti --privileged --net host -v /etc/grid-security/:/etc/grid-security/  -v /data/certs/:/data/certs/  -v /etc/vomses:/etc/vomses -v /data/user/logs:/data/srv/TaskManager/logs -v /data/srv/TaskWorkerConfig.py:/data/srv/TaskManager/${TW_VERSION}/TaskWorkerConfig.py  crabTW:$TW_VERSION`

#### Enter container
`docker exec -it CRABTWv1 /bin/bash`
