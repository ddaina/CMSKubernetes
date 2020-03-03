FROM cmssw/cmsweb:20190814
MAINTAINER Daina Dirmaite daina.dirmaite@gmail.com

ENV WDIR=/data
ENV USER=crab3


# add new user and switch to user
RUN useradd ${USER} && install -o ${USER} -d ${WDIR}
USER ${USER}

ARG TW_VERSION
ENV RELEASE $TW_VERSION
ENV TW_VERSION $TW_VERSION


RUN mkdir -p /data/srv/tmp && mkdir -p /data/srv/TaskManager
WORKDIR ${WDIR}


# install
COPY --chown=${USER}:${USER} install_TW.sh .
RUN echo "Y" > yes.repo
RUN sh install_TW.sh < yes.repo


WORKDIR ${WDIR}/srv/TaskManager/

COPY --chown=${USER}:${USER} env.sh stop.sh start.sh ./  
COPY --chown=${USER}:${USER} TaskWorkerConfig.py ${RELEASE}/TaskWorkerConfig.py 
COPY --chown=${USER}:${USER} condor_config ${WDIR}/srv/condor_config 


# run the service
CMD source ${WDIR}/srv/TaskManager/start.sh && while true; do sleep 60;done
