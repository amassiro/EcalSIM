# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein file:step2_SIM.root --fileout file:HIG-RunIISummer19UL17DIGIPremix-00001.root --mc --eventcontent PREMIXRAW --runUnscheduled --datatier GEN-SIM-DIGI --conditions 106X_mc2017_realistic_v6 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --nThreads 8 --geometry DB:Extended --datamix PreMix --era Run2_2017 --python_filename HIG-RunIISummer19UL17DIGIPremix-00001_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2017_cff import Run2_2017
from Configuration.ProcessModifiers.premix_stage2_cff import premix_stage2

process = cms.Process('DIGI2RAW',Run2_2017,premix_stage2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.DigiDM_cff')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('file:step2_SIM.root'),
    #setRunNumberForEachLumi = cms.untracked.vuint32(1, 2, 4, 5, 6, 9, 10, 14, 20, 22, 25, 30),  #assumes 7 lumis
    setRunNumberForEachLumi = cms.untracked.vuint32(
#                                                    299337,
#                                                    299338, 
#                                                    299339,
#                                                    299340,
#                                                    299341,
#                                                    299342,
#                                                    299343,
#                                                    299344,
#                                                    299345,
#                                                    299346,
#                                                    299347,
#                                                    299348,
#                                                    300000

                                                    298475,
                                                    298486, 
                                                    298615,
                                                    303454

 
                                                   ),  #assumes 7 lumis
    inputCommands = cms.untracked.vstring(
        'keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.PREMIXRAWoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:/tmp/amassiro/HIG-RunIISummer19UL17DIGIPremix-00001.root'),
    outputCommands = process.PREMIXRAWEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mixData.input.fileNames = cms.untracked.vstring([
  #'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/00002/1C56C5CD-24BC-A841-A5D5-FD70C468F890.root',
  #'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/00003/ED3110CF-AF42-A94C-B382-E7620DF2EAF1.root',
  #'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUAutumn18_102X_upgrade2018_realistic_v15-v1/00000/1B520F65-6F89-9843-A9DC-DB8ED0F88B5B.root'
   #'/store/mc/RunIISummer19ULPrePremix/Neutrino_E-10_gun/PREMIX/UL17_106X_mc2017_realistic_v6-v1/70025/17AA35B2-6C4D-7C46-B304-8A0844B4AEA0.root', # -> now issue here ...
   #'/store/mc/RunIISummer19ULPrePremix/Neutrino_E-10_gun/PREMIX/UL17_106X_mc2017_realistic_v6-v1/70025/DB999423-8252-0447-B7FE-764E58B8541C.root',
   #'/store/mc/RunIISummer19ULPrePremix/Neutrino_E-10_gun/PREMIX/UL17_106X_mc2017_realistic_v6-v1/70025/79107CE9-B5B4-DA43-8ACC-5EBBD78CEB32.root'
   
   #'/store/mc/RunIISummer19ULPrePremix/Neutrino_E-10_gun/PREMIX/UL17_106X_mc2017_realistic_v6-v1/70025/D58FA235-10D4-8C4C-863A-67D77BA41AA6.root',
    'file:/tmp/amassiro/D58FA235-10D4-8C4C-863A-67D77BA41AA6.root'
   
   #'/store/mc/RunIISummer19ULPrePremix/Neutrino_E-10_gun/PREMIX/UL17_106X_mc2017_realistic_v6-v1/70025/00A45230-7B63-1543-ADDF-07F657B30CE5.root',
   #'/store/mc/RunIISummer19ULPrePremix/Neutrino_E-10_gun/PREMIX/UL17_106X_mc2017_realistic_v6-v1/70025/260C68AE-E710-9749-BC6D-6A9C3702E5E0.root',
   #'/store/mc/RunIISummer19ULPrePremix/Neutrino_E-10_gun/PREMIX/UL17_106X_mc2017_realistic_v6-v1/70025/1798D750-4595-2F46-9F22-AF310CE389D5.root',
   #'/store/mc/RunIISummer19ULPrePremix/Neutrino_E-10_gun/PREMIX/UL17_106X_mc2017_realistic_v6-v1/70025/FE0E6562-7444-854F-9D17-3AA0D034068B.root',
   #'/store/mc/RunIISummer19ULPrePremix/Neutrino_E-10_gun/PREMIX/UL17_106X_mc2017_realistic_v6-v1/70025/60B0B300-B69A-1145-9E81-8D0F09E1C6C0.root',
   #'/store/mc/RunIISummer19ULPrePremix/Neutrino_E-10_gun/PREMIX/UL17_106X_mc2017_realistic_v6-v1/70025/AD1EF9BC-A015-7F40-8700-ECAC408A9849.root'
   
  ])


#
#    106X_mc2017_realistic_v7 
#    final GT for UL2017
#    laser tag EcalLaserAPDPNRatios_UL_2017_mc
#

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mc2017_realistic_v7', '')

#
# For version in "amassiro_premix_OptionC_2tags_ECAL"
#

process.GlobalTag.toGet = cms.VPSet(

     #
     # the tag used in the pre-mix library generation
     #
     cms.PSet(     record = cms.string("EcalLaserAPDPNRatiosMCRcd"),
                   tag = cms.string("EcalLaserAPDPNRatios_UL_2017_mc"),
                   connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                  ),

     #
     # data tag now used for MC
     #
     cms.PSet(     record = cms.string("EcalLaserAPDPNRatiosRcd"),
                   #tag = cms.string("EcalLaserAPDPNRatios_UL_2016_mc_3sigma"),
                   tag = cms.string("EcalLaserAPDPNRatios_weekly_hlt"),
                   connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
                  ),

#
#   https://twiki.cern.ch/twiki/bin/viewauth/CMS/EcalDB#Laser_APDPNRatios
#


)
     
#
#
#

## Very important, otherwise:
# 
# No "EcalLaserDbRecordMC" record found in the EventSetup.n
#
process.EcalLaserCorrectionServiceMC = cms.ESProducer("EcalLaserCorrectionServiceMC")
#
#
     
# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.PREMIXRAWoutput_step = cms.EndPath(process.PREMIXRAWoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.digi2raw_step,process.endjob_step,process.PREMIXRAWoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
