# EcalSIM
Instructions for simulation developments

Kate:

    lxplus-ECAL-sim

Where:

    /afs/cern.ch/user/a/amassiro/work/ECAL/SIM/CMSSW_10_6_0/src/ECALValidation/EcalSIM
    
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
    
    
    mkdir ECALValidation
    cd ECALValidation/
    git clone git@github.com:amassiro/EcalSIM.git

    
Branch:

    git checkout -b amassiro_premix_OptionC_ECAL
    
    git remote add origin git@github.com:amassiro/cmssw
    
    git fetch origin
    
    git push -u origin amassiro_premix_OptionC_ECAL

    