import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

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

mcProduction = 'Summer16_102X_nAODv5_Full2016v6'

fakeReco = 'Run2016_102X_nAODv5_Full2016v6'

dataReco = 'Run2016_102X_nAODv5_Full2016v6'

mcSteps = 'MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6{var}_weighted'

fakeSteps = 'DATAl1loose2016v6__l2loose__fakeW_weighted'

dataSteps = 'DATAl1loose2016v6__l2loose__l2tightOR2016v6_weighted'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  #treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
    treeBaseDir = '/eos/user/c/cprieels/work/TopPlusDMRunIILegacyRootfiles/'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
        #return '/afs/cern.ch/user/y/yiiyama/public/hwwvirtual/Summer16/l2tightOR__{var}'.format(var=var)
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))
        #return '/afs/cern.ch/user/y/yiiyama/public/hwwvirtual/Summer16/l2tightOR'

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, fakeReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
    ['B','Run2016B-Nano1June2019_ver2-v1'],
    ['C','Run2016C-Nano1June2019-v1'],
    ['D','Run2016D-Nano1June2019-v1'],
    ['E','Run2016E-Nano1June2019-v1'],
    ['F','Run2016F-Nano1June2019-v1'],
    ['G','Run2016G-Nano1June2019-v1'],
    ['H','Run2016H-Nano1June2019-v1']
]

DataSets = ['MuonEG','SingleMuon','SingleElectron','DoubleMuon', 'DoubleEG']

DataTrig = {
    'MuonEG'         : ' Trigger_ElMu' ,
    'SingleMuon'     : '!Trigger_ElMu && Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_ElMu && !Trigger_sngMu && Trigger_sngEl',
    'DoubleMuon'     : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && Trigger_dblMu',
    'DoubleEG'       : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && !Trigger_dblMu && Trigger_dblEl'
}

#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

###### DY #######

ptllDYW_NLO = '(0.876979+gen_ptll*(4.11598e-03)-(2.35520e-05)*gen_ptll*gen_ptll)*(1.10211 * (0.958512 - 0.131835*TMath::Erf((gen_ptll-14.1972)/10.1525)))*(gen_ptll<140)+0.891188*(gen_ptll>=140)'
ptllDYW_LO  = '(8.61313e-01+gen_ptll*4.46807e-03-1.52324e-05*gen_ptll*gen_ptll)*(1.08683 * (0.95 - 0.0657370*TMath::Erf((gen_ptll-11.)/5.51582)))*(gen_ptll<140)+1.141996*(gen_ptll>=140)'

files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO')


samples['DY'] = {
    'name': files,
    'weight': mcCommonWeight + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0))',
    'FilesPerJob': 4,
}
addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)

###### Top #######

samples['ttbar'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

addSampleWeight(samples,'ttbar','TTTo2L2Nu','Top_pTrw')

files =  nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_top')

samples['singleTop'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

#IMPORTANT!! TO BE USED TO FIX THE CROSS-SECTIONS OF SOME SAMPLES                                             
addSampleWeight(samples,'singleTop','ST_t-channel_antitop','3.068')
addSampleWeight(samples,'singleTop','ST_t-channel_top','3.068')

samples['TTToSemiLeptonic'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'TTToSemiLeptonic'),
    'weight': mcCommonWeight,
    'FilesPerJob': 2,
}

samples['ttV'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'TTZjets') + nanoGetSampleFiles(mcDirectory, 'TTWJetsToLNu_ext1'),
    'weight': mcCommonWeight,
    'FilesPerJob': 2,
}


###### WW ########

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu'),
    'weight': mcCommonWeight + '*nllW', # temporary - nllW module not run on PS and UE variation samples
    'FilesPerJob': 1
}

######## Vg ########

files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
    nanoGetSampleFiles(mcDirectory, 'Zg')

samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*(!(Gen_ZGstar_mass > 0))',
    'FilesPerJob': 4
}

######## VgS ########

files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
    nanoGetSampleFiles(mcDirectory, 'Zg') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')

