# EcalSIM
Instructions for simulation developments

Kate:

    lxplus-ECAL-sim

Where:

    /afs/cern.ch/user/a/amassiro/work/ECAL/SIM/CMSSW_10_6_0/src/ECALValidation/EcalSIM
    
    and for the PR:
    
    /afs/cern.ch/user/a/amassiro/work/ECAL/SIM/ToRebase/CMSSW_11_0_X_2019-10-06-2300/src
    /afs/cern.ch/user/a/amassiro/work/ECAL/SIM/ToRebase/CMSSW_11_0_X_2019-10-17-2300/src
    
    
Install:

    cmsrel CMSSW_10_6_0
    cd CMSSW_10_6_0/src/
    cmsenv
    git cms-init

    git-cms-addpkg  SimCalorimetry/EcalSimAlgos
    git-cms-addpkg  SimCalorimetry/EcalSimProducers
    git-cms-addpkg  SimG4CMS/Calo
    git-cms-addpkg  RecoLocalCalo/EcalRecProducers
    git-cms-addpkg  CalibCalorimetry/EcalLaserCorrection
    
    git-cms-addpkg  CondFormats/DataRecord/
    git-cms-addpkg  CondFormats/EcalObjects/
    git-cms-addpkg  CondCore/EcalPlugins/ 
    
    
    git-cms-addpkg  Configuration/PyReleaseValidation/ 

        
    mkdir ECALValidation
    cd ECALValidation/
    git clone git@github.com:amassiro/EcalSIM.git

    
Branch:

    git checkout -b amassiro_premix_OptionC_ECAL
    git checkout -b amassiro_premix_OptionC_2tags_ECAL
    git checkout -b amassiro_premix_OptionC_2tags_ECAL_11_0_X
    
    git remote add origin git@github.com:amassiro/cmssw
    
    git fetch origin
    
    git push -u origin amassiro_premix_OptionC_ECAL
    git push -u origin amassiro_premix_OptionC_2tags_ECAL
    git push -u origin amassiro_premix_OptionC_2tags_ECAL_11_0_X


Rebase: 
 
    git cms-rebase-topic amassiro:amassiro_premix_OptionC_2tags_ECAL
    git cms-rebase-topic amassiro:amassiro_premix_OptionC_2tags_ECAL_11_0_X
    

Just downlaod my branch:

    git cms-init
    git    cms-merge-topic    amassiro:amassiro_premix_OptionC_2tags_ECAL
    git    cms-merge-topic    amassiro:amassiro_premix_OptionC_2tags_ECAL_11_0_X
    
    
Idea:

    correction_factor_for_premixed_sample_transparency = value_LC_prime / value_LC;

    Use the first IOV to define "value_LC_prime"
    
    
    NB: using IOV to define changes, not time!
    
    
    
    
    amassiro_premix_OptionC_2tags_ECAL
    --> completely rewritten code. New record in DB is needed to handle the "ratio" and get LC_prime 
    --> not simple workaround using "ref" or "lin" was found, keeping the current code and 
        the default value for MC (and Data), in simulation and reconstruction
        
