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

    
    