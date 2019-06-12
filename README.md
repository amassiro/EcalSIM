# EcalSIM
Instructions for simulation developments

Where:

    /afs/cern.ch/user/a/amassiro/work/ECAL/SIM/CMSSW_10_6_0/src/ECALValidation/EcalSIM
    
Install:

    cmsrel CMSSW_10_6_0
    cd CMSSW_10_6_0/src/
    cmsenv
    git cms-init

    git-cms-addpkg  SimCalorimetry/EcalSimAlgos
    git-cms-addpkg  SimG4CMS/Calo
    git-cms-addpkg  RecoLocalCalo/EcalRecProducers
    
    
    mkdir ECALValidation
    cd ECALValidation/
    git clone git@github.com:amassiro/EcalSIM.git
