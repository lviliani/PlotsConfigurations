# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py 

# imported from samples.py:
# samples, treeBaseDir, mcProduction, mcSteps
# imported from cuts.py
# cuts
import os

if os.path.exists('HTXS_stage1_categories.py') :
  handle = open('HTXS_stage1_categories.py','r')
  exec(handle)
  handle.close()

if os.path.exists('thuNormFactors.py') :
  handle = open('thuNormFactors.py','r')
  exec(handle)
  handle.close()

if os.path.exists('thuVBFNormFactors.py') :
  handle = open('thuVBFNormFactors.py','r')
  exec(handle)
  handle.close()

sampleNames = []
for cat in HTXSStage1_1Categories:
  if 'GG2H_' in cat:
    sampleNames.append(cat.replace('GG2H','ggH_hww'))
    sampleNames.append(cat.replace('GG2H','ggH_htt'))
  elif 'QQ2HQQ_' in cat:
    sampleNames.append(cat.replace('QQ2HQQ','qqH_hww'))
    sampleNames.append(cat.replace('QQ2HQQ','qqH_htt'))
    sampleNames.append(cat.replace('QQ2HQQ','WH_had_hww'))
    sampleNames.append(cat.replace('QQ2HQQ','WH_had_htt'))
    sampleNames.append(cat.replace('QQ2HQQ','ZH_had_hww'))
    sampleNames.append(cat.replace('QQ2HQQ','ZH_had_htt'))
  elif 'QQ2HLNU_' in cat:
    sampleNames.append(cat.replace('QQ2HLNU','WH_lep_hww'))
    sampleNames.append(cat.replace('QQ2HLNU','WH_lep_htt'))
  elif 'QQ2HLL_' in cat:
    sampleNames.append(cat.replace('QQ2HLL','ZH_lep_hww'))
    sampleNames.append(cat.replace('QQ2HLL','ZH_lep_htt'))
  elif 'GG2HLL_' in cat:
    sampleNames.append(cat.replace('GG2HLL','ggZH_lep_hww'))
  elif 'TTH' in cat:
    sampleNames.append(cat.replace('TTH','ttH_hww'))
  elif 'BBH' in cat:
    sampleNames.append(cat.replace('BBH','bbH_hww'))


from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

try:
    mc_emb = [skey for skey in samples if skey != 'DATA' and skey != 'Dyveto' and not skey.startswith('Fake')]
    mc = [skey for skey in mc_emb if skey != 'Dyemb']
except NameError:
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''

from LatinoAnalysis.Tools.HiggsXSection import HiggsXSection
HiggsXS = HiggsXSection()

cuts0j = []
cuts1j = []

for k in cuts:
  for cat in cuts[k]['categories']:
    if '0j' in cat: cuts0j.append(k+'_'+cat)
    elif '1j' in cat: cuts1j.append(k+'_'+cat)

################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity
nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc if skey not in ['WW', 'top'])
}

nuisances['lumi_correlated'] = {
    'name': 'lumi_13TeV_correlated',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ['WW', 'top'])
}

nuisances['lumi_correlated_1718'] = {
    'name': 'lumi_13TeV_correlated_1718',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['WW', 'top'])
}


nuisances['fake_syst'] = {
    'name': 'CMS_fake_syst_2018',
    'type': 'lnN',
    'samples': {
        'Fake': '1.3'
    },
    'perRecoBin': True
}

nuisances['fake_ele'] = {
    'name': 'CMS_fake_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWEleUp', 'fakeWEleDown'],
    },
    'perRecoBin': True
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatEleUp', 'fakeWStatEleDown']
    },
    'perRecoBin': True
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWMuUp', 'fakeWMuDown'],
    },
    'perRecoBin': True
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    },
    'perRecoBin': True
}


##### B-tagger

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2018'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc_emb),
}

##### Electron Efficiency and energy scale

nuisances['eff_e_CR'] = {
    'name': 'CMS_eff_e_CR_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc_emb),
    'cuts': [cut for cut in cuts if '_CR_' in cut or 'top' in cut or 'dytt' in cut],
#    'perRecoBin': True
}


nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc_emb),
    'cuts': [cut for cut in cuts if not ('_CR_' in cut or 'top' in cut or 'dytt' in cut)],
#    'perRecoBin': True
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
    'AsLnN': '1'
}

if useEmbeddedDY:
  nuisances['electronpt_emb'] = {
    'name': 'CMS_scale_e_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp' : 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': {'Dyemb': ['1', '1']},
    'folderUp': treeBaseDir+'/Embedding2018_102X_nAODv7_Full2018v7/DATAl1loose2018v7__l2loose__l2tightOR2018v7__Embedding__EmbElepTup_suffix/',
    'folderDown': treeBaseDir+'/Embedding2018_102X_nAODv7_Full2018v7/DATAl1loose2018v7__l2loose__l2tightOR2018v7__Embedding__EmbElepTdo_suffix/',
    'AsLnN': '1'
  }


##### Muon Efficiency and energy scale

