groupPlot['Higgs'] = {
    'nameHR' : "SM Higgs",
    'isSignal' : 0,
    'color': 632+3, #kRed +3
    'samples'  : ['Higgs']
}

groupPlot['multiB'] = {
    'nameHR' : 'multiB',
    'isSignal' : 0,
    #'isSignal' : 1,
    'color': 857, # kAzure -3  
    #'samples'  : ['WW', 'WWewk', 'ggWW', 'VBF-V', 'WZqcd', 'WZewk', 'ZZ', 'VVV', 'Vg', 'VgS_L', 'VgS_H', 'ggH_hww', 'qqH_hww', 'ZH_hww', 'WH_hww', 'ttH_hww', 'ggH_htt', 'ZH_htt']
    #'samples'  : ['WW', 'WWewk', 'ggWW', 'WZqcd', 'WZewk', 'ZZ', 'VVV', 'Vg', 'VgS_L', 'VgS_H', 'ggH_hww', 'qqH_hww', 'ZH_hww', 'WH_hww', 'ttH_hww', 'ggH_htt', 'ZH_htt'] #, 'VBF-V'
    #'samples'  : ['WW', 'WWewk', 'ggWW', 'WZqcd', 'WZewk', 'ZZ', 'VVV', 'Vg', 'VgS_L', 'VgS_H', 'Higgs'] #, 'VBF-V'
    'samples'  : ['WW', 'WWewk', 'ggWW', 'WZqcd', 'WZewk', 'ZZ', 'VVV', 'Vg', 'VgS_L', 'VgS_H'] #, 'VBF-V'
}

groupPlot['DY'] = {
    'nameHR' : "DY",
    'isSignal' : 0,
    'color': 418,    # kGreen+2
    'samples'  : ['DY']
    #'samples'  : ['DY', 'DYlow']
}
#groupPlot['DY'] = {
#    'nameHR' : "DY",
#    'isSignal' : 0,
#    'color': 418,    # kGreen+2
#    'samples'  : ['DY']
#}
#
#groupPlot['DYlow'] = {
#    'nameHR' : "DYlow",
#    'isSignal' : 0,
#    'color': 416,    # kGreen+2
#    'samples'  : ['DYlow']
#}

groupPlot['FAKE'] = {
    'nameHR' : "Fake",
    'isSignal' : 0,
    'color'    : 617,   # kViolet + 1
    'samples'  : ['FAKE']
}


groupPlot['top'] = {
    'nameHR' : 'tW and t#bar{t}',
    'isSignal' : 0,
    'color': 400,   # kYellow
    #'samples'  : ['ttop', 'stop'],
    #'scale'    : 1.11,
    'samples'  : ['top']
}
#groupPlot['ttop'] = {
#    'nameHR' : 't#bar{t}',
#    'isSignal' : 0,
#    'color': 400,   # kYellow
#    'samples'  : ['ttop']
#}
#groupPlot['stop'] = {
#    'nameHR' : 'single t',
#    'isSignal' : 0,
#    'color': 401,   # kYellow
#    'samples'  : ['stop']
#}


groupPlot['Wjets'] = {
    'nameHR' : "W+jets",
    'isSignal' : 0,
    'color': 921,      # kGray + 1
    'samples'  : ['Wjets']
}

#groupPlot['WW'] = {
#    'nameHR' : 'WW',
#    'isSignal' : 0,
#    'color': 851, # kAzure -9 
#    'samples'  : ['WW', 'WWewk', 'qqWWqq', 'WW2J'] #, 'ggWW']
#}
#
#groupPlot['Vg'] = {
#    'nameHR' : "V#gamma",
#    'isSignal' : 0,
#    'color'    : 800,  #810,   # kOrange + 10
#    'samples'  : ['Vg']
#}
#
#groupPlot['VgS'] = {
#    'nameHR' : "V#gamma*",
#    'isSignal' : 0,
#    'color'    : 409,   # kGreen - 9
#    'samples'  : ['VgS_L', 'VgS_H']
#}
#
#groupPlot['VZ'] = {
#    'nameHR' : "VZ",
#    'isSignal' : 0,
#    'color'    : 617,   # kViolet + 1  
#    'samples'  : ['VZ']
#}
#
#groupPlot['VVV'] = {
#    'nameHR' : 'VVV',
#    'isSignal' : 0,
#    'color': 857, # kAzure -3  
#    'samples'  : ['VVV']
#}

