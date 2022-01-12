import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2018
configurations = os.path.dirname(configurations) # ggH2018
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight, getBaseWnAOD

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

################################################
################# SKIMS ########################
################################################

mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'

dataReco = 'Run2018_102X_nAODv7_Full2018v7'

fakeReco = dataReco

embedReco = 'Embedding2018_102X_nAODv7_Full2018v7'

mcSteps = 'MCl1loose2018v7__MCCorr2018v7_trigEffMC__l2loose__l2tightOR2018v7__trigFix{var}'#MCl1loose2018v7__MCCorr2018v7___l2loose__l2tightOR2018v7__trigFix{var}'

fakeSteps = 'DATAl1loose2018v7__l2loose__fakeW'

dataSteps = 'DATAl1loose2018v7__l2loose__l2tightOR2018v7'

embedSteps = 'DATAl1loose2018v7__l2loose__l2tightOR2018v7__Embedding'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, fakeReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)
embedDirectory = os.path.join(treeBaseDir, embedReco, embedSteps)

mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'
#mcCommonWeight_singlEl = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC*TriggerEffWeight_sngEl'
#mcCommonWeight_singlMu = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC*TriggerEffWeight_sngMu'
#mcCommonWeight_ElMu = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC*TriggerEffWeight_ElMu'
#mcCommonWeight_dblMu = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC*TriggerEffWeight_dblMu'
#mcCommonWeight_dblEl = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC*TriggerEffWeight_dblEl'
#mcCommonWeight_Trig = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC*TriggerEffWeight_2l'
mcCommonWeight_singlEl = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC*TriggerEffWeightMCTandP_sngEl'
mcCommonWeight_singlMu = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC*TriggerEffWeightMCTandP_sngMu'
mcCommonWeight_ElMu = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC*TriggerEffWeightMCTandP_ElMu'
mcCommonWeight_dblMu = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC*TriggerEffWeightMCTandP_dblMu'
mcCommonWeight_dblEl = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC*TriggerEffWeightMCTandP_dblEl'
mcCommonWeight_Trig = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC*TriggerEffWeightFixMCTandP_2l'#TriggerAltEffWeightMCTandP_2l' #FIX


###########################################
#############   SIGNALS  ##################
###########################################

#### ggH -> WW

samples['ggH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

samples['ggH_hww_singlEl'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight_singlEl,
    'FilesPerJob': 1,
}

samples['ggH_hww_singlMu'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight_singlMu,
    'FilesPerJob': 1,
}

samples['ggH_hww_ElMu'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight_ElMu,
    'FilesPerJob': 1,
}

samples['ggH_hww_dblMu'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight_dblMu,
    'FilesPerJob': 1,
}

samples['ggH_hww_dblEl'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight_dblEl,
    'FilesPerJob': 1,
}


samples['ggH_hww_Trig'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight_Trig,
    'FilesPerJob': 1,
}