nuisances['eff_m_CR'] = {
    'name': 'CMS_eff_m_CR_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc_emb),
    'cuts': [cut for cut in cuts if '_CR_' in cut or 'top' in cut or 'dytt' in cut],
#    'perRecoBin': True
}


nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc_emb),
    'cuts': [cut for cut in cuts if not ('_CR_' in cut or 'top' in cut or 'dytt' in cut)],
#    'perRecoBin': True
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
    'AsLnN': '1'
}

if useEmbeddedDY:
  nuisances['muonpt_emb'] = {
    'name': 'CMS_scale_m_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp' : 'MupTup',
    'mapDown': 'MupTdo',
    'samples': {'Dyemb': ['1', '1']},
    'folderUp': treeBaseDir+'/Embedding2018_102X_nAODv7_Full2018v7/DATAl1loose2018v7__l2loose__l2tightOR2018v7__Embedding__EmbMupTup_suffix/',
    'folderDown': treeBaseDir+'/Embedding2018_102X_nAODv7_Full2018v7/DATAl1loose2018v7__l2loose__l2tightOR2018v7__Embedding__EmbMupTdo_suffix/',
    'AsLnN': '1'
  }


##### Jet energy scale
jes_systs = ['JESAbsolute','JESAbsolute_2018','JESBBEC1','JESBBEC1_2018','JESEC2','JESEC2_2018','JESFlavorQCD','JESHF','JESHF_2018','JESRelativeBal','JESRelativeSample_2018']
folderup = ""
folderdo = ""

for js in jes_systs:
  if 'Absolute' in js:
    folderup = makeMCDirectory('JESAbsoluteup_suffix')
    folderdo = makeMCDirectory('JESAbsolutedo_suffix')
  elif 'BBEC1' in js:
    folderup = makeMCDirectory('JESBBEC1up_suffix')
    folderdo = makeMCDirectory('JESBBEC1do_suffix')
  elif 'EC2' in js:
    folderup = makeMCDirectory('JESEC2up_suffix')
    folderdo = makeMCDirectory('JESEC2do_suffix')
  elif 'HF' in js:
    folderup = makeMCDirectory('JESHFup_suffix')
    folderdo = makeMCDirectory('JESHFdo_suffix')
  elif 'Relative' in js:
    folderup = makeMCDirectory('JESRelativeup_suffix')
    folderdo = makeMCDirectory('JESRelativedo_suffix')
  elif 'FlavorQCD' in js:
    folderup = makeMCDirectory('JESFlavorQCDup_suffix')
    folderdo = makeMCDirectory('JESFlavorQCDdo_suffix')

  nuisances[js] = {
      'name': 'CMS_scale_'+js,
      'kind': 'suffix',
      'type': 'shape',
      'mapUp': js+'up',
      'mapDown': js+'do',
      'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['VZ']),
      'folderUp': folderup,
      'folderDown': folderdo,
      'AsLnN': '1'
  }


##### Jet energy resolution
nuisances['JER'] = {
    'name': 'CMS_res_j_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'JERup',
    'mapDown': 'JERdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('JERup_suffix'),
    'folderDown': makeMCDirectory('JERdo_suffix'),
    'AsLnN': '1'
}

##### MET energy scale

nuisances['met'] = {
    'name': 'CMS_scale_met_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'METup',
    'mapDown': 'METdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('METup_suffix'),
    'folderDown': makeMCDirectory('METdo_suffix'),
    'AsLnN': '1'
}

##### Di-Tau vetoing for embedding
if useEmbeddedDY:
  if runDYveto:
    nuisances['embedveto']  = {
                    'name'  : 'CMS_embed_veto_2018',
                    'kind'  : 'weight',
                    'type'  : 'shape',
                    'samples'  : {
                       'Dyemb'    : ['1', '1'],
                       'Dyveto'   : ['0.1', '-0.1'],
                    }
             }
  else:
    # These hardcoded numbers have been obtained by running the full Dyveto (with runDYveto=True in samples.py) 
    # and computing the lnN uncertainty as variation of the up/down integral with respect to the nominal Dyemb integral
    unc_dict = {}
    unc_dict['hww2l2v_13TeV_of0j_pth0_10']      =   '1.03724'
    unc_dict['hww2l2v_13TeV_of0j_pth10_200']    =   '1.02891'
    unc_dict['hww2l2v_13TeV_of1j_pth0_60']      =   '1.01188'
    unc_dict['hww2l2v_13TeV_of1j_pth60_120']    =   '1.02647'
    unc_dict['hww2l2v_13TeV_of1j_pth120_200']   =   '1.01830'
    unc_dict['hww2l2v_13TeV_dytt_0j_pth0_10']   =   '1.00226'
    unc_dict['hww2l2v_13TeV_dytt_0j_pth10_200'] =   '1.00226'
    unc_dict['hww2l2v_13TeV_dytt_1j_pth0_60']   =   '1.00177'
    unc_dict['hww2l2v_13TeV_dytt_1j_pth60_120'] =   '1.00177'
    unc_dict['hww2l2v_13TeV_dytt_1j_pth120_200']=   '1.00177'
    unc_dict['hww2l2v_13TeV_top_0j_pth0_10']    =   '1.01190'
    unc_dict['hww2l2v_13TeV_top_0j_pth10_20']   =   '1.01190'
    unc_dict['hww2l2v_13TeV_top_1j_pth0_60']    =   '1.01777'
    unc_dict['hww2l2v_13TeV_top_1j_pth60_120']  =   '1.01777'
    unc_dict['hww2l2v_13TeV_top_1j_pth120_200'] =   '1.01777'
    unc_dict['hww2l2v_13TeV_ww_0j']             =   '1.05776'
    unc_dict['hww2l2v_13TeV_ww_1j']             =   '1.05914'

    for category,uncertainty in unc_dict.iteritems():
      nuisances['embedveto_'+category]  = {
                      'name'  : 'CMS_embed_veto_2018',
                      'type'  : 'lnN',
                      'samples'  : {
                         'Dyemb'    : uncertainty,
                         },
                       'cuts': [category],
                     }

