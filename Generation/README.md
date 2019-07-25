Test with generation
====

GENSIM

    cmsRun ZEE_13TeV_TuneCUETP8M1_cfi_GEN_SIM.py

DIGI2RAW
    
    voms-proxy-init -voms cms -rfc

    cmsDriver.py step2 --conditions auto:phase1_2018_realistic --pileup_input das:/RelValMinBias_13/CMSSW_9_0_0_pre4-90X_mcRun2_asymptotic_v1-v1/GEN-SIM  -n 10 --era Run2_2018 --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,DIGI2RAW --datatier GEN-SIM-DIGI-RAW --pileup AVE_35_BX_25ns --geometry DB:Extended
    
    cmsRun step2_DIGI_L1_DIGI2RAW_PU.py

    cmsDriver.py step2 --conditions auto:phase1_2018_realistic --pileup_input das:/RelValMinBias_13/CMSSW_9_0_0_pre4-90X_mcRun2_asymptotic_v1-v1/GEN-SIM  -n 10 --era Run2_2018 --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2018 --datatier GEN-SIM-DIGI-RAW --pileup AVE_35_BX_25ns --geometry DB:Extended
    
    cmsDriver.py step2 --conditions auto:phase1_2018_realistic --pileup_input das:/RelValMinBias_13/CMSSW_10_6_0-106X_upgrade2018_design_v3-v1/GEN-SIM   -n 10 --era Run2_2018 --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2018 --datatier GEN-SIM-DIGI-RAW --pileup AVE_35_BX_25ns --geometry DB:Extended
    step2_SIM.root -> ZEE_13TeV_TuneCUETP8M1_cfi_GEN_SIM.root
    
    step2_SIM.root -> ZEE_13TeV_TuneCUETP8M1_cfi_GEN_SIM.root
    

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
    
    
    
    cmsDriver.py step2 --datamix PreMix  --conditions auto:phase1_2018_realistic --pileup_input das:/RelValPREMIXUP18_PU25/CMSSW_10_3_0_pre4-PU25ns_103X_upgrade2018_realistic_v4-v1/GEN-SIM-DIGI-RAW   -n 10 --era Run2_2018 --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2018 --datatier GEN-SIM-DIGI-RAW --pileup AVE_35_BX_25ns --geometry DB:Extended
    
    Instructions here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideSimulation
    
    cmsRun step2_DIGI_L1_DIGI2RAW_HLT_PU.py
    
    
RAW2RECO

    cmsRun step3_RAW2DIGI_L1Reco_RECO_EI_PAT_VALIDATION_DQM_PU.py

    
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
    
    
