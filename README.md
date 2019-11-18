# EcalSIM
Instructions for simulation developments

Kate:

    lxplus-ECAL-sim

Where:

    /afs/cern.ch/user/a/amassiro/work/ECAL/SIM/CMSSW_10_6_0/src/ECALValidation/EcalSIM
    
    and for the PR:
    
    /afs/cern.ch/user/a/amassiro/work/ECAL/SIM/ToRebase/CMSSW_11_0_X_2019-10-06-2300/src
    
    
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
    
    
    mkdir ECALValidation
    cd ECALValidation/
    git clone git@github.com:amassiro/EcalSIM.git

    
Branch:

    git checkout -b amassiro_premix_OptionC_ECAL
    git checkout -b amassiro_premix_OptionC_2tags_ECAL
    
    git remote add origin git@github.com:amassiro/cmssw
    
    git fetch origin
    
    git push -u origin amassiro_premix_OptionC_ECAL
    git push -u origin amassiro_premix_OptionC_2tags_ECAL


Rebase: 
 
    git cms-rebase-topic amassiro:amassiro_premix_OptionC_2tags_ECAL
    

Just downlaod my branch:

    git cms-init
    git    cms-merge-topic    amassiro:amassiro_premix_OptionC_2tags_ECAL
    
    
Idea:

    correction_factor_for_premixed_sample_transparency = value_LC_prime / value_LC;

    Use the first IOV to define "value_LC_prime"
    
    
    NB: using IOV to define changes, not time!
    
    
    
    
    amassiro_premix_OptionC_2tags_ECAL
    --> completely rewritten code. New record in DB is needed to handle the "ratio" and get LC_prime 
    --> not simple workaround using "ref" or "lin" was found, keeping the current code and 
        the default value for MC (and Data), in simulation and reconstruction
        
Test runthematrix:

    runTheMatrix.py --what premix -l 250202.172 --label AMASSIROTEST --noCaf -t 8 -m 4500 -b 'fullSimPU2017_premix' --wm test

    runTheMatrix.py --what premix -l 250202.183 --label AMASSIROTEST --noCaf -t 8 -m 4500 -b 'fullSimPU2018_premix' --wm test

    
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
    
    
    
    
    
    