##### Pileup

nuisances['PU'] = {
    'name': 'CMS_PU_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'DY': ['0.993259983266*(puWeightUp/puWeight)', '0.997656381501*(puWeightDown/puWeight)'],
        'top': ['1.00331969187*(puWeightUp/puWeight)', '0.999199609528*(puWeightDown/puWeight)'],
        'WW': ['1.0033022059*(puWeightUp/puWeight)', '0.997085330608*(puWeightDown/puWeight)'],
        'ggH_hww': ['1.0036768006*(puWeightUp/puWeight)', '0.995996570285*(puWeightDown/puWeight)'],
        'qqH_hww': ['1.00374694528*(puWeightUp/puWeight)', '0.995878596852*(puWeightDown/puWeight)'],
    },
    'AsLnN': '1',
}

### PU ID SF uncertainty
puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'CMS_PUID_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mc)
}


##### PS
nuisances['PS_ISR']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[2]', 'PSWeight[0]']) for skey in mc if skey not in ['Vg','VgS','WWewk']), #PSWeights are buggy for some samples, we add them back by hand below
}

nuisances['PS_FSR']  = {
    'name': 'PS_FSR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[3]', 'PSWeight[1]']) for skey in mc if skey not in ['Vg','VgS','WWewk']), #PSWeights are buggy for some samples, we add them back by hand below
}

## PS nuisances computed by hand as a function of nCleanGenJets using alternative samples (when available). Needed if nominal samples have buggy PSWeights
nuisances['PS_ISR_ForBuggySamples']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Vg'     : ['1.00227428567253*(nCleanGenJet==0) + 1.00572014989997*(nCleanGenJet==1) + 0.970824885256465*(nCleanGenJet==2) + 0.927346068071086*(nCleanGenJet>=3)', '0.996488506572636*(nCleanGenJet==0) + 0.993582795375765*(nCleanGenJet==1) + 1.03643678934568*(nCleanGenJet==2) + 1.09735277266955*(nCleanGenJet>=3)'],
        'VgS'    : ['1.0000536116408023*(nCleanGenJet==0) + 1.0100100693580492*(nCleanGenJet==1) + 0.959068359375*(nCleanGenJet==2) + 0.9117049260469496*(nCleanGenJet>=3)', '0.9999367833485968*(nCleanGenJet==0) + 0.9873682892005163*(nCleanGenJet==1) + 1.0492717737268518*(nCleanGenJet==2) + 1.1176958835210322*(nCleanGenJet>=3)'],
    },
}

nuisances['PS_FSR_ForBuggySamples']  = {
    'name': 'PS_FSR',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Vg'     : ['0.999935529935028*(nCleanGenJet==0) + 0.997948255568351*(nCleanGenJet==1) + 1.00561645493085*(nCleanGenJet==2) + 1.0212896960035*(nCleanGenJet>=3)', '1.00757702771109*(nCleanGenJet==0) + 1.00256681166083*(nCleanGenJet==1) + 0.93676371569867*(nCleanGenJet==2) + 0.956448336052435*(nCleanGenJet>=3)'],
        'VgS'    : ['0.9976593177227735*(nCleanGenJet==0) + 1.0016125187585532*(nCleanGenJet==1) + 1.0049344618055556*(nCleanGenJet==2) + 1.0195631514301164*(nCleanGenJet>=3)', '1.0026951855766457*(nCleanGenJet==0) + 1.0008132148661049*(nCleanGenJet==1) + 1.003949291087963*(nCleanGenJet==2) + 0.9708160910230832*(nCleanGenJet>=3)'],
    },
}

# An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# And we don't observe any dependency of UE variations on njet
nuisances['UE']  = {
                'name'  : 'UE_CP5',
                'skipCMS' : 1,
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mc), 
}

####### Generic "cross section uncertainties"

