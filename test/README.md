After the PR, some tests with official samples.

New sample, 11th May 2020:

    /RelValZEE_13UP18_RD/CMSSW_11_1_0_pre7-PUpmx25ns_110X_upgrade2018_realistic_v9_RD_1HS-v1/GEN-SIM-RECO
    /RelValZEE_13UP18_RD/CMSSW_11_1_0_pre7-PUpmx25ns_110X_upgrade2018_realistic_v9_RD_1HS-v1/MINIAODSIM
    
Use EcalZee package

    cmsRun dumpMC.py  inputFiles=file:/tmp/amassiro/HIG-RunIISummer19UL17MiniAOD-00001.root     outputFile=test.root

    cmsRun dumpMC.py   inputFiles=many::files.py \
                       outputFile=/tmp/amassiro/test.root
 
 

Plot
====


    tree = (TTree*) _file0->Get("TreeProducer/tree")
    tree->Draw("mll", "mll>10")
    
    tree->Draw("run:lumi","", "colz")
      
      