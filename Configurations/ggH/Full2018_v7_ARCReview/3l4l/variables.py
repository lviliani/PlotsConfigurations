# variables

#variables = {}
    


variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }

variables['pt1']  = {   'name': 'Lepton_pt[0]',
                        'range' : (20,20,100),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 0
                        }
'''
variables['pt1_singleEl']  = {   'name': 'Lepton_pt[0]*TriggerEffWeight_sngEl',
                        'range' : (20,20,100),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 0
                        }

variables['pt1_singleMu']  = {   'name': 'Lepton_pt[0]*TriggerEffWeight_sngMu',
                        'range' : (20,20,100),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 0
                        }

variables['pt1_ElMu']  = {   'name': 'Lepton_pt[0]*TriggerEffWeight_ElMu',
                        'range' : (20,20,100),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 0
                        }

'''
variables['pt2']  = {   'name': 'Lepton_pt[1]',
                        'range' : (20,10,100),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 0
                        }

variables['pt3']  = {   'name': 'Lepton_pt[2]',
                        'range' : (20,10,100),
                        'xaxis' : 'p_{T} 3rd lep',
                        'fold'  : 0
                        }



variables['eta1']  = {  'name': 'Lepton_eta[0]',
                        'range' : (20,-3,3),
                        'xaxis' : '#eta 1st lep',
                        'fold'  : 3
                        }

variables['eta2']  = {  'name': 'Lepton_eta[1]',
                        'range' : (20,-3,3),
                        'xaxis' : '#eta 2nd lep',
                        'fold'  : 3
                        }

variables['eta3']  = {  'name': 'Lepton_eta[2]',
                        'range' : (20,-3,3),
                        'xaxis' : '#eta 3rd lep',
                        'fold'  : 3
                        }

