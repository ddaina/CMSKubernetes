from multiprocessing import cpu_count
from WMCore.Configuration import ConfigurationEx
import HTCondorLocator
import logging


config = ConfigurationEx()

## External services url's
config.section_("Services")
config.Services.PhEDExurl = 'https://phedex.cern.ch'
config.Services.DBSUrl = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader'
config.Services.MyProxy= 'myproxy.cern.ch'

config.section_("TaskWorker")
config.TaskWorker.polling = 30 #seconds
#config.TaskWorker.polling = 60 #MM - increased to 60 after TW has been off one day
# we can add one worker per core, plus some spare ones since most of actions wait for I/O

config.TaskWorker.nslaves = 2


config.TaskWorker.name = 'CRAB-TW' #Remember to update this!

config.TaskWorker.recurringActions =['RemovetmpDir']
# config.TaskWorker.recurringActions = ['RenewRemoteProxies', 'RemovetmpDir', 'BanDestinationSites']


config.TaskWorker.scratchDir = '/data/srv/tmp' #make sure this directory exists
config.TaskWorker.logsDir = './logs'

## SB START - simple config for testing
#config.TaskWorker.nslaves = 1
#config.TaskWorker.recurringActions = []
## SB END

# Setting the list of users for the highprio accounting group.
# config.TaskWorker.highPrioUsers = ['sethzenz']


## Possible values for mode are:
#   - cmsweb-dev
#   - cmsweb-preprod
#   - cmsweb-prod
#   - private
config.TaskWorker.mode = 'test'
config.TaskWorker.restURInoAPI = '/crabserver/preprod/'

## If 'private' mode then a server url is needed
config.TaskWorker.resturl = 'cmsweb-testbed.cern.ch'

## the parameters here below are used to contact cmsweb services for the REST-DB interactions
config.TaskWorker.cmscert = '/data/certs/servicecert.pem'
config.TaskWorker.cmskey = '/data/certs/servicekey.pem'

config.TaskWorker.backend = 'glidein'
#Retry policy
config.TaskWorker.max_retry = 4
config.TaskWorker.retry_interval = [30, 60, 120, 0]


#Default False. If true dagman will not retry the job on ASO failures
config.TaskWorker.retryOnASOFailures = True
#Dafault 0. If -1 no ASO timeout, if transfer is stuck in ASO we'll retry the postjob FOREVER (well, eventually a dagman timeout for the node will be hit).
#If 0 default timeout of 4 to 6 hours will be used. If specified the timeout set will be used (minutes).
config.TaskWorker.ASOTimeout = 86400

# Control the ordering of stageout attempts.
# - remote means a copy from the worker node to the final destination SE directly.
# - local means a copy from the worker node to the worker node site's SE.
# One can include any combination of the above, or leaving one of the methods out.
# For example, CRAB2 is effectively:
# config.TaskWorker.stageoutPolicy = ["remote"]
# This is the CRAB3 default: ["local", "remote"]:
config.TaskWorker.stageoutPolicy = ["local", "remote"]
config.TaskWorker.dashboardTaskType = 'analysis'

# 0 - number of post jobs = max( (# jobs)*.1, 20)
# -1 - no limit
# This is needed for Site Metrics
# It should not block any site for Site Metrics and if needed for other activities
config.TaskWorker.ActivitiesToRunEverywhere = ['hctest', 'hcdev']

config.TaskWorker.maxIdle = 1000
config.TaskWorker.maxPost = 20

# new schedd chooser
#config.TaskWorker.scheddPickerFunction = HTCondorLocator.memoryBasedChoices
#config.TaskWorker.scheddPickerFunction = tunedScheddSubmission
#config.TaskWorker.scheddPickerFunction = totalRandom
#config.TaskWorker.scheddPickerFunction = newScheddPicker
config.TaskWorker.scheddPickerFunction = HTCondorLocator.capacityMetricsChoicesHybrid

config.TaskWorker.DDMServer = 'dynamo.mit.edu'

config.section_("Sites")
#config.Sites.DashboardURL = "https://cmst1.web.cern.ch/CMST1/SST/analysis/usableSites.json"
config.Sites.DashboardURL = "https://cmssst.web.cern.ch/cmssst/analysis/usableSites.json"

# config.Sites.available = []


config.section_("MyProxy")
config.MyProxy.serverhostcert = '/data/certs/hostcert.pem'
config.MyProxy.serverhostkey = '/data/certs/hostkey.pem'
#config.MyProxy.uisource = '/afs/cern.ch/cms/LCG/LCG-2/UI/cms_ui_env.sh'
config.MyProxy.cleanEnvironment = True
config.MyProxy.credpath = '/data/certs/creds' #make sure this directory exists
config.MyProxy.serverdn = '<enter server dn>'

# Setting the minimum runtime requirements in minutes for automatic splitting
config.TaskWorker.minAutomaticRuntimeMins = 60
config.TaskWorker.highPrioEgroups = ['cms-crab-HighPrioUsers']

