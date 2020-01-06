Errors
====

/cvmfs/cms-ib.cern.ch/nweek-02598/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj/bin/../lib/gcc/x86_64-unknown-linux-gnu/8.3.1/../../../../x86_64-unknown-linux-gnu/bin/ld: tmp/slc7_amd64_gcc820/src/CalibCalorimetry/EcalLaserCorrection/src/CalibCalorimetryEcalLaserCorrection/EcalLaserDbRecordMC.cc.o: in function `std::set<edm::eventsetup::EventSetupRecordKey, std::less<edm::eventsetup::EventSetupRecordKey>, std::allocator<edm::eventsetup::EventSetupRecordKey> > edm::eventsetup::findDependentRecordsFor<EcalLaserDbRecordMC>()':
EcalLaserDbRecordMC.cc:(.text._ZN3edm10eventsetup23findDependentRecordsForI19EcalLaserDbRecordMCEESt3setINS0_19EventSetupRecordKeyESt4lessIS4_ESaIS4_EEv[_ZN3edm10eventsetup23findDependentRecordsForI19EcalLaserDbRecordMCEESt3setINS0_19EventSetupRecordKeyESt4lessIS4_ESaIS4_EEv]+0x8b): undefined reference to `char const* edm::typelookup::className<EcalLaserAPDPNRatiosMCRcd>()'
/cvmfs/cms-ib.cern.ch/nweek-02598/slc7_amd64_gcc820/external/gcc/8.2.0-pafccj/bin/../lib/gcc/x86_64-unknown-linux-gnu/8.3.1/../../../../x86_64-unknown-linux-gnu/bin/ld: EcalLaserDbRecordMC.cc:(.text._ZN3edm10eventsetup23findDependentRecordsForI19EcalLaserDbRecordMCEESt3setINS0_19EventSetupRecordKeyESt4lessIS4_ESaIS4_EEv[_ZN3edm10eventsetup23findDependentRecordsForI19EcalLaserDbRecordMCEESt3setINS0_19EventSetupRecordKeyESt4lessIS4_ESaIS4_EEv]+0x94): undefined reference to `std::type_info const& edm::typelookup::classTypeInfo<EcalLaserAPDPNRatiosMCRcd>()'
collect2: error: ld returned 1 exit status
gmake: *** [config/SCRAM/GMake/Makefile.rules:1732: tmp/slc7_amd64_gcc820/src/CalibCalorimetry/EcalLaserCorrection/src/CalibCalorimetryEcalLaserCorrection/libCalibCalorimetryEcalLaserCorrection.so] Error 1
gmake: *** Waiting for unfinished jobs....


This file was not committed:

    CondFormats/DataRecord/src/EcalLaserAPDPNRatiosMCRcd.cc
    

    
Tests
====


Preparing to run 250202.172 TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25

# in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/CMSSW_11_0_0_pre8/src dryRun for 'cd 250202.172_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25
 cmsDriver.py TTbar_13TeV_TuneCUETP8M1_cfi  --conditions auto:phase1_2017_realistic -n 10 --era Run2_2017 --eventcontent FEVTDEBUG --relval 9000,50 -s GEN,SIM --datatier GEN-SIM --beamspot Realistic25ns13TeVEarly2017Collision --io TTbar_13UP17.io --python TTbar_13UP17.py --fileout file:step1.root  --nThreads 8 > step1_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1
 

# in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/CMSSW_11_0_0_pre8/src dryRun for 'cd 250202.172_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25
 cmsDriver.py step2  --datamix PreMix --conditions auto:phase1_2017_realistic --pileup_input das:/RelValPREMIXUP17_PU25/CMSSW_10_6_0-PU25ns_106X_mc2017_realistic_v3-v1/PREMIX --customise_commands "process.EcalLaserCorrectionServiceMC = cms.ESProducer('EcalLaserCorrectionServiceMC') \n process.GlobalTag.toGet = cms.VPSet( cms.PSet(     record = cms.string('EcalLaserAPDPNRatiosMCRcd'),  tag = cms.string('EcalLaserAPDPNRatios_UL_2017_mc'),  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS') ) )" --era Run2_2017 --procModifiers premix_stage2 -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW,HLT:@relval2017 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --eventcontent FEVTDEBUGHLT --io DIGIPRMXUP17_PU25_RD.io --python DIGIPRMXUP17_PU25_RD.py -n 100  --filein  file:step1.root  --fileout file:step2.root  --nThreads 8 > step2_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1
 
 
  cmsDriver.py step2  --datamix PreMix --conditions auto:phase1_2017_realistic --pileup_input das:/RelValPREMIXUP17_PU25/CMSSW_10_6_0-PU25ns_106X_mc2017_realistic_v3-v1/PREMIX --customise_commands "process.EcalLaserCorrectionServiceMC = cms.ESProducer('EcalLaserCorrectionServiceMC') \n process.GlobalTag.toGet = cms.VPSet( cms.PSet(     record = cms.string('EcalLaserAPDPNRatiosMCRcd'),  tag = cms.string('EcalLaserAPDPNRatios_UL_2017_mc'),  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS') ) )" --era Run2_2017 --procModifiers premix_stage2 -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW,HLT:@relval2017 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --eventcontent FEVTDEBUGHLT --io DIGIPRMXUP17_PU25_RD.io --python DIGIPRMXUP17_PU25_RD.py -n 100  --filein  file:step1.root  --fileout file:step2.root  --nThreads 8 > step2_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1

  cmsDriver.py step2  --datamix PreMix --conditions auto:phase1_2017_realistic --pileup_input das:/RelValPREMIXUP17_PU25/CMSSW_10_6_0-PU25ns_106X_mc2017_realistic_v3-v1/PREMIX --customise_commands "process.EcalLaserCorrectionServiceMC = cms.ESProducer('EcalLaserCorrectionServiceMC') \n process.GlobalTag.toGet = cms.VPSet( cms.PSet(     record = cms.string('EcalLaserAPDPNRatiosMCRcd'),  tag = cms.string('EcalLaserAPDPNRatios_UL_2017_mc'),  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS') ) )  \n process.ecal_sim_parameter_map.timeDependent=cms.untracked.bool(True)" --era Run2_2017 --procModifiers premix_stage2 -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW,HLT:@relval2017 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --eventcontent FEVTDEBUGHLT --io DIGIPRMXUP17_PU25_RD.io --python DIGIPRMXUP17_PU25_RD.py -n 100  --filein  file:step1.root  --fileout file:step2.root  --nThreads 8 > step2_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1
 

  cmsDriver.py step2  --datamix PreMix --conditions auto:phase1_2017_realistic --pileup_input das:/RelValPREMIXUP17_PU25/CMSSW_10_6_0-PU25ns_106X_mc2017_realistic_v3-v1/PREMIX --customise_commands "process.EcalLaserCorrectionServiceMC = cms.ESProducer('EcalLaserCorrectionServiceMC') \n process.GlobalTag.toGet = cms.VPSet( cms.PSet(     record = cms.string('EcalLaserAPDPNRatiosMCRcd'),  tag = cms.string('EcalLaserAPDPNRatios_UL_2017_mc'),  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS') ) )  \n process.mixData.workers.ecal.timeDependent=True" --era Run2_2017 --procModifiers premix_stage2 -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW,HLT:@relval2017 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --eventcontent FEVTDEBUGHLT --io DIGIPRMXUP17_PU25_RD.io --python DIGIPRMXUP17_PU25_RD.py -n 100  --filein  file:step1.root  --fileout file:step2.root  --nThreads 8 > step2_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1
 
 
 
 
# in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/CMSSW_11_0_0_pre8/src dryRun for 'cd 250202.172_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25
 cmsDriver.py step3  --conditions auto:phase1_2017_realistic -n 10 --era Run2_2017 --eventcontent RECOSIM,MINIAODSIM,DQM --runUnscheduled  --procModifiers premix_stage2 -s RAW2DIGI,L1Reco,RECO,RECOSIM,EI,PAT,VALIDATION:@standardValidationNoHLT+@miniAODValidation,DQM:@standardDQMFakeHLT+@miniAODDQM --datatier GEN-SIM-RECO,MINIAODSIM,DQMIO --io RECOPRMXUP17_PU25.io --python RECOPRMXUP17_PU25.py --filein  file:step2.root  --fileout file:step3.root  --nThreads 8 > step3_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1
 

# in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/CMSSW_11_0_0_pre8/src dryRun for 'cd 250202.172_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25
 cmsDriver.py step4  --conditions auto:phase1_2017_realistic -s HARVESTING:@standardValidationNoHLT+@standardDQMFakeHLT+@miniAODValidation+@miniAODDQM --filetype DQM --geometry DB:Extended --era Run2_2017 --mc  --io HARVESTUP17_PU25.io --python HARVESTUP17_PU25.py -n 100  --filein file:step3_inDQM.root --fileout file:step4.root  > step4_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1

 
 
Conddb:

    https://cms-conddb.cern.ch/cmsDbBrowser/list/Prod/tags/EcalLaserAPDPNRatios_Run_Dep_MC
 
 
PR numbers
====

    https://github.com/cms-sw/cmssw/pull/28214
    
    
    