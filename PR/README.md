Errors
====

/cvmfs/cms-ib.cern.ch/nweek-02598/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj/bin/../lib/gcc/x86_64-unknown-linux-gnu/8.3.1/../../../../x86_64-unknown-linux-gnu/bin/ld: tmp/slc7_amd64_gcc820/src/CalibCalorimetry/EcalLaserCorrection/src/CalibCalorimetryEcalLaserCorrection/EcalLaserDbRecordMC.cc.o: in function `std::set<edm::eventsetup::EventSetupRecordKey, std::less<edm::eventsetup::EventSetupRecordKey>, std::allocator<edm::eventsetup::EventSetupRecordKey> > edm::eventsetup::findDependentRecordsFor<EcalLaserDbRecordMC>()':
EcalLaserDbRecordMC.cc:(.text._ZN3edm10eventsetup23findDependentRecordsForI19EcalLaserDbRecordMCEESt3setINS0_19EventSetupRecordKeyESt4lessIS4_ESaIS4_EEv[_ZN3edm10eventsetup23findDependentRecordsForI19EcalLaserDbRecordMCEESt3setINS0_19EventSetupRecordKeyESt4lessIS4_ESaIS4_EEv]+0x8b): undefined reference to `char const* edm::typelookup::className<EcalLaserAPDPNRatiosMCRcd>()'
/cvmfs/cms-ib.cern.ch/nweek-02598/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj/bin/../lib/gcc/x86_64-unknown-linux-gnu/8.3.1/../../../../x86_64-unknown-linux-gnu/bin/ld: EcalLaserDbRecordMC.cc:(.text._ZN3edm10eventsetup23findDependentRecordsForI19EcalLaserDbRecordMCEESt3setINS0_19EventSetupRecordKeyESt4lessIS4_ESaIS4_EEv[_ZN3edm10eventsetup23findDependentRecordsForI19EcalLaserDbRecordMCEESt3setINS0_19EventSetupRecordKeyESt4lessIS4_ESaIS4_EEv]+0x94): undefined reference to `std::type_info const& edm::typelookup::classTypeInfo<EcalLaserAPDPNRatiosMCRcd>()'
collect2: error: ld returned 1 exit status
gmake: *** [config/SCRAM/GMake/Makefile.rules:1732: tmp/slc7_amd64_gcc820/src/CalibCalorimetry/EcalLaserCorrection/src/CalibCalorimetryEcalLaserCorrection/libCalibCalorimetryEcalLaserCorrection.so] Error 1
gmake: *** Waiting for unfinished jobs....