apply_on = {
    'top': [
        '(topGenPt * antitopGenPt <= 0.) * 1.0816 + (topGenPt * antitopGenPt > 0.)',
        '(topGenPt * antitopGenPt <= 0.) * 0.9184 + (topGenPt * antitopGenPt > 0.)'
    ]
}

nuisances['singleTopToTTbar'] = {
    'name': 'singleTopToTTbar',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': apply_on
}

nuisances['VgStar'] = {
    'name': 'CMS_hww_VgStarScale',
    'type': 'lnN',
    'samples': {
        'VgS_L': '1.25'
    }
}

if useWgFXFX:
#   nuisances['VgScale'] = {
#       'name': 'CMS_hww_VgScale',
#       'type': 'lnN',
#       'samples': {
#           'Vg': '1.06'
#       }
#   }

## Vg scale as a function of nGenJet

  nuisances['VgScale'] = {
      'name': 'CMS_hww_VgScale',
      'type': 'shape',
      'kind': 'weight',
      'samples': {
          'Vg': ['0.984 * (nCleanGenJet==0) + 1.015 * (nCleanGenJet==1) + 1.09 * ( nCleanGenJet>1)',
                 '1.014 * (nCleanGenJet==0) + 0.985 * (nCleanGenJet==1) + 0.93 * ( nCleanGenJet>1)']
      }
  }

nuisances['VZ'] = {
    'name': 'CMS_hww_VZScale',
    'type': 'lnN',
    'samples': {
        'VgS_H': '1.16'
    }
}

###### pdf uncertainties

# PDF eigenvariations for WW and top
for i in range(1,33):
  # LHEPdfWeight are PDF4LHC variations, while nominal is NNPDF.
  # LHEPdfWeight[i] reweights from NNPDF nominal to PDF4LHC member i
  # LHEPdfWeight[0] in particular reweights from NNPDF nominal to PDF4LHC nominal
  pdf_variations = ["LHEPdfWeight[%d]/LHEPdfWeight[0]" %i, "2. - LHEPdfWeight[%d]/LHEPdfWeight[0]" %i ]

  nuisances['pdf_WW_eigen'+str(i)]  = {
    'name'  : 'CMS_hww_pdf_WW_eigen'+str(i),
    'skipCMS' : 1,
    'kind'  : 'weight',
    'type'  : 'shape',
    'samples'  : {
      'WW'   : pdf_variations,
    },
  }
  nuisances['pdf_top_eigen'+str(i)]  = {
    'name'  : 'CMS_hww_pdf_top_eigen'+str(i),
    'skipCMS' : 1,
    'kind'  : 'weight',
    'type'  : 'shape',
    'samples'  : {
      'top'   : pdf_variations,
    },
  }

valuesggh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH','125.09','pdf','sm')
valuesggzh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','pdf','sm')
valuesbbh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','bbH','125.09','pdf','sm')

nuisances['pdf_Higgs_gg'] = {
    'name': 'pdf_Higgs_gg',
    'samples': {
        'ggH_htt': valuesggh,
        'bbH_hww': valuesbbh
    },
    'type': 'lnN',
}

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','pdf','sm')

nuisances['pdf_Higgs_ttH'] = {
    'name': 'pdf_Higgs_ttH',
    'samples': {
        'ttH_hww': values
    },
    'type': 'lnN',
}

valuesqqh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm')
valueswh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','pdf','sm')
valueszh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','pdf','sm')

nuisances['pdf_Higgs_qqbar'] = {
    'name': 'pdf_Higgs_qqbar',
    'type': 'lnN',
    'samples': {
        'qqH_htt': valuesqqh,
        'WH_htt': valueswh,
        'ZH_htt': valueszh
    },
}

#FIXME: check this 4%
nuisances['pdf_qqbar'] = {
    'name': 'pdf_qqbar',
    'type': 'lnN',
    'samples': {
        'Vg': '1.04',
        'VZ': '1.04',  # PDF: 0.0064 / 0.1427 = 0.0448493
        'VgS': '1.04', # PDF: 0.0064 / 0.1427 = 0.0448493
    },
}

nuisances['pdf_Higgs_gg_ACCEPT'] = {
    'name': 'pdf_Higgs_gg_ACCEPT',
    'samples': {
        'ggH_htt': '1.006',
        'bbH_hww': '1.006'
    },
    'type': 'lnN',
}

nuisances['pdf_gg_ACCEPT'] = {
    'name': 'pdf_gg_ACCEPT',
    'samples': {
        'ggWW': '1.006',
    },
    'type': 'lnN',
}

nuisances['pdf_Higgs_qqbar_ACCEPT'] = {
    'name': 'pdf_Higgs_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        'qqH_htt': '1.002',
        'WH_htt': '1.003',
        'ZH_htt': '1.002',
    },
}

nuisances['pdf_qqbar_ACCEPT'] = {
    'name': 'pdf_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        'VZ': '1.001',
    },
}

##### Renormalization & factorization scales



## Shape nuisance due to QCD scale variations for DY
# LHE scale variation weights (w_var / w_nominal)

## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']
topvars0j = []
topvars1j = []