#groupPlot['multiB'] = {
#    'nameHR' : 'multiB',
#    'isSignal' : 0,
#    'color': 857, # kAzure -3  
#    #'samples'  : ['VVV', 'WW', 'WWewk', 'qqWWqq', 'WW2J', 'Vg', 'VgS_L', 'VgS_H', 'VZ']
#    'samples'  : ['VVV', 'WW', 'WWewk', 'ggWW', 'Vg', 'VgS_L', 'VgS_H', 'VZ', 'ggH_hww', 'qqH_hww', 'ZH_hww', 'WH_hww', 'ttH_hww', 'ggH_htt', 'ZH_htt', 'VBF-V']
#}




#groupPlot['Higgs'] = {
#    'nameHR' : 'Higgs',
#    'isSignal' : 0,
#    'color': 632, # kRed 
#    'samples': ['ggH_hww', 'qqH_hww', 'ZH_hww', 'WH_hww', 'ttH_hww', 'ggH_htt', 'ZH_htt'] #, 'ggZH_hww'] #, 'ggZH_htt'] #, 'WH_htt'] 
#}

### SIGNAL
if os.path.exists(signal_file) :
    handle = open(signal_file,'r')
    exec(handle)
    handle.close()
else:
    raise IOError('FILE NOT FOUND: '+signal_file+'does not exist.')

#mhs_list = ['160', '180', '200']
#mx_list = ['100', '150', '200']
#mZp_list = ['195', '200', '295', '300', '400', '500', '800', '1000', '1200', '1500']
#
#models = []
#for mhs in mhs_list:
#    for mx in mx_list:
#        for mZp in mZp_list:
#            mp = 'mhs_'+mhs+'_mx_'+mx+'_mZp_'+mZp
for mp in signal:
    #if not 'mA_400' in mp: continue
    mpo = mp.replace('darkHiggs_', '')
    mhs = mpo.split('_')[1] 
    mx  = mpo.split('_')[3] 
    mZp = mpo.split('_')[5] 
    #if not 'mA_400' in mp: continue
    #if not mhs == '160' and not mx == '100' in mp: continue
    if not mhs == '160': continue 
    if not mx == '100' : continue
    if not mZp in ['500']: continue
    groupPlot[mp] = {
    'nameHR'   : signal[mp]['plot_name'],
#    'isSignal' : 2,
    'isSignal' : 1,
    'color'    : signal[mp]['color'],   # kViolet + 1
    'samples'  : [mp],
    #'scale'    : 100000,
    }

#groupPlot['DATA'] = {


#plot = {}

# keys here must match keys in samples.py
#
plot['DY']  = {
    'color': 418,    # kGreen+2
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0,
}

#plot['DYlow']  = {
#    'color': 416,    # kGreen+2
#    'isSignal' : 0,
#    'isData'   : 0,
#    'scale'    : 1.0,
#}

plot['top'] = {
    'nameHR' : 'tW and t#bar{t}',
    'color': 400,   # kYellow
    'isSignal' : 0,
    'isData'   : 0,
    #'scale'    : 1.0,
    'scale'    : 1.02,
}


plot['WW']  = {
    'color': 851, # kAzure -9
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
}

plot['ggWW']  = {
    'color': 850, # kAzure -10
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}

plot['WWewk']  = {
    'color': 851, # kAzure -9
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
}

#plot['qqWWqq']  = {
#    'color': 852, # kAzure -8
#    'isSignal' : 0,
#    'isData'   : 0,
#    'scale'    : 1.0
#}
#
#plot['WW2J']  = {
#    'color': 852, # kAzure -8
#    'isSignal' : 0,
#    'isData'   : 0,
#    'scale'    : 1.0
#}

plot['Vg']  = {
    'color': 859, # kAzure -1
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}

plot['VgS_H'] = {
    'color'    : 617,   # kViolet + 1
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}

plot['VgS_L'] = {
    'color'    : 617,   # kViolet + 1
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}

#plot['VBF-V']  = {
#    'color': 859, # kAzure -2
#    'isSignal' : 0,
#    'isData'   : 0,
#    'scale'    : 1.0
#}

