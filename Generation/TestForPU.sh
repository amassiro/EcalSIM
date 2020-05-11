

#  cmsDriver.py ZEE_13TeV_TuneCUETP8M1_cfi  \
#         --conditions auto:phase1_2018_realistic -n 500 \
#         --era Run2_2018 --relval 200000,100 -s GEN,SIM --datatier GEN-SIM \
#         --beamspot Realistic25ns13TeVEarly2018Collision --eventcontent FEVTDEBUG \
#         --io ZEE_13UP18_RD.io --python ZEE_13UP18_RD.py\
#         --conditions=111X_upgrade2018_realistic_RunDep_v1 --no_exec --fileout file:/tmp/amassiro/gen.root --nThreads 8 \
#         --python_filename ZEE_13TeV_TuneCUETP8M1_cfi_RunDepTest_GEN_SIM.py 
#     
# cmsRun ZEE_13TeV_TuneCUETP8M1_cfi_RunDepTest_GEN_SIM.py 



#   cmsDriver.py step2   --filein file:/tmp/amassiro/gen.root --fileout file:/tmp/amassiro/ZEE_13TeV_TuneCUETP8M1_cfi_RAW.root  \
#          --pileup_input "das:/RelValPREMIXUP18_PU25/CMSSW_11_1_0_pre2-PU25ns_111X_upgrade2018_realistic_RunDep_premix_v1-v1/PREMIX" \
#          --mc --eventcontent PREMIXRAW --runUnscheduled --datatier GEN-SIM-DIGI-RAW \
#          --conditions 111X_upgrade2018_realistic_RunDep_v1  \
#          --step DIGI,DATAMIX,L1,DIGI2RAW --nThreads 8 \
#           --procModifiers premix_stage2    --geometry DB:Extended --datamix PreMix --era Run2_2018 \
#           -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW  \
#            --io DIGIPRMXUP18_PU25_RD.io \
#           --python_filename Zee_DIGIPremix_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1000
#    

cmsRun Zee_DIGIPremix_cfg.py 


#  cmsDriver.py step1 --filein file:/tmp/amassiro/ZEE_13TeV_TuneCUETP8M1_cfi_RAW.root \
#           --fileout file:/tmp/amassiro/ZEE_13TeV_TuneCUETP8M1_cfi_RECO.root --mc --eventcontent AODSIM \
#           --runUnscheduled --datatier AODSIM --conditions 111X_upgrade2018_realistic_RunDep_v1 \
#           --step RAW2DIGI,L1Reco,RECO,RECOSIM --nThreads 8 --geometry DB:Extended --era Run2_2018 \
#           --python_filename RAW2RECO_Zee.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 500 
#     
cmsRun RAW2RECO_Zee.py
    
# 
#    cmsDriver.py step1 --filein file:/tmp/amassiro/ZEE_13TeV_TuneCUETP8M1_cfi_RECO.root --fileout file:/tmp/amassiro/ZEE_13TeV_TuneCUETP8M1_cfi_MINIAOD.root \
#           --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 111X_upgrade2018_realistic_RunDep_v1 \
#           --step PAT --nThreads 8 --geometry DB:Extended --era Run2_2018 --python_filename MINIAOD_Zee.py\
#           --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 9600 \
#           --customise_commands "del process.patTrigger; del process.selectedPatTrigger; del process.slimmedPatTrigger;   process.MINIAODSIMoutput.outputCommands.append('keep *_particleFlowSuperClusterECAL_*_*');"
#     
  
cmsRun MINIAOD_Zee.py
  

cmsRun dumpMC.py  inputFiles=file:/tmp/amassiro/ZEE_13TeV_TuneCUETP8M1_cfi_MINIAOD.root    outputFile=test.1.root
  