## Factors computed to renormalize the top scale variations such that the integral is not changed in each RECO jet bin (we have rateParams for that)
topScaleNormFactors0j = {'LHEScaleWeight[3]': 1.0026322046882807, 'LHEScaleWeight[0]': 1.0761381504953040, 'LHEScaleWeight[1]': 1.0758902481739956, 'LHEScaleWeight[Length$(LHEScaleWeight)-1]': 0.9225780960271310, 'LHEScaleWeight[Length$(LHEScaleWeight)-4]': 1.0006689791003040, 'LHEScaleWeight[Length$(LHEScaleWeight)-2]': 0.9242759920995479}
topScaleNormFactors1j = {'LHEScaleWeight[3]': 1.0088973745933350, 'LHEScaleWeight[0]': 1.0858717477880675, 'LHEScaleWeight[1]': 1.0809970696561464, 'LHEScaleWeight[Length$(LHEScaleWeight)-1]': 0.9115155831354494, 'LHEScaleWeight[Length$(LHEScaleWeight)-4]': 0.9950909615738225, 'LHEScaleWeight[Length$(LHEScaleWeight)-2]': 0.9194241285459210}

topvars0j.append('LHEScaleWeight[0]/'+str(topScaleNormFactors0j['LHEScaleWeight[0]']))
topvars0j.append('LHEScaleWeight[Length$(LHEScaleWeight)-1]/'+str(topScaleNormFactors0j['LHEScaleWeight[Length$(LHEScaleWeight)-1]']))

topvars1j.append('LHEScaleWeight[0]/'+str(topScaleNormFactors1j['LHEScaleWeight[0]']))
topvars1j.append('LHEScaleWeight[Length$(LHEScaleWeight)-1]/'+str(topScaleNormFactors1j['LHEScaleWeight[Length$(LHEScaleWeight)-1]']))

# for var in variations:
#   topvars0j.append(var+'/'+str(topScaleNormFactors0j[var]))
#   topvars1j.append(var+'/'+str(topScaleNormFactors1j[var]))

## QCD scale nuisances for top are decorrelated for each RECO jet bin: the QCD scale is different for different jet multiplicities so it doesn't make sense to correlate them
nuisances['QCDscale_top_0j']  = {
    'name'  : 'QCDscale_top_0j',
    'skipCMS' : 1,
    'kind'  : 'weight',
    'type'  : 'shape',
    'cutspost' : lambda self, cuts: [cut for cut in cuts if '0j' in cut],
    'samples'  : {
       'top' : topvars0j,
    }
}

nuisances['QCDscale_top_1j']  = {
    'name'  : 'QCDscale_top_1j',
    'skipCMS' : 1,
    'kind'  : 'weight',
    'type'  : 'shape',
    'cutspost' : lambda self, cuts: [cut for cut in cuts if '1j' in cut],
    'samples'  : {
       'top' : topvars1j,
    }
}



## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']

nuisances['QCDscale_V'] = {
    'name': 'QCDscale_V',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {'DY': variations},
    'AsLnN': '1'
}

if useWgFXFX:
  nuisances['QCDscale_VV'] = {
      'name': 'QCDscale_VV',
      'kind': 'weight_envelope',
      'type': 'shape',
      'samples': {
          'VZ': variations,
      },
  }
else:
  nuisances['QCDscale_VV'] = {
      'name': 'QCDscale_VV',
      'kind': 'weight_envelope',
      'type': 'shape',
      'samples': {
          'Vg': variations,
          'VZ': variations,
          'VgS': variations
      },
  }


# ggww and interference
nuisances['QCDscale_ggVV'] = {
    'name': 'QCDscale_ggVV',
    'type': 'lnN',
    'samples': {
        'ggWW': '1.15',
    },
}

# NLL resummation variations
nuisances['WWresum0j']  = {
  'name'  : 'CMS_hww_WWresum_0j',
  'skipCMS' : 1,
  'kind'  : 'weight',
  'type'  : 'shape',
  'samples'  : {
     'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
   },
  'cutspost'  : lambda self, cuts: [cut for cut in cuts if '0j' in cut]
}

nuisances['WWqscale0j']  = {
   'name'  : 'CMS_hww_WWqscale_0j',
   'skipCMS' : 1,
   'kind'  : 'weight',
   'type'  : 'shape',
   'samples'  : {
      'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
    },
   'cutspost'  : lambda self, cuts: [cut for cut in cuts if '0j' in cut]
}

nuisances['WWresum1j']  = {
  'name'  : 'CMS_hww_WWresum_1j',
  'skipCMS' : 1,
  'kind'  : 'weight',
  'type'  : 'shape',
  'samples'  : {
     'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
   },
  'cutspost'  : lambda self, cuts: [cut for cut in cuts if '1j' in cut]
}

nuisances['WWqscale1j']  = {
   'name'  : 'CMS_hww_WWqscale_1j',
   'skipCMS' : 1,
   'kind'  : 'weight',
   'type'  : 'shape',
   'samples'  : {
      'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
    },
   'cutspost'  : lambda self, cuts: [cut for cut in cuts if '1j' in cut]
}

