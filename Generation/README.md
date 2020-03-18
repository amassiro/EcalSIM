Test with generation
====

Needed fix:

    https://github.com/cms-sw/cmssw/pull/27649
    
    git-cms-addpkg  IOPool/Input

    -> and modify file: IOPool/Input/src/RootFile.cc

GENSIM

    cmsRun ZEE_13TeV_TuneCUETP8M1_cfi_GEN_SIM.py

    
    cmsDriver.py ZEE_13TeV_TuneCUETP8M1_cfi  \
         --conditions auto:phase1_2018_realistic -n 100 \
         --era Run2_2018 --relval 200000,100 -s GEN,SIM --datatier GEN-SIM \
         --beamspot Realistic25ns13TeVEarly2018Collision --eventcontent FEVTDEBUG \
         --io ZEE_13UP18_RD.io --python ZEE_13UP18_RD.py\
         --conditions=111X_upgrade2018_realistic_RunDep_v1 --no_exec --fileout file:/tmp/amassiro/gen.root --nThreads 8 \
         --python_filename ZEE_13TeV_TuneCUETP8M1_cfi_RunDepTest_GEN_SIM.py 
    
    
    --customise_commands process.source.numberEventsInLuminosityBlock=cms.untracked.uint32(1000) \n \
         process.GlobalTag.toGet = cms.VPSet( cms.PSet(     record = cms.string('EcalLaserAPDPNRatiosRcd'),  tag = cms.string('EcalLaserAPDPNRatios_Run_Dep_MC'),  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS') ) ) \
         
    cmsRun ZEE_13TeV_TuneCUETP8M1_cfi_RunDepTest_GEN_SIM.py 
    
         
    
    
DIGI2RAW
    
    voms-proxy-init -voms cms -rfc

    cmsDriver.py step2 --conditions auto:phase1_2018_realistic --pileup_input das:/RelValMinBias_13/CMSSW_9_0_0_pre4-90X_mcRun2_asymptotic_v1-v1/GEN-SIM  -n 10 --era Run2_2018 --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,DIGI2RAW --datatier GEN-SIM-DIGI-RAW --pileup AVE_35_BX_25ns --geometry DB:Extended
    
    cmsRun step2_DIGI_L1_DIGI2RAW_PU.py
    
    cmsDriver.py step2 --conditions auto:phase1_2018_realistic --pileup_input das:/RelValMinBias_13/CMSSW_9_0_0_pre4-90X_mcRun2_asymptotic_v1-v1/GEN-SIM  -n 10 --era Run2_2018 --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2018 --datatier GEN-SIM-DIGI-RAW --pileup AVE_35_BX_25ns --geometry DB:Extended
    
    cmsDriver.py step2 --conditions auto:phase1_2018_realistic --pileup_input das:/RelValMinBias_13/CMSSW_10_6_0-106X_upgrade2018_design_v3-v1/GEN-SIM   -n 10 --era Run2_2018 --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2018 --datatier GEN-SIM-DIGI-RAW --pileup AVE_35_BX_25ns --geometry DB:Extended
    step2_SIM.root -> ZEE_13TeV_TuneCUETP8M1_cfi_GEN_SIM.root
    
    step2_SIM.root -> ZEE_13TeV_TuneCUETP8M1_cfi_GEN_SIM.root
    
    mv ZEE_13TeV_TuneCUETP8M1_cfi_GEN_SIM.root step2_SIM.root

    
Premix

    cmsDriver.py step1 --fileout file:ZEE_13TeV_TuneCUETP8M1_cfi_GEN_SIM.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-PUAutumn18_102X_upgrade2018_realistic_v15-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 102X_upgrade2018_realistic_v15 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:@relval2018 --procModifiers premix_stage2 --nThreads 8 --geometry DB:Extended --datamix PreMix --era Run2_2018 --python_filename EXO-RunIIAutumn18DRPremix-00305_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 2626 
    .addMonitoring -n 10 
    

    cmsDriver.py step1 --fileout file:testpremix.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-PUAutumn18_102X_upgrade2018_realistic_v15-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions auto:phase1_2018_realistic --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:@relval2018 --procModifiers premix_stage2 --nThreads 8 --geometry DB:Extended --datamix PreMix --era Run2_2018 --python_filename EXO-RunIIAutumn18DRPremix-00305_1_cfg.py --no_exec -n 10    --filein file:step2_SIM.root
    
    
    cmsDriver.py step1 --fileout file:testpremix.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-PUAutumn18_102X_upgrade2018_realistic_v15-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions auto:phase1_2018_realistic --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --nThreads 8 --geometry DB:Extended --datamix PreMix --era Run2_2018 --python_filename EXO-RunIIAutumn18DRPremix-00305_1_cfg.py --no_exec -n 10    --filein file:step2_SIM.root
    
    
         
    
    
    dasgoclient --query='file dataset=/Neutrino_E-10_gun/RunIISummer19ULPrePremix-UL17_106X_mc2017_realistic_v6-v1/PREMIX'
    
    root://cms-xrd-global.cern.ch:1094//store/mc/RunIISummer19ULPrePremix/Neutrino_E-10_gun/PREMIX/UL17_106X_mc2017_realistic_v6-v1/70025/D58FA235-10D4-8C4C-863A-67D77BA41AA6.root
    xrdcp root://cmsxrootd.fnal.gov//store/mc/RunIISummer19ULPrePremix/Neutrino_E-10_gun/PREMIX/UL17_106X_mc2017_realistic_v6-v1/70025/D58FA235-10D4-8C4C-863A-67D77BA41AA6.root /tmp/amassiro/D58FA235-10D4-8C4C-863A-67D77BA41AA6.root
    
    
    cmsDriver.py step1   --filein file:step2_SIM.root --fileout file:HIG-RunIISummer19UL17DIGIPremix-00001.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer19ULPrePremix-UL17_106X_mc2017_realistic_v6-v1/PREMIX" --mc --eventcontent PREMIXRAW --runUnscheduled --datatier GEN-SIM-DIGI --conditions 106X_mc2017_realistic_v6 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --nThreads 8 --geometry DB:Extended --datamix PreMix --era Run2_2017 --python_filename HIG-RunIISummer19UL17DIGIPremix-00001_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10
    
    
    cmsDriver.py step1   --filein file:step2_SIM.root --fileout file:HIG-RunIISummer19UL17DIGIPremix-00001.root --mc --eventcontent PREMIXRAW --runUnscheduled --datatier GEN-SIM-DIGI --conditions 106X_mc2017_realistic_v6 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --nThreads 8 --geometry DB:Extended --datamix PreMix --era Run2_2017 --python_filename HIG-RunIISummer19UL17DIGIPremix-00001_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

    cmsRun HIG-RunIISummer19UL17DIGIPremix-00001_1_cfg.py
    
    cmsRun RunIISummer19UL17DIGIPremix.py
    
    In the output we have already:  "FEDRawDataCollection                  "rawDataCollector"          ""                "DIGI2RAW"   " --> good!

    
    
    
    ZEE_13TeV_TuneCUETP8M1_cfi_GEN_SIM.root
    
    cmsDriver.py step2   --filein file:/tmp/amassiro/gen.root --fileout file:/tmp/amassiro/ZEE_13TeV_TuneCUETP8M1_cfi_RAW.root  \
           --pileup_input "das:/RelValPREMIXUP18_PU25/CMSSW_11_1_0_pre2-PU25ns_111X_upgrade2018_realistic_RunDep_premix_v1-v1/PREMIX" \
           --mc --eventcontent PREMIXRAW --runUnscheduled --datatier GEN-SIM-DIGI-RAW \
           --conditions 111X_upgrade2018_realistic_RunDep_v1  \
           --step DIGI,DATAMIX,L1,DIGI2RAW --nThreads 8 \
            --procModifiers premix_stage2    --geometry DB:Extended --datamix PreMix --era Run2_2018 \
            -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW  \
             --io DIGIPRMXUP18_PU25_RD.io \
            --python_filename Zee_DIGIPremix_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1000
    
    
    
    step2 --datamix PreMix
    --conditions auto:phase1_2018_realistic --pileup_input das:/RelValPREMIXUP18_PU25/CMSSW_11_1_0_pre2-PU25ns_111X_upgrade2018_realistic_RunDep_premix_v1-v1/PREMIX 
    --customise_commands process.EcalLaserCorrectionServiceMC = cms.ESProducer('EcalLaserCorrectionServiceMC') \n process.GlobalTag.toGet = cms.VPSet( cms.PSet(     record = cms.string('EcalLaserAPDPNRatiosMCRcd'),  tag = cms.string('EcalLaserAPDPNRatios_Run_Dep_MC_first_IOV'),  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS') ), cms.PSet(     record = cms.string('EcalLaserAPDPNRatiosRcd'),  tag = cms.string('EcalLaserAPDPNRatios_Run_Dep_MC'),  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS') ) )  \n process.mixData.workers.ecal.timeDependent=True \n process.source.firstLuminosityBlockForEachRun = cms.untracked.VLuminosityBlockID(*[cms.LuminosityBlockID(x,y) for x,y in ((315257, 1), (316082, 222), (316720, 445), (317527, 668), (320917, 890), (321414, 1112), (321973, 1334), (322492, 1556), (324245, 1779))])
    --era Run2_2018 --procModifiers premix_stage2 -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW,HLT:@relval2018 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --eventcontent FEVTDEBUGHLT --io DIGIPRMXUP18_PU25_RD.io --python DIGIPRMXUP18_PU25_RD.py --conditions=111X_upgrade2018_realistic_RunDep_v1 -n 100 --no_exec --filein file:step1.root --fileout file:step2.root --nThreads 8
    
    cmsRun Zee_DIGIPremix_cfg.py 
    
    https://cmsweb.cern.ch/reqmgr2/fetch?rid=chayanit_RVCMSSW_11_1_0_pre4ZEE_13UP18_RD_PUpmx25ns__200307_151654_9609
    
    
    
    
    
If in need to run HLT specific:
    
    cmsDriver.py step1 --filein file:/tmp/amassiro/HIG-RunIISummer19UL17DIGIPremix-00001.root --fileout file:/tmp/amassiro/HIG-RunIISummer19UL17DIGIPremix-00001.STEP1.root --mc --eventcontent RAWSIM --datatier GEN-SIM-RAW --conditions 106X_mc2017_realistic_v7 --customise_commands 'process.source.bypassVersionCheck = cms.untracked.bool(True)' --step HLT:2e34v40 --nThreads 8 --geometry DB:Extended --era Run2_2017 --python_filename HIG-RunIISummer19UL17HLT-00001_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1858 
    
    cmsDriver.py step1 --filein file:/tmp/amassiro/HIG-RunIISummer19UL17DIGIPremix-00001.root --fileout file:/tmp/amassiro/HIG-RunIISummer19UL17DIGIPremix-00001.STEP1.root --mc --eventcontent RAWSIM --datatier GEN-SIM-RAW --conditions 106X_mc2017_realistic_v7 --customise_commands 'process.source.bypassVersionCheck = cms.untracked.bool(True)' --step HLT --nThreads 8 --geometry DB:Extended --era Run2_2017 --python_filename HIG-RunIISummer19UL17HLT-00001_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1858 
    
    
    cmsRun HIG-RunIISummer19UL17HLT-00001_1_cfg.py
    
    
    
RAW2RECO

    cmsDriver.py step1 --filein file:/tmp/amassiro/HIG-RunIISummer19UL17DIGIPremix-00001.root  --fileout file:/tmp/amassiro/HIG-RunIISummer19UL17RECO-00001.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 106X_mc2017_realistic_v7 --step RAW2DIGI,L1Reco,RECO,RECOSIM --nThreads 8 --geometry DB:Extended --era Run2_2017 --python_filename RAW2RECO.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 3042 

    cmsDriver.py step1 --filein file:/tmp/amassiro/HIG-RunIISummer19UL17DIGIPremix-00001.STEP1.root  --fileout file:/tmp/amassiro/HIG-RunIISummer19UL17RECO-00001.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 106X_mc2017_realistic_v7 --step RAW2DIGI,L1Reco,RECO,RECOSIM --nThreads 8 --geometry DB:Extended --era Run2_2017 --python_filename RAW2RECO.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 3042 
    
    cmsRun RAW2RECO.py

    
    
    
    cmsDriver.py step1 --filein file:/tmp/amassiro/ZEE_13TeV_TuneCUETP8M1_cfi_RAW.root  --fileout file:/tmp/amassiro/ZEE_13TeV_TuneCUETP8M1_cfi_RECO.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 111X_upgrade2018_realistic_RunDep_v1 --step RAW2DIGI,L1Reco,RECO,RECOSIM --nThreads 8 --geometry DB:Extended --era Run2_2018 --python_filename RAW2RECO_Zee.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 100 
    
    cmsRun RAW2RECO_Zee.py
    
    
    
MiniAOD 

    cmsDriver.py step1 --filein file:/tmp/amassiro/HIG-RunIISummer19UL17RECO-00001.root --fileout file:/tmp/amassiro/HIG-RunIISummer19UL17MiniAOD-00001.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 106X_mc2017_realistic_v7 --step PAT --nThreads 8 --geometry DB:Extended --era Run2_2017 --python_filename MINIAOD.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 9600  --customise_commands "del process.patTrigger; del process.selectedPatTrigger; del process.slimmedPatTrigger;   process.MINIAODSIMoutput.outputCommands.append('keep *_particleFlowSuperClusterECAL_*_*');"
    
    
    cmsRun MINIAOD.py
    
    
    
    cmsDriver.py step1 --filein file:/tmp/amassiro/ZEE_13TeV_TuneCUETP8M1_cfi_RECO.root --fileout file:/tmp/amassiro/ZEE_13TeV_TuneCUETP8M1_cfi_MINIAOD.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 111X_upgrade2018_realistic_RunDep_v1 --step PAT --nThreads 8 --geometry DB:Extended --era Run2_2018 --python_filename MINIAOD_Zee.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 9600  --customise_commands "del process.patTrigger; del process.selectedPatTrigger; del process.slimmedPatTrigger;   process.MINIAODSIMoutput.outputCommands.append('keep *_particleFlowSuperClusterECAL_*_*');"
    
    cmsRun MINIAOD_Zee.py
    
    
    
All steps:

    https://cms-pdmv.cern.ch/mcm/chained_requests?prepid=HIG-chain_RunIISummer19UL17wmLHEGEN_flowRunIISummer19UL17SIM_flowRunIISummer19UL17DIGIPremix_flowRunIISummer19UL17HLT_flowRunIISummer19UL17RECO_flowRunIISummer19UL17MiniAOD_flowRunIISummer19UL17NanoAOD-00001&page=0&shown=15
    
Test using the toolkit https://github.com/amassiro/EcalZee: 

    cmsRun dumpMC.py  inputFiles=file:/tmp/amassiro/HIG-RunIISummer19UL17MiniAOD-00001.root     outputFile=test.root

    ln -s ../../EcalZee/test/dumpMC.py

    
    cmsRun dumpMC.py  inputFiles=/store/relval/CMSSW_11_1_0_pre4/RelValZEE_13UP18_RD/MINIAODSIM/PUpmx25ns_111X_upgrade2018_realistic_RunDep_v1-v1/10000/F01022D0-54FC-A749-818F-C168534B7167.root     outputFile=test.root

    
     
     
     
    
    tree = (TTree*) _file0->Get("TreeProducer/tree")
    tree->Draw("std_vector_Ele_r9[0]", "@std_vector_Ele_r9.size()>=1 && std_vector_Ele_r9[0]>0")

    tree->Draw("std_vector_Ele_r9[0]", "@std_vector_Ele_r9.size()>=1")

 
    
    
Example:

    /RelValMinBias_13/CMSSW_9_0_0_pre4-90X_mcRun2_asymptotic_v1-v1/GEN-SIM --> segfault
    /RelValMinBias_13/CMSSW_9_3_0_pre3-92X_upgrade2018_realistic_v8_resub-v1/GEN-SIM --> segfault
    /RelValMinBias_13/CMSSW_10_6_0-106X_upgrade2018_design_v3-v1/GEN-SIM  --> ok, but no, since I need the premix sample!
    
    
    /RelValPREMIXUP18_PU25/CMSSW_10_3_0_pre4-PU25ns_103X_upgrade2018_realistic_v4-v1/GEN-SIM-DIGI-RAW 

    
    
    
Chat:

    There are three ways to have one job process multiple different Runs of your choosing
    
    1) If you want N different Runs, first run N different jobs each writing a file with a different Run number. This can be done with the EmptySource using the option 'firstRun', from PoolSource use 'setRunNumber'. Then run a simple cmsRun job to merge all the files created into one file or just run your next job over all N files.
    
    2) If you are running a job using the EmptySource, you can specify for each new LuminosityBlock being generated, what Run number should be used
    
    process.source = cms.Source("EmptySource",
                                     numberEventsInLuminosityBlock = cms.untracked.uint32(100), #makes the job create more than 1 Lumi
                                     firstLuminosityBlockForEachRun = cms.untracked.VLuminosityBlockID( (2,1), (10,2), (35, 3) ) )
    process.maxEvents.input = 100*3 #want 3 lumis, each with its own run
    
    3) If you are starting from a ROOT file, then you can override the run number for each LuminosityBlock
    
    process.source = cms.Source("PoolSource",
                                     fileNames =...
                                     setRunNumberForEachLumi = cms.untracked.vuint32(2, 10, 35) )#assumes 3 lumis
    
    You can see the full options for each of the sources by doing
        edmPluginHelp -p EmptySource
        edmPluginHelp -p PoolSource
    
    
