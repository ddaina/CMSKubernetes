#### Set TW version
`TW_VERSION=3.3.2003.rc4`

#### Build image 
`docker build . -t mytaskworker:$TW_VERSION --build-arg TW_VERSION=$TW_VERSION`

#### Run given image 
`docker run --name CRABTWv1 -d -ti --privileged --net host -v /etc/grid-security/:/etc/grid-security/  -v /data/certs/:/data/certs/  -v /etc/vomses:/etc/vomses  mytaskworker:$TW_VERSION`

#### Enter in a container
`docker exec -it CRABTWv1 /bin/bash`
