Test with generation
====

GENSIM

    cmsRun ZEE_13TeV_TuneCUETP8M1_cfi_GEN_SIM.py

DIGI2RAW
    
    cmsDriver.py step2 --conditions auto:phase1_2018_realistic --pileup_input das:/RelValMinBias_13/CMSSW_9_0_0_pre4-90X_mcRun2_asymptotic_v1-v1/GEN-SIM  -n 10 --era Run2_2018 --eventcontent FEVTDEBUGHLT -s DIGI:pdigi_valid,L1,DIGI2RAW --datatier GEN-SIM-DIGI-RAW --pileup AVE_35_BX_25ns --geometry DB:Extended
    
    cmsRun step2_DIGI_L1_DIGI2RAW_PU.py
    
RAW2RECO

    cmsRun step3_RAW2DIGI_L1Reco_RECO_EI_PAT_VALIDATION_DQM_PU.py

    
Example:

    /RelValMinBias_13/CMSSW_9_0_0_pre4-90X_mcRun2_asymptotic_v1-v1/GEN-SIM 