plot['WZqcd']  = {
    'color': 858, # kAzure -2
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}
plot['WZewk']  = {
    'color': 861, # kAzure -2
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}

plot['ZZ']  = {
    'color': 860, # kAzure -2
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}

plot['VVV']  = {
    'color': 857, # kAzure -3
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}

plot['Wjets']  = {
    'color': 856, # kAzure -4
    'isSignal' : 0,
    'isData'   : 0,
    #'scale'    : 1.0
    'scale'    : 1.02
}

plot['FAKE']  = {
    'color': 855, # kAzure -5
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1.0
}


# HWW
plot['Higgs'] = {
    'nameHR' : 'SM Higgs',
    'color': 632+3, # kRed+3
    'isSignal' : 0,
    'isData'   : 0,
    'scale'    : 1    #
}

##plot['H_hww'] = {
##                  'nameHR' : 'Hww',
##                  'color': 632, # kRed
##                  'isSignal' : 1,
##                  'isData'   : 0,
##                  'scale'    : 1    #
##                  }
#
#plot['ZH_hww'] = {
#    'nameHR' : 'ZH',
#    'color': 632+3, # kRed+3
#    'isSignal' : 0,
#    'isData'   : 0,
#    'scale'    : 1    #
#}
#
## plot['ggZH_hww'] = {
##     'nameHR' : 'ggZH',
##     'color': 632+4, # kRed+4
##     'isSignal' : 0,
##     'isData'   : 0,
##     'scale'    : 1    #
## }
#
#plot['WH_hww'] = {
#    'nameHR' : 'WH',
#    'color': 632+2, # kRed+2
#    'isSignal' : 0,
#    'isData'   : 0,
#    'scale'    : 1    #
#}
#
#
#plot['qqH_hww'] = {
#    'nameHR' : 'qqH',
#    'color': 632+1, # kRed+1
#    'isSignal' : 0,
#    'isData'   : 0,
#    'scale'    : 1    #
#}
#
#
#plot['ggH_hww'] = {
#    'nameHR' : 'ggH',
#    'color': 632, # kRed
#    'isSignal' : 0,
#    'isData'   : 0,
#    'scale'    : 1    #
#}
#
#plot['ttH_hww'] = {
#    'nameHR' : 'ttH',
#    'color': 632+6, # kRed+6
#    'isSignal' : 0,
#    'isData'   : 0,
#    'scale'    : 1    #
#}
#
#plot['ggH_htt']  = {
#    'color': 428,    # kGreen+12
#    'isSignal' : 0,
#    'isData'   : 0,
#    'scale'    : 1.0,
#}
#plot['qqH_htt']  = {
#    'color': 428,    # kGreen+12
#    'isSignal' : 0,
#    'isData'   : 0,
#    'scale'    : 1.0,
#}
#plot['ZH_htt']  = {
#    'color': 428,    # kGreen+12
#    'isSignal' : 0,
#    'isData'   : 0,
#    'scale'    : 1.0,
#}
## plot['WH_htt']  = {
##     'color': 428,    # kGreen+12
##     'isSignal' : 0,
##     'isData'   : 0,
##     'scale'    : 1.0,
## }

### Signal
for mp in signal:
    mpo = mp.replace('darkHiggs_', '')
    mhs = mpo.split('_')[1] 
    mx  = mpo.split('_')[3] 
    mZp = mpo.split('_')[5] 
    #if not 'mA_400' in mp: continue
    if not mhs == '160': continue 
    if not mx == '100' : continue
    if not mZp in ['500']: continue
    plot[mp] = {
    'nameHR'   : signal[mp]['plot_name'],
    'isSignal' : 2,
    'isData'   : 0,
    'color'    : signal[mp]['color'],   # kViolet + 1
    'samples'  : [mp],
    #'scale'    : 100000,
    }

## data

plot['DATA']  = {
                  'nameHR' : 'Data',
                  'color': 1 ,
                  'isSignal' : 0,
                  'isData'   : 1 ,
                  'isBlind'  : 0
              }




# additional options
legend['lumi'] = 'L = 35.9/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'





# samples['ggZH_hww'] = {
# samples['ggZH_htt'] = {
# samples['WH_htt'] = {