nuisances['EWKcorr_WW'] = {
    'name': 'CMS_hww_EWKcorr_WW',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'WW': ['1.', '1./ewknloW']
    },
    'symmetrize' : True,
}

# Uncertainty on SR/CR ratio
nuisances['CRSR_accept_DY'] = {
    'name': 'CMS_hww_CRSR_accept_DY',
    'type': 'lnN',
    'samples': {'DY': '1.02'},
    'cuts': [cut for cut in cuts if '_CR_' in cut],
    'cutspost': (lambda self, cuts: [cut for cut in cuts if '_DY_' in cut]),
}

# Uncertainty on SR/CR ratio
nuisances['CRSR_accept_top'] = {
    'name': 'CMS_hww_CRSR_accept_top',
    'type': 'lnN',
    'samples': {'top': '1.01'},
    'cuts': [cut for cut in cuts if '_CR_' in cut],
    'cutspost': (lambda self, cuts: [cut for cut in cuts if '_top_' in cut]),
}

# Theory uncertainty for ggH
#
#
#   THU_ggH_Mu, THU_ggH_Res, THU_ggH_Mig01, THU_ggH_Mig12, THU_ggH_VBF2j, THU_ggH_VBF3j, THU_ggH_PT60, THU_ggH_PT120, THU_ggH_qmtop
#
#   see https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsWG/SignalModelingTools

thus = [
    ('THU_ggH_Mu', 'ggH_mu_2'),
    ('THU_ggH_Res', 'ggH_res_2'),
    ('THU_ggH_Mig01', 'ggH_mig01_2'),
    ('THU_ggH_Mig12', 'ggH_mig12_2'),
    ('THU_ggH_VBF2j', 'ggH_VBF2j_2'),
    ('THU_ggH_VBF3j', 'ggH_VBF3j_2'),
    ('THU_ggH_PT60', 'ggH_pT60_2'),
    ('THU_ggH_PT120', 'ggH_pT120_2'),
    ('THU_ggH_qmtop', 'ggH_qmtop_2')
]

for name, vname in thus:
    updown = [vname, '2.-%s' % vname]
    
    nuisances[name] = {
        'name': name,
        'skipCMS': 1,
        'kind': 'weight',
        'type': 'shape',
        'samples': {
          'ggH_hww': updown,
          #'ggH_htt': updown
        }
    }
    for sname in sampleNames:
        if 'ggH_hww' in sname:
          if 'GT200' not in sname:
            normthu = globals()[name.replace("THU_","thuNormFactors_")][sname.replace('ggH_hww','GG2H')][0]
            nuisances[name]['samples'].update({sname : [vname+'/'+normthu,'2.-'+vname+'/'+normthu]})
        else:
            nuisances[name]['samples'].update({name : [vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_200_300'][0]
            ,'2.-'+vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_200_300'][0]]})
            nuisances[name]['samples'].update({name : [vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_300_450'][0]
            ,'2.-'+vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_300_450'][0]]})
            nuisances[name]['samples'].update({name : [vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_450_650'][0]
            ,'2.-'+vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_450_650'][0]]})
            nuisances[name]['samples'].update({name : [vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_GT650'][0]
            ,'2.-'+vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_GT650'][0]]})

# Theory uncertainty for qqH 
#
#
#   see https://gitlab.cern.ch/LHCHIGGSXS/LHCHXSWG2/STXS/VBF-Uncertainties/-/blob/master/qq2Hqq_uncert_scheme.cpp

thusQQH = [
  ("THU_qqH_PTH200","qqH_PTH200"),
  ("THU_qqH_Mjj60","qqH_Mjj60"),
  ("THU_qqH_Mjj120","qqH_Mjj120"),
  ("THU_qqH_Mjj350","qqH_Mjj350"),
  ("THU_qqH_Mjj700","qqH_Mjj700"),
  ("THU_qqH_Mjj1000","qqH_Mjj1000"),
  ("THU_qqH_Mjj1500","qqH_Mjj1500"),
  ("THU_qqH_PTH25","qqH_PTH25"),
  ("THU_qqH_JET01","qqH_JET01"),
  ("THU_qqH_EWK","qqH_EWK"),
]

for name, vname in thusQQH:
    updown = [vname, '2.-%s' % vname]
    
    nuisances[name] = {
        'name': name,
        'skipCMS': 1,
        'kind': 'weight',
        'type': 'shape',
        'samples': {
          'qqH_hww': updown,
        }
    }
    for sname in sampleNames:
        if 'qqH_hww' in sname:
          normthu = globals()[name.replace("THU_","thuNormFactors_")][sname.replace('qqH_hww','QQ2HQQ')][0]
          nuisances[name]['samples'].update({sname : [vname+'/'+normthu,'2.-'+vname+'/'+normthu]})
    print nuisances[name]


### QCD STXS accept                                                                                                                           
nuisances['ggH_scale_0jet'] = {
               'name'  : 'ggH_scale_0jet',
               'samples'  : {
                   'ggH_hww_0J_PTH_0_10' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_0J_PTH_0_10'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_0J_PTH_0_10'][1]],
                   'ggH_hww_0J_PTH_GT10' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_0J_PTH_GT10'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_0J_PTH_GT10'][1]],
                  },
               'type'  : 'shape',
               'kind'  : 'weight',
              }

nuisances['ggH_scale_1jet_lowpt'] = {
               'name'  : 'ggH_scale_1jet_lowpt',
               'samples'  : {
                   'ggH_hww_1J_PTH_0_60' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_1J_PTH_0_60'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_1J_PTH_0_60'][1]],
                   'ggH_hww_1J_PTH_60_120' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_1J_PTH_60_120'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_1J_PTH_60_120'][1]],
                   'ggH_hww_1J_PTH_120_200' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_1J_PTH_120_200'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_1J_PTH_120_200'][1]],
                  },
               'type'  : 'shape',
               'kind'  : 'weight',
              }
nuisances['ggH_scale_2jet_lowpt'] = {
               'name'  : 'ggH_scale_2jet_lowpt',
               'samples'  : {
                   'ggH_hww_GE2J_MJJ_0_350_PTH_0_60' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_0_60'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_0_60'][1]],
                   'ggH_hww_GE2J_MJJ_0_350_PTH_60_120' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_60_120'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_60_120'][1]],
                   'ggH_hww_GE2J_MJJ_0_350_PTH_120_200' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_120_200'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_120_200'][1]],
                  },
               'type'  : 'shape',
               'kind'  : 'weight',
              }

