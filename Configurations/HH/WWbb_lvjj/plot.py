# plot configuration



# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#




#groupPlot['HH']  = {  
#                 'nameHR' : 'HH',
#                 'isSignal' : 1,
#         0        'color': 861,   
#                 'samples'  : ['HH']
#              }

groupPlot['Wjets']  = {
                        'nameHR' : 'W+Jets',
                        'isSignal' : 0,
                        'color': 620,  
                        'samples'  : ['Wjets']
                        }

groupPlot['TTToSemilepton']  = {    
				'nameHR' : 'TTToSemilepton',
				'isSignal' : 0,
				'color' : 860,
				'samples' : ['TT']
                		 }	


groupPlot['TTWJetsToLNu'] = {
				'nameHR' : 'TTWJetsToLNu',
				'isSignal' : 0,
				'color' : 617,
				'samples' : ['TTW']
				}

groupPlot['WZTo1L1Nu2Q'] = {
                                'nameHR' : 'WZTo1L1Nu2Q',
                                'isSignal' : 0,
                                'color' : 400,
                                'samples' : ['WZTo1L1Nu2Q']
                                }

groupPlot['WZTo1L3Nu'] = {
                                'nameHR' : 'WZTo1L3Nu',
                                'isSignal' : 0,
                                'color' : 632,
                                'samples' : ['WZTo1L3Nu']
                                }

groupPlot['WWW']  = {
                        'nameHR' : 'WWW',
                        'isSignal' : 0,
                        'color': 850,
                        'samples'  : ['WWW']
                        }



groupPlot['WWZ']  = {
                        'nameHR' : 'WWZ',
                        'isSignal' : 0,
                        'color': 410,
                        'samples'  : ['WWZ']
                        }


#groupPlot['top']  = {  
                  #'nameHR' : 'tW and t#bart',
                  #'isSignal' : 0,
                  #'color': 400, #  kYellow
                  #'samples'  : ['top']
              #}

#groupPlot['WW']  = {  
                  #'nameHR' : 'WW',
                  #'isSignal' : 0,
                  #'color': 851, # kAzure -9 
                  #'samples'  : ['WW', 'ggWW']
              #}

#groupPlot['VVV']  = {  
                  #'nameHR' : 'VVV',
                  #'isSignal' : 0,
                  #'color': 857, # kAzure -3  
                  #'samples'  : ['VVV']
              #}


#groupPlot['VZ']  = {  
                  #'nameHR' : "VZ/#gamma*/#gamma",
                  #'isSignal' : 0,
                  #'color'    : 617,   # kViolet + 1  
                  #'samples'  : ['VZ', 'Vg', 'Wg', 'VgS', 'WZ', 'ZZ','Zg']
              #}


#groupPlot['DY']  = {  
                  #'nameHR' : "DY",
                  #'isSignal' : 0,
                  #'color': 418,  #  kGreen+2
                  ##'samples'  : ['DY1', 'DY2']
                  #'samples'  : ['DY']
              #}


#groupPlot['Higgs']  = {  
                  #'nameHR' : 'Higgs',
                  #'isSignal' : 1,
                  #'color': 632, # kRed 
                  #'samples'  : ['H_htt', 'H_hww', 'ZH_hww', 'ggZH_hww', 'WH_hww', 'qqH_hww', 'ggH_hww','bbH_hww']
              #}






#plot = {}

# keys here must match keys in samples.py    
#                    
#plot['HH']  = {  
#                  'color': 861,    
#                  'isSignal' : 1,
#                  'isData'   : 0, 
#                  'scale'    : 1.   ,
#              }

plot['Wjets']  = {
                  'color': 620,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }


plot['TT']  = {
                  'color': 860,    
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }



plot['TTW']  = {
                  'color': 617,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }

plot['WZTo1L1Nu2Q']  = {
                  'color': 400,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }

plot['WZTo1L3Nu']  = {
	          'color': 632,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }

plot['WWW']  = {
                  'color': 850,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }

plot['WWZ']  = {
                  'color': 410,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }

#legend['lumi'] = 'L = 6.3/fb'
legend['lumi'] = 'L = 35.9/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'




