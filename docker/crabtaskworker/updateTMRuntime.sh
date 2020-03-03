# Run the script from your github CRABServer directory
# this is a hardcoded name in htcondor_make_runtime.sh with no relation
# with actual CRAB version
CRAB3_DUMMY_VERSION=3.3.0-pre1
# this must match the TW release to update
TW_ARCH=slc7_amd64_gcc630
TW_RELEASE=$TW_VERSION
MYTESTAREA=/data/srv/TaskManager/$TW_RELEASE
CRABTASKWORKER_ROOT=${MYTESTAREA}/${TW_ARCH}/cms/crabtaskworker/${TW_RELEASE}
# CRAB_OVERRIDE_SOURCE tells htcondor_make_runtime.sh where to find the CRABServer repository
export CRAB_OVERRIDE_SOURCE=/data/user

pushd $CRAB_OVERRIDE_SOURCE/CRABServer
sh bin/htcondor_make_runtime.sh
mv TaskManagerRun-$CRAB3_DUMMY_VERSION.tar.gz TaskManagerRun.tar.gz
mv CMSRunAnalysis-$CRAB3_DUMMY_VERSION.tar.gz CMSRunAnalysis.tar.gz
cmd=cp
targethost=
$cmd -v CMSRunAnalysis.tar.gz CRAB3-externals.zip TaskManagerRun.tar.gz $CRAB_OVERRIDE_SOURCE/CRABServer/scripts/AdjustSites.py $CRAB_OVERRIDE_SOURCE/CRABServer/scripts/dag_bootstrap_startup.sh $CRAB_OVERRIDE_SOURCE/CRABServer/scripts/dag_bootstrap.sh $CRAB_OVERRIDE_SOURCE/CRABServer/scripts/gWMS-CMSRunAnalysis.sh $CRAB_OVERRIDE_SOURCE/CRABServer/scripts/CMSRunAnalysis.sh $CRAB_OVERRIDE_SOURCE/CRABServer/scripts/cmscp.py $CRAB_OVERRIDE_SOURCE/CRABServer/scripts/DashboardFailure.sh $targethost$CRABTASKWORKER_ROOT/data

popd