nuisances['ggH_scale_highpt'] = {
               'name'  : 'ggH_scale_highpt',
               'samples'  : {
                   'ggH_hww_PTH_200_300' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_PTH_200_300'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_PTH_200_300'][1]],
                   'ggH_hww_PTH_300_450' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_PTH_300_450'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_PTH_300_450'][1]],
                  },
               'type'  : 'shape',
               'kind'  : 'weight',
              }

nuisances['ggH_scale_very_highpt'] = {
               'name'  : 'ggH_scale_very_highpt',
               'samples'  : {
                   'ggH_hww_PTH_450_650' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_PTH_450_650'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_PTH_450_650'][1]],
                   'ggH_hww_PTH_GT650' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_PTH_GT650'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_PTH_GT650'][1]],
                  },
               'type'  : 'shape',
               'kind'  : 'weight',
              }

nuisances['ggH_scale_vbf'] = {
               'name'  : 'ggH_scale_vbf',
               'samples'  : {
                   'ggH_hww_GE2J_MJJ_350_700_PTHJJ_0_25' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_350_700_PTHJJ_0_25'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_350_700_PTHJJ_0_25'][1]],
                   'ggH_hww_GE2J_MJJ_350_700_PTHJJ_GT25' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_350_700_PTHJJ_GT25'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_350_700_PTHJJ_GT25'][1]],
                   'ggH_hww_GE2J_MJJ_GT700_PTHJJ_0_25' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_GT700_PTHJJ_0_25'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_GT700_PTHJJ_0_25'][1]],
                   'ggH_hww_GE2J_MJJ_GT700_PTHJJ_GT25' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_GT700_PTHJJ_GT25'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_GT700_PTHJJ_GT25'][1]],
                  },
               'type'  : 'shape',
               'kind'  : 'weight',
              }