Test runthematrix:

    runTheMatrix.py --what premix -l 250202.183 --label AMASSIROTEST2 --noCaf -t 8 -m 4500 -b 'fullSimPU2018_premix' --wm test

    
        
    Preparing to run 250202.183 TTbar_13UP18_RD_test+TTbar_13UP18_RD_test+DIGIPRMXUP18_PU25_RD_test+RECOPRMXUP18_PU25_RD_test+HARVESTUP18_PU25
    
    # in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/CMSSW_11_0_0_pre8/src dryRun for 'cd 250202.183_TTbar_13UP18_RD_test+TTbar_13UP18_RD_test+DIGIPRMXUP18_PU25_RD_test+RECOPRMXUP18_PU25_RD_test+HARVESTUP18_PU25
     cmsDriver.py TTbar_13TeV_TuneCUETP8M1_cfi  --conditions auto:phase1_2018_realistic -n 10 --customise_commands "process.source.numberEventsInLuminosityBlock=cms.untracked.uint32(5) \n process.GlobalTag.toGet = cms.VPSet( cms.PSet(     record = cms.string('EcalLaserAPDPNRatiosRcd'),  tag = cms.string('EcalLaserAPDPNRatios_Run_Dep_MC'),  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS') ) ) " --era Run2_2018 --relval 2000,50 -s GEN,SIM --datatier GEN-SIM --beamspot Realistic25ns13TeVEarly2017Collision --eventcontent FEVTDEBUG --io TTbar_13UP18_RD_test.io --python TTbar_13UP18_RD_test.py --fileout file:step1.root  --nThreads 8 > step1_TTbar_13UP18_RD_test+TTbar_13UP18_RD_test+DIGIPRMXUP18_PU25_RD_test+RECOPRMXUP18_PU25_RD_test+HARVESTUP18_PU25.log  2>&1
     
    
    # in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/CMSSW_11_0_0_pre8/src dryRun for 'cd 250202.183_TTbar_13UP18_RD_test+TTbar_13UP18_RD_test+DIGIPRMXUP18_PU25_RD_test+RECOPRMXUP18_PU25_RD_test+HARVESTUP18_PU25
     cmsDriver.py step2  --datamix PreMix --conditions auto:phase1_2018_realistic --pileup_input das:/RelValPREMIXUP18_PU25/CMSSW_10_6_0-PU25ns_106X_upgrade2018_realistic_v4-v1/PREMIX --customise_commands "process.EcalLaserCorrectionServiceMC = cms.ESProducer('EcalLaserCorrectionServiceMC') \n process.GlobalTag.toGet = cms.VPSet( cms.PSet(     record = cms.string('EcalLaserAPDPNRatiosMCRcd'),  tag = cms.string('EcalLaserAPDPNRatios_Run_Dep_MC_first_IOV'),  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS') ), cms.PSet(     record = cms.string('EcalLaserAPDPNRatiosRcd'),  tag = cms.string('EcalLaserAPDPNRatios_Run_Dep_MC'),  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS') ) )  \n process.ecal_sim_parameter_map.timeDependent=cms.bool(True) \n process.source.setRunNumberForEachLumi = cms.untracked.vuint32(315257,316083)" --era Run2_2018 --procModifiers premix_stage2 -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW,HLT:@relval2018 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --eventcontent FEVTDEBUGHLT --io DIGIPRMXUP18_PU25_RD_test.io --python DIGIPRMXUP18_PU25_RD_test.py -n 100  --filein  file:step1.root  --fileout file:step2.root  --nThreads 8 > step2_TTbar_13UP18_RD_test+TTbar_13UP18_RD_test+DIGIPRMXUP18_PU25_RD_test+RECOPRMXUP18_PU25_RD_test+HARVESTUP18_PU25.log  2>&1
     
    
    # in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/CMSSW_11_0_0_pre8/src dryRun for 'cd 250202.183_TTbar_13UP18_RD_test+TTbar_13UP18_RD_test+DIGIPRMXUP18_PU25_RD_test+RECOPRMXUP18_PU25_RD_test+HARVESTUP18_PU25
     cmsDriver.py step3  --conditions auto:phase1_2018_realistic -n 10 --customise_commands "process.EcalLaserCorrectionServiceMC = cms.ESProducer('EcalLaserCorrectionServiceMC') \n process.GlobalTag.toGet = cms.VPSet( cms.PSet(     record = cms.string('EcalLaserAPDPNRatiosMCRcd'),  tag = cms.string('EcalLaserAPDPNRatios_Run_Dep_MC_first_IOV'),  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS') ), cms.PSet(     record = cms.string('EcalLaserAPDPNRatiosRcd'),  tag = cms.string('EcalLaserAPDPNRatios_Run_Dep_MC'),  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS') ) )  \n process.ecal_sim_parameter_map.timeDependent=cms.bool(True) " --era Run2_2018 --runUnscheduled  --procModifiers premix_stage2 -s RAW2DIGI,L1Reco,RECO,RECOSIM,EI,PAT,VALIDATION:@standardValidationNoHLT+@miniAODValidation,DQM:@standardDQMFakeHLT+@miniAODDQM --datatier GEN-SIM-RECO,MINIAODSIM,DQMIO --eventcontent RECOSIM,MINIAODSIM,DQM --io RECOPRMXUP18_PU25_RD_test.io --python RECOPRMXUP18_PU25_RD_test.py --filein  file:step2.root  --fileout file:step3.root  --nThreads 8 > step3_TTbar_13UP18_RD_test+TTbar_13UP18_RD_test+DIGIPRMXUP18_PU25_RD_test+RECOPRMXUP18_PU25_RD_test+HARVESTUP18_PU25.log  2>&1
     
    
    # in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/CMSSW_11_0_0_pre8/src dryRun for 'cd 250202.183_TTbar_13UP18_RD_test+TTbar_13UP18_RD_test+DIGIPRMXUP18_PU25_RD_test+RECOPRMXUP18_PU25_RD_test+HARVESTUP18_PU25
     cmsDriver.py step4  --conditions auto:phase1_2018_realistic -s HARVESTING:@standardValidationNoHLT+@standardDQMFakeHLT+@miniAODValidation+@miniAODDQM --filetype DQM --geometry DB:Extended --era Run2_2018 --mc  --io HARVESTUP18_PU25.io --python HARVESTUP18_PU25.py -n 100  --filein file:step3_inDQM.root --fileout file:step4.root  > step4_TTbar_13UP18_RD_test+TTbar_13UP18_RD_test+DIGIPRMXUP18_PU25_RD_test+RECOPRMXUP18_PU25_RD_test+HARVESTUP18_PU25.log  2>&1
     
    250202.183_TTbar_13UP18_RD_test+TTbar_13UP18_RD_test+DIGIPRMXUP18_PU25_RD_test+RECOPRMXUP18_PU25_RD_test+HARVESTUP18_PU25 Step0-PASSED Step1-PASSED Step2-PASSED Step3-PASSED  - time date Thu Nov 21 18:00:23 2019-date Thu Nov 21 18:00:23 2019; exit: 0 0 0 0
    1 1 1 1 tests passed, 0 0 0 0 failed


    
    
    
    
    
    
    
    cmsRun ${LOCAL_TEST_DIR}/PrePoolInputTest_cfg.py RunPerLumiTest.root 50 1 25 1 5 || die 'Failure using PrePoolInputTest_cfg.py' $?
    
    cmsRun ${LOCAL_TEST_DIR}/RunPerLumiTest_cfg.py 25 >& ${LOCAL_TMP_DIR}/RunPerLumiTest.txt || die 'Failure using RunPerLumiTest_cfg.py' $?
    grep 'record' ${LOCAL_TMP_DIR}/RunPerLumiTest.txt | cut -d ' ' -f 4-11 > ${LOCAL_TMP_DIR}/RunPerLumiTest.filtered.txt
    diff ${LOCAL_TEST_DIR}/unit_test_outputs/RunPerLumiTest.filtered.txt ${LOCAL_TMP_DIR}/RunPerLumiTest.filtered.txt || die 'incorrect output using RunPerLumiTest_cfg.py' $? 
    
    cmsRun ${LOCAL_TEST_DIR}/RunPerLumiTest_cfg.py 50 >& ${LOCAL_TMP_DIR}/tooManyLumis.txt && die 'RunPerLumiTest_cfg.py should have failed but did not' $?
    grep "MismatchedInputFiles" ${LOCAL_TMP_DIR}/tooManyLumis.txt || die  'RunPerLumiTest_cfg.py should have failed but did not' $?
    
    
    
    runTheMatrix.py --what premix -l 250202.172 --label AMASSIROTEST --noCaf -t 8 -m 4500 -b 'fullSimPU2017_premix' --wm test

    
    
    # in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/ToRebase/CMSSW_11_0_X_2019-10-06-2300/src dryRun for 'cd 250202.172_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25
    cmsDriver.py TTbar_13TeV_TuneCUETP8M1_cfi  --conditions auto:phase1_2017_realistic -n 10 --era Run2_2017 --eventcontent FEVTDEBUG --relval 9000,50 -s GEN,SIM --datatier GEN-SIM --beamspot Realistic25ns13TeVEarly2017Collision --io TTbar_13UP17.io --python TTbar_13UP17.py --fileout file:step1.root  --nThreads 8 > step1_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1
    
    
    #    in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/ToRebase/CMSSW_11_0_X_2019-10-06-2300/src dryRun for 'cd 250202.172_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25
    cmsDriver.py step2  --datamix PreMix --conditions auto:phase1_2017_realistic --pileup_input das:/RelValPREMIXUP17_PU25/CMSSW_10_6_0-PU25ns_106X_mc2017_realistic_v3-v1/PREMIX --customise_commands "process.EcalLaserCorrectionServiceMC = cms.ESProducer('EcalLaserCorrectionServiceMC')" --era Run2_2017 --procModifiers premix_stage2 -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW,HLT:@relval2017 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --eventcontent FEVTDEBUGHLT --io DIGIPRMXUP17_PU25_RD.io --python DIGIPRMXUP17_PU25_RD.py -n 100  --filein  file:step1.root  --fileout file:step2.root  --nThreads 8 > step2_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1
    
    
    
    
    
    process.GlobalTag.toGet = cms.VPSet(

     #
     # the tag used in the pre-mix library generation
     #
     cms.PSet(     record = cms.string("EcalLaserAPDPNRatiosMCRcd"),
                   tag = cms.string("EcalLaserAPDPNRatios_UL_2017_mc"),
                   connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                  ),

                  
                  
                  
                  
                  
    
    cmsDriver.py step2  --datamix PreMix --conditions auto:phase1_2017_realistic --pileup_input das:/RelValPREMIXUP17_PU25/CMSSW_10_6_0-PU25ns_106X_mc2017_realistic_v3-v1/PREMIX --customise_commands "process.EcalLaserCorrectionServiceMC = cms.ESProducer("EcalLaserCorrectionServiceMC")" --era Run2_2017 --procModifiers premix_stage2 -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW,HLT:@relval2017 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --eventcontent FEVTDEBUGHLT --io DIGIPRMXUP17_PU25_RD.io --python DIGIPRMXUP17_PU25_RD.py -n 100  --filein  file:step1.root  --fileout file:step2.root  --nThreads 8 
    
    
    cmsDriver.py step2  --datamix PreMix --conditions auto:phase1_2017_realistic --pileup_input das:/RelValPREMIXUP17_PU25/CMSSW_10_6_0-PU25ns_106X_mc2017_realistic_v3-v1/PREMIX --era Run2_2017 --procModifiers premix_stage2 -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW,HLT:@relval2017 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --eventcontent FEVTDEBUGHLT --io DIGIPRMXUP17_PU25_RD.io --python DIGIPRMXUP17_PU25_RD.py -n 100  --filein  file:step1.root  --fileout file:step2.root  --nThreads 8 
    
    
    
    
    
    
    
    
    
    
    
    
    #    in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/ToRebase/CMSSW_11_0_X_2019-10-06-2300/src dryRun for 'cd 250202.172_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25
    cmsDriver.py step3  --conditions auto:phase1_2017_realistic -n 10 --era Run2_2017 --eventcontent RECOSIM,MINIAODSIM,DQM --runUnscheduled  --procModifiers premix_stage2 -s RAW2DIGI,L1Reco,RECO,RECOSIM,EI,PAT,VALIDATION:@standardValidationNoHLT+@miniAODValidation,DQM:@standardDQMFakeHLT+@miniAODDQM --datatier GEN-SIM-RECO,MINIAODSIM,DQMIO --io RECOPRMXUP17_PU25.io --python RECOPRMXUP17_PU25.py --filein  file:step2.root  --fileout file:step3.root  --nThreads 8 > step3_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1
    
    
    #    in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/ToRebase/CMSSW_11_0_X_2019-10-06-2300/src dryRun for 'cd 250202.172_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25
    cmsDriver.py step4  --conditions auto:phase1_2017_realistic -s HARVESTING:@standardValidationNoHLT+@standardDQMFakeHLT+@miniAODValidation+@miniAODDQM --filetype DQM --geometry DB:Extended --era Run2_2017 --mc  --io HARVESTUP17_PU25.io --python HARVESTUP17_PU25.py -n 100  --filein file:step3_inDQM.root --fileout file:step4.root  > step4_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1
    
    
    
    
    
    
    
    runTheMatrix.py --what premix -l 250202.172 --label AMASSIROTEST --noCaf -t 8 -m 4500 -b 'fullSimPU2017_premix' --wm test
    
    
    
    Preparing to run 250202.172 TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25
    
    # in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/CMSSW_11_0_0_pre8/src/ECALValidation/EcalSIM/Generation dryRun for 'cd 250202.172_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25
     cmsDriver.py TTbar_13TeV_TuneCUETP8M1_cfi  --conditions auto:phase1_2017_realistic -n 10 --era Run2_2017 --eventcontent FEVTDEBUG --relval 9000,50 -s GEN,SIM --datatier GEN-SIM --beamspot Realistic25ns13TeVEarly2017Collision --io TTbar_13UP17.io --python TTbar_13UP17.py --fileout file:step1.root  --nThreads 8 > step1_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1
     
    
    # in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/CMSSW_11_0_0_pre8/src/ECALValidation/EcalSIM/Generation dryRun for 'cd 250202.172_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25
     cmsDriver.py step2  --datamix PreMix --conditions auto:phase1_2017_realistic --pileup_input das:/RelValPREMIXUP17_PU25/CMSSW_10_6_0-PU25ns_106X_mc2017_realistic_v3-v1/PREMIX --customise_commands process.EcalLaserCorrectionServiceMC = cms.ESProducer('EcalLaserCorrectionServiceMC') --era Run2_2017 --procModifiers premix_stage2 -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW,HLT:@relval2017 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --eventcontent FEVTDEBUGHLT --io DIGIPRMXUP17_PU25_RD.io --python DIGIPRMXUP17_PU25_RD.py -n 100  --filein  file:step1.root  --fileout file:step2.root  --nThreads 8 > step2_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1
     
     cmsDriver.py step2  --datamix PreMix --conditions auto:phase1_2017_realistic --pileup_input das:/RelValPREMIXUP17_PU25/CMSSW_10_6_0-PU25ns_106X_mc2017_realistic_v3-v1/PREMIX --customise_commands "process.EcalLaserCorrectionServiceMC = cms.ESProducer('EcalLaserCorrectionServiceMC')" --era Run2_2017 --procModifiers premix_stage2 -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW,HLT:@relval2017 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --eventcontent FEVTDEBUGHLT --io DIGIPRMXUP17_PU25_RD.io --python DIGIPRMXUP17_PU25_RD.py -n 100  --filein  file:step1.root  --fileout file:step2.root  --nThreads 8 > step2_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1

     cmsDriver.py step2  --datamix PreMix --conditions auto:phase1_2017_realistic --pileup_input das:/RelValPREMIXUP17_PU25/CMSSW_10_6_0-PU25ns_106X_mc2017_realistic_v3-v1/PREMIX --customise_commands "process.EcalLaserCorrectionServiceMC = cms.ESProducer('EcalLaserCorrectionServiceMC') 
                                                                  process.GlobalTag.toGet = cms.VPSet(cms.PSet(     record = cms.string('EcalLaserAPDPNRatiosMCRcd'),  tag = cms.string('EcalLaserAPDPNRatios_UL_2017_mc'),                                                                          connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS') ) )" --era Run2_2017 --procModifiers premix_stage2 -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW,HLT:@relval2017 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --eventcontent FEVTDEBUGHLT --io DIGIPRMXUP17_PU25_RD.io --python DIGIPRMXUP17_PU25_RD.py -n 100  --filein  file:step1.root  --fileout file:step2.root  --nThreads 8 > step2_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1

      process.ecal_sim_parameter_map.timeDependent=cms.untracked.bool(True)
                                                                  
      cmsDriver.py step2  --datamix PreMix --conditions auto:phase1_2017_realistic --pileup_input das:/RelValPREMIXUP17_PU25/CMSSW_10_6_0-PU25ns_106X_mc2017_realistic_v3-v1/PREMIX --customise_commands "process.EcalLaserCorrectionServiceMC = cms.ESProducer('EcalLaserCorrectionServiceMC') \n process.GlobalTag.toGet = cms.VPSet( cms.PSet(     record = cms.string('EcalLaserAPDPNRatiosMCRcd'),  tag = cms.string('EcalLaserAPDPNRatios_UL_2017_mc'),  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS') ) )" --era Run2_2017 --procModifiers premix_stage2 -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW,HLT:@relval2017 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --eventcontent FEVTDEBUGHLT --io DIGIPRMXUP17_PU25_RD.io --python DIGIPRMXUP17_PU25_RD.py -n 100  --filein  file:step1.root  --fileout file:step2.root  --nThreads 8 > step2_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1
                                                        
      cmsDriver.py step2  --datamix PreMix --conditions auto:phase1_2017_realistic --pileup_input das:/RelValPREMIXUP17_PU25/CMSSW_10_6_0-PU25ns_106X_mc2017_realistic_v3-v1/PREMIX --customise_commands "process.EcalLaserCorrectionServiceMC = cms.ESProducer('EcalLaserCorrectionServiceMC') \n process.GlobalTag.toGet = cms.VPSet( cms.PSet(     record = cms.string('EcalLaserAPDPNRatiosMCRcd'),  tag = cms.string('EcalLaserAPDPNRatios_UL_2017_mc'),  connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS') ) ) \n process.ecal_sim_parameter_map.timeDependent=cms.untracked.bool(True)    " --era Run2_2017 --procModifiers premix_stage2 -s DIGI:pdigi_valid,DATAMIX,L1,DIGI2RAW,HLT:@relval2017 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --eventcontent FEVTDEBUGHLT --io DIGIPRMXUP17_PU25_RD.io --python DIGIPRMXUP17_PU25_RD.py -n 100  --filein  file:step1.root  --fileout file:step2.root  --nThreads 8 > step2_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1

      
      
    # in: /afs/cern.ch/work/a/amassiro/ECAL/SIM/CMSSW_11_0_0_pre8/src/ECALValidation/EcalSIM/Generation dryRun for 'cd 250202.172_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25
     cmsDriver.py step3  --conditions auto:phase1_2017_realistic -n 10 --era Run2_2017 --eventcontent RECOSIM,MINIAODSIM,DQM --runUnscheduled  --procModifiers premix_stage2 -s RAW2DIGI,L1Reco,RECO,RECOSIM,EI,PAT,VALIDATION:@standardValidationNoHLT+@miniAODValidation,DQM:@standardDQMFakeHLT+@miniAODDQM --datatier GEN-SIM-RECO,MINIAODSIM,DQMIO --io RECOPRMXUP17_PU25.io --python RECOPRMXUP17_PU25.py --filein  file:step2.root  --fileout file:step3.root  --nThreads 8 > step3_TTbar_13UP17+TTbar_13UP17+DIGIPRMXUP17_PU25_RD+RECOPRMXUP17_PU25+HARVESTUP17_PU25.log  2>&1
     

    
    