samples['VgS'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 4,
    'subsamples': {
      'L': 'gstarLow',
      'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'VgS', 'Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS', 'Zg', '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples, 'VgS', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')

############ VZ ############

files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')

samples['VZ'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.11',
    'FilesPerJob': 4
}

########## VVV #########

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWW')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}


###########################################
################# SIGNALS #################
###########################################

signals = []
signalDir = '/eos/user/c/cprieels/work/TopPlusDMRunIILegacyRootfiles/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6_weighted/'

samples['TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_50'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_50'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_50')

samples['TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_100'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_100'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_100')

samples['TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_150'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_150'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_150')

samples['TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_200'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_200'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_200')

samples['TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_250'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_250'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_250')

samples['TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_300'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_300'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_300')

samples['TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_350'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_350'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_350')

samples['TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_400'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_400'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_400')

samples['TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_450'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_450'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_450')

samples['TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_500'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_500'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_pseudoscalar_LO_Mchi_1_Mphi_500')


samples['TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_50'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_50'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_50')

samples['TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_100'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_100'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_100')

samples['TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_150'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_150'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_150')

samples['TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_200'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_200'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_200')

samples['TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_250'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_250'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_250')

samples['TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_300'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_300'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_300')

samples['TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_350'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_350'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_350')

samples['TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_400'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_400'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_400')

samples['TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_450'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_450'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_450')

samples['TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_500'] = {
    'name': nanoGetSampleFiles(signalDir, 'TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_500'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 1,
}
signals.append('TTbarDMJets_Dilepton_scalar_LO_Mchi_1_Mphi_500')


"""
samples['DMscalar_Dilepton_top_tWChan_Mchi1_Mphi10'] = {
    'name': nanoGetSampleFiles(signalDir, 'DMscalar_Dilepton_top_tWChan_Mchi1_Mphi10'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 10,
}
signals.append('DMscalar_Dilepton_top_tWChan_Mchi1_Mphi10')

samples['DMscalar_Dilepton_top_tWChan_Mchi1_Mphi20'] = {
    'name': nanoGetSampleFiles(signalDir, 'DMscalar_Dilepton_top_tWChan_Mchi1_Mphi20'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 10,
}
signals.append('DMscalar_Dilepton_top_tWChan_Mchi1_Mphi20')

samples['DMscalar_Dilepton_top_tWChan_Mchi1_Mphi50'] = {
    'name': nanoGetSampleFiles(signalDir, 'DMscalar_Dilepton_top_tWChan_Mchi1_Mphi50'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 10,
}
signals.append('DMscalar_Dilepton_top_tWChan_Mchi1_Mphi50')

files = nanoGetSampleFiles(signalDir, 'DMscalar_Dilepton_top_tWChan_Mchi1_Mphi100') + \
        nanoGetSampleFiles(signalDir, 'DMscalar_Dilepton_top_tWChan_Mchi1_Mphi100_ext')

samples['DMscalar_Dilepton_top_tWChan_Mchi1_Mphi100'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 10,
}
signals.append('DMscalar_Dilepton_top_tWChan_Mchi1_Mphi100')

samples['DMscalar_Dilepton_top_tWChan_Mchi1_Mphi200'] = {
    'name': nanoGetSampleFiles(signalDir, 'DMscalar_Dilepton_top_tWChan_Mchi1_Mphi200'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 10,
}
signals.append('DMscalar_Dilepton_top_tWChan_Mchi1_Mphi200')

samples['DMscalar_Dilepton_top_tWChan_Mchi1_Mphi300'] = {
    'name': nanoGetSampleFiles(signalDir, 'DMscalar_Dilepton_top_tWChan_Mchi1_Mphi300'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 10,
}
signals.append('DMscalar_Dilepton_top_tWChan_Mchi1_Mphi300')

samples['DMscalar_Dilepton_top_tWChan_Mchi1_Mphi500'] = {
    'name': nanoGetSampleFiles(signalDir, 'DMscalar_Dilepton_top_tWChan_Mchi1_Mphi500'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 10,
}
signals.append('DMscalar_Dilepton_top_tWChan_Mchi1_Mphi500')

samples['DMscalar_Dilepton_top_tWChan_Mchi1_Mphi1000'] = {
    'name': nanoGetSampleFiles(signalDir, 'DMscalar_Dilepton_top_tWChan_Mchi1_Mphi1000'),
    'weight': mcCommonWeightNoMatch,
    'FilesPerJob': 10,
}
signals.append('DMscalar_Dilepton_top_tWChan_Mchi1_Mphi1000')
"""

###########################################
################## FAKE ###################
###########################################

samples['Fake'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW*(event%36 == 0)',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    # only this file is v3
    if ('2016E' in sd and 'MuonEG' in pd):
      files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd.replace('v1', 'v3'))

    else:
      files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)

    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))


###########################################
################## DATA ###################
###########################################

samples['DATA'] = {
  'name': [],
  'weight': 'METFilter_DATA*LepWPCut*(event%36 == 0)',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    # only this file is v3
    if ('2016E' in sd and 'MuonEG' in pd):
      files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd.replace('v1', 'v3'))

    else:
      files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
    
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))

