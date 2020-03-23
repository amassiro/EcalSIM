Pileup studies for time dependent MC
====

Study the assumption of 1 unique pileup library in the mixing, as far as photostatistics of pileup is concerned.

Approach:

    Add a gaussian smearing in the mixing for the pileup. In principle only intime pileup is problematic, but the smearing is added consistently for all.
    
Compare +10%, +20%, +50%, +70% smearing.

Data:

    scp amassiro@lxplus.cern.ch:/afs/cern.ch/user/a/amassiro/work/ECAL/SIM/CMSSW_11_1_0_pre4/src/ECALValidation/EcalSIM/Generation/test.*perc.root   .
    
    r99t drawSmearing.cxx\(\"std_vector_Ele_pt\",10,0,100\)
    r99t drawSmearing.cxx\(\"std_vector_Ele_sigmaIetaIeta\",40,0,0.05\)
    r99t drawSmearing.cxx\(\"std_vector_Ele_sigmaIphiIphi\",40,0,0.05\)
    r99t drawSmearing.cxx\(\"std_vector_Ele_r9\",40,0,1.20\)
    r99t drawSmearing.cxx\(\"std_vector_Ele_dr03EcalRecHitSumEt\",40,0.00,10.00\)
    
    
