# variables

#variables = {}
    


variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
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
