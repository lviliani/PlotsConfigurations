# variables

#variables = {}
    


variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }

variables['pt1']  = {   'name': 'Lepton_pt[0]',
                        'range' : ([0,5,10,15,20,25,30,35,40,45,50,70,100],),#(20,20,100),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 0
                        }
variables['pt2']  = {   'name': 'Lepton_pt[1]',
                        'range' : ([0,5,10,15,20,25,30,35,40,60,100],),#(20,20,100),
                        'xaxis' : 'p_{T} 2nd lep',
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

variables['njets']  = { 'name': 'Sum$(CleanJet_pt>30)',
                        'range' : (5,0,5),
                        'xaxis' : 'Number of jets',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['drll']  = { 'name': 'drll',
                        'range' : ([0,0.25,0.5,1.,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0],),#(10,0,5),
                        'xaxis' : '#Delta R_{ll}',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['dphill']  = { 'name': 'dphill',
                        'range' : (10,0,3),
                        'xaxis' : '#Delta #phi_{ll}',
                        'fold' : 3   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }

variables['classvbf'] = {'name': 'vbfdnn',
                        'range' : (10,0,1),
                        'xaxis' : 'DNN discriminant vbf',
                        'fold'  : 3,
}

variables['mll'] = {'name': 'mll',
                        'range' : ([12,25,35,40,45,50,55,70,90,210],),
                        'xaxis' : 'mll',
                        'fold'  : 3,
}


variables['mth'] = {'name': 'mth',
                        'range' : ([60,80,90,100,110,120,130,150,200],),
                        'xaxis' : 'mth',
                        'fold'  : 3,
}