nuisances['vbf_scale_0jet'] = {
               'name'  : 'vbf_scale_0jet',
               'samples'  : {
                   'qqH_hww_0J' : ['LHEScaleWeight[8]/'+QCDScaleFactors['QQ2HQQ_0J'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['QQ2HQQ_0J'][1]],
                  },
               'type'  : 'shape',
               'kind'  : 'weight',
              }

nuisances['vbf_scale_1jet'] = {
               'name'  : 'vbf_scale_1jet',
               'samples'  : {
                   'qqH_hww_1J' : ['LHEScaleWeight[8]/'+QCDScaleFactors['QQ2HQQ_1J'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['QQ2HQQ_1J'][1]],
                  },
               'type'  : 'shape',
               'kind'  : 'weight',
              }

nuisances['vbf_scale_lowmjj'] = {
               'name'  : 'vbf_scale_lowmjj',
               'samples'  : {
                    'qqH_hww_MJJ_0_60' : ['LHEScaleWeight[8]/'+QCDScaleFactors['QQ2HQQ_MJJ_0_60'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['QQ2HQQ_MJJ_0_60'][1]],
                    'qqH_hww_MJJ_60_120' : ['LHEScaleWeight[8]/'+QCDScaleFactors['QQ2HQQ_MJJ_60_120'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['QQ2HQQ_MJJ_60_120'][1]],
                    'qqH_hww_MJJ_120_350' : ['LHEScaleWeight[8]/'+QCDScaleFactors['QQ2HQQ_MJJ_120_350'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['QQ2HQQ_MJJ_120_350'][1]],
                  },
               'type'  : 'shape',
               'kind'  : 'weight',
              }

nuisances['vbf_scale_highmjj_lowpt'] = {
               'name'  : 'vbf_scale_highmjj_lowpt',
               'samples'  : {
                    'qqH_hww_MJJ_350_700_PTHJJ_0_25' : ['LHEScaleWeight[8]/'+QCDScaleFactors['QQ2HQQ_MJJ_350_700_PTHJJ_0_25'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['QQ2HQQ_MJJ_350_700_PTHJJ_0_25'][1]],
                    'qqH_hww_MJJ_350_700_PTHJJ_GT25' : ['LHEScaleWeight[8]/'+QCDScaleFactors['QQ2HQQ_MJJ_350_700_PTHJJ_GT25'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['QQ2HQQ_MJJ_350_700_PTHJJ_GT25'][1]],
                    'qqH_hww_MJJ_GT700_PTHJJ_0_25' : ['LHEScaleWeight[8]/'+QCDScaleFactors['QQ2HQQ_MJJ_GT700_PTHJJ_0_25'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['QQ2HQQ_MJJ_GT700_PTHJJ_0_25'][1]],
                    'qqH_hww_MJJ_GT700_PTHJJ_GT25' : ['LHEScaleWeight[8]/'+QCDScaleFactors['QQ2HQQ_MJJ_GT700_PTHJJ_GT25'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['QQ2HQQ_MJJ_GT700_PTHJJ_GT25'][1]],
                  },
               'type'  : 'shape',
               'kind'  : 'weight',
              }

nuisances['vbf_scale_highmjj_highpt'] = {
               'name'  : 'vbf_scale_highmjj_highpt',
               'samples'  : {
                    'qqH_hww_MJJ_GT350_PTH_GT200' : ['LHEScaleWeight[8]/'+QCDScaleFactors['QQ2HQQ_MJJ_GT350_PTH_GT200'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['QQ2HQQ_MJJ_GT350_PTH_GT200'][1]],
                  },
               'type'  : 'shape',
               'kind'  : 'weight',
              }



#### QCD scale uncertainties for Higgs signals other than ggH

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm')

nuisances['QCDscale_qqH'] = {
    'name': 'QCDscale_qqH', 
    'samples': {
        'qqH_htt': values
    },
    'type': 'lnN'
}

valueswh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm')
valueszh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm')

nuisances['QCDscale_VH'] = {
    'name': 'QCDscale_VH', 
    'samples': {
        'WH_htt': valueswh,
        'ZH_htt': valueszh
    },
    'type': 'lnN',
}

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','scale','sm')

nuisances['QCDscale_ttH'] = {
    'name': 'QCDscale_ttH',
    'samples': {
        'ttH_hww': values
    },
    'type': 'lnN',
}

nuisances['QCDscale_WWewk'] = {
    'name': 'QCDscale_WWewk',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'WWewk': ['LHEScaleWeight[0]', 'LHEScaleWeight[2]']
    }
}

nuisances['QCDscale_qqbar_ACCEPT'] = {
    'name': 'QCDscale_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        'qqH_htt': '1.003',
        'WH_htt': '1.010',
        'ZH_htt': '1.015',
        #'VZ': '1.004',
    }
}

nuisances['QCDscale_gg_ACCEPT'] = {
    'name': 'QCDscale_gg_ACCEPT',
    'samples': {
        'ggH_htt': '1.012',
        'ggWW': '1.012',
    },
    'type': 'lnN',
}

## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '0',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}

#rate parameters
cutdict = {}
tags = ['0j_pth0_10','0j_pth10_200','1j_pth0_60','1j_pth60_120','1j_pth120_200']
for tag in tags: cutdict[tag] = []

for k in cuts:
  for cat in cuts[k]['categories']:
    for tag in tags:
       if tag in cat: cutdict[tag].append(k+'_'+cat)

for tag in tags:

  nuisances['DYembnorm'+tag]  = {
                 'name'  : 'CMS_hww_DYttnorm'+tag,
                 'samples'  : {
                     'Dyemb' : '1.00',
                     },
                 'type'  : 'rateParam',
                 'cuts'  : cutdict[tag]
                }

  nuisances['WWnorm'+tag]  = {
                 'name'  : 'CMS_hww_WWnorm'+tag,
                 'samples'  : {
                     'WW' : '1.00',
                     },
                 'type'  : 'rateParam',
                 'cuts'  : cutdict[tag]
                }

  nuisances['ggWWnorm'+tag]  = {
                 'name'  : 'CMS_hww_WWnorm'+tag,
                 'samples'  : {
                     'ggWW' : '1.00',
                     },
                 'type'  : 'rateParam',
                 'cuts'  : cutdict[tag]
                }

  nuisances['Topnorm'+tag]  = {
                 'name'  : 'CMS_hww_Topnorm'+tag,
                 'samples'  : {
                     'top' : '1.00',
                     },
                 'type'  : 'rateParam',
                 'cuts'  : cutdict[tag]
                }


for n in nuisances.values():
    n['skipCMS'] = 1

print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))
