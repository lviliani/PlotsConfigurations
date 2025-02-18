#RAndKff  = {}
RAndKff['DYmva0p80'] = {
    'RFile'   : 'rootFile/plots_DYESTIM_2017_v7_Zpeak.root' ,
    'KffFile' : '../rootFile/plots_DYESTIM_ggH_SF_2017_v7_DYMVA080.root' ,
    'Regions' : { 
        '0jee' : {
            'kNum' : '0j_ee_in' ,
            'kDen' : '0j_mm_in' ,
            'RNum' : '0j_ee_out' ,
            'RDen' : '0j_ee_in' ,
        } ,
        '0jmm' : {
            'kNum' : '0j_mm_in' ,
            'kDen' : '0j_ee_in' ,
            'RNum' : '0j_mm_out' ,
            'RDen' : '0j_mm_in' ,
        } ,
        '1jee' : {
            'kNum' : '1j_ee_in' ,
            'kDen' : '1j_mm_in' ,
            'RNum' : '1j_ee_out' ,
            'RDen' : '1j_ee_in' ,
        } ,
        '1jmm' : {
            'kNum' : '1j_mm_in' ,
            'kDen' : '1j_ee_in' ,
            'RNum' : '1j_mm_out' ,
            'RDen' : '1j_mm_in' ,
        } ,
        '2jee' : {
            'kNum' : '2j_ee_in' ,
            'kDen' : '2j_mm_in' ,
            'RNum' : '2j_ee_out' ,
            'RDen' : '2j_ee_in' ,
        } ,
        '2jmm' : {
            'kNum' : '2j_mm_in' ,
            'kDen' : '2j_ee_in' ,
            'RNum' : '2j_mm_out' ,
            'RDen' : '2j_mm_in' ,
        } ,
        '2jVHee' : {
            'kNum' : 'VH_ee_in' ,
            'kDen' : 'VH_mm_in' ,
            'RNum' : 'VH_ee_out' ,
            'RDen' : 'VH_ee_in' ,
        } ,
        '2jVHmm' : {
            'kNum' : 'VH_mm_in' ,
            'kDen' : 'VH_ee_in' ,
            'RNum' : 'VH_mm_out' ,
            'RDen' : 'VH_mm_in' ,
        } ,
        '2jVBFee' : {
            'kNum' : 'VBF_ee_in' ,
            'kDen' : 'VBF_mm_in' ,
            'RNum' : 'VBF_ee_out' ,
            'RDen' : 'VBF_ee_in' ,
        } ,
        '2jVBFmm' : {
            'kNum' : 'VBF_mm_in' ,
            'kDen' : 'VBF_ee_in' ,
            'RNum' : 'VBF_mm_out' ,
            'RDen' : 'VBF_mm_in' ,
        } ,
    } ,
}

#DYestim = {}
DYestim['hww2l2v_13TeV_0j_ee'] = {
    'rinout'  : 'DYmva0p80' ,
    'rsyst'   : 0.06 ,
    'ksyst'   : 0.01 ,
    'njet'    : '0j' ,
    'flavour' : 'ee' ,
    'DYProc'  : 'DY' ,
    'SFin'    : 'hww2l2v_13TeV_DYin_0j_ee' ,
    'SFinDa'  : 'DATA',
    'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'DFin'    : 'hww2l2v_13TeV_DYin_0j_df' ,
    'DFinDa'  : 'DATA' ,
    'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'NPname'  : 'DYeenorm0j' ,
    #'AccNum'  : 'hww2l2v_13TeV_HAccNum_0j_ee/events/histo_DY',
    #'AccDen'  : 'hww2l2v_13TeV_AccDen_0j_ee/events/histo_DY',
    #'asyst'   : 0.03 ,
}

DYestim['hww2l2v_13TeV_0j_mm'] = {
    'rinout'  : 'DYmva0p80' ,
    'rsyst'   : 0.05 , 
    'ksyst'   : 0.01 , 
    'njet'    : '0j'    ,
    'flavour' : 'mm' ,
    'DYProc'  : 'DY' ,
    'SFin'    : 'hww2l2v_13TeV_DYin_0j_mm' ,
    'SFinDa'  : 'DATA' ,
    'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'DFin'    : 'hww2l2v_13TeV_DYin_0j_df' ,
    'DFinDa'  : 'DATA' ,
    'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'NPname'  : 'DYmmnorm0j' ,
    #'AccNum'  : 'hww2l2v_13TeV_HAccNum_0j_mm/events/histo_DY',
    #'AccDen'  : 'hww2l2v_13TeV_AccDen_0j_mm/events/histo_DY',
    #'asyst'   : 0.01 ,
} 

DYestim['hww2l2v_13TeV_1j_ee'] = {
    'rinout'  : 'DYmva0p80' ,
    'rsyst'   : 0.02 , 
    'ksyst'   : 0.01 , 
    'njet'    : '1j'    ,
    'flavour' : 'ee' ,
    'DYProc'  : 'DY' ,
    'SFin'    : 'hww2l2v_13TeV_DYin_1j_ee' ,
    'SFinDa'  : 'DATA' ,
    'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'DFin'    : 'hww2l2v_13TeV_DYin_1j_df' ,
    'DFinDa'  : 'DATA' ,
    'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'NPname'  : 'DYeenorm1j' ,
    #'AccNum'  : 'hww2l2v_13TeV_HAccNum_1j_ee/events/histo_DY',
    #'AccDen'  : 'hww2l2v_13TeV_AccDen_1j_ee/events/histo_DY',
    #'asyst'   : 0.03 ,
} 

DYestim['hww2l2v_13TeV_1j_mm'] = {
    'rinout'  : 'DYmva0p80' ,
    'rsyst'   : 0.01 , 
    'ksyst'   : 0.01 , 
    'njet'    : '1j'    ,
    'flavour' : 'mm' ,
    'DYProc'  : 'DY' ,
    'SFin'    : 'hww2l2v_13TeV_DYin_1j_mm' ,
    'SFinDa'  : 'DATA' ,
    'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'DFin'    : 'hww2l2v_13TeV_DYin_1j_df' ,
    'DFinDa'  : 'DATA' ,
    'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'NPname'  : 'DYmmnorm1j' ,
    #'AccNum'  : 'hww2l2v_13TeV_HAccNum_1j_mm/events/histo_DY',
    #'AccDen'  : 'hww2l2v_13TeV_AccDen_1j_mm/events/histo_DY',
    #'asyst'   : 0.01 ,
} 

DYestim['hww2l2v_13TeV_2j_ee'] = {
    'rinout'  : 'DYmva0p80' ,
    'rsyst'   : 0.07 ,
    'ksyst'   : 0.01 ,
    'njet'    : '2j'    ,
    'flavour' : 'ee' ,
    'DYProc'  : 'DY' ,
    'SFin'    : 'hww2l2v_13TeV_DYin_2j_ee' ,
    'SFinDa'  : 'DATA' ,
    'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'DFin'    : 'hww2l2v_13TeV_DYin_2j_df' ,
    'DFinDa'  : 'DATA' ,
    'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'NPname'  : 'DYeenorm2j' ,
    #'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_ee/events/histo_DY',
    #'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_ee/events/histo_DY',
    #'asyst'   : 0.01 ,
}

DYestim['hww2l2v_13TeV_2j_mm'] = {
    'rinout'  : 'DYmva0p80' ,
    'rsyst'   : 0.01 ,
    'ksyst'   : 0.03 ,
    'njet'    : '2j'    ,
    'flavour' : 'mm' ,
    'DYProc'  : 'DY' ,
    'SFin'    : 'hww2l2v_13TeV_DYin_2j_mm' ,
    'SFinDa'  : 'DATA' ,
    'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'DFin'    : 'hww2l2v_13TeV_DYin_2j_df' ,
    'DFinDa'  : 'DATA' ,
    'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'NPname'  : 'DYmmnorm2j' ,
    #'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_mm/events/histo_DY',
    #'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_mm/events/histo_DY',
    #'asyst'   : 0.04 ,
}

DYestim['hww2l2v_13TeV_2j_vbf_ee'] = {
    'rinout'  : 'DYmva0p80' ,
    'rsyst'   : 0.02 ,
    'ksyst'   : 0.02 ,
    'njet'    : '2jVBF'    ,
    'flavour' : 'ee' ,
    'DYProc'  : 'DY' ,
    'SFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_ee' ,
    'SFinDa'  : 'DATA' ,
    'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'DFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_df' ,
    'DFinDa'  : 'DATA' ,
    'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'NPname'  : 'DYeenorm2jvbf' ,
    #'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_vbf_ee/events/histo_DY',
    #'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vbf_ee/events/histo_DY',
    #'asyst'   : 0.21 ,
}

DYestim['hww2l2v_13TeV_2j_vbf_mm'] = {
    'rinout'  : 'DYmva0p80' ,
    'rsyst'   : 0.02 ,
    'ksyst'   : 0.03 ,
    'njet'    : '2jVBF'    ,
    'flavour' : 'mm' ,
    'DYProc'  : 'DY' ,
    'SFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_mm' ,
    'SFinDa'  : 'DATA' ,
    'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'DFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_df' ,
    'DFinDa'  : 'DATA' ,
    'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'NPname'  : 'DYmmnorm2jvbf' ,
    #'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_vbf_mm/events/histo_DY',
    #'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vbf_mm/events/histo_DY',
    #'asyst'   : 0.01 ,
}

DYestim['hww2l2v_13TeV_2j_vh_ee'] = {
    'rinout'  : 'DYmva0p80' ,
    'rsyst'   : 0.02 ,
    'ksyst'   : 0.02 ,
    'njet'    : '2jVH'    ,
    'flavour' : 'ee' ,
    'DYProc'  : 'DY' ,
    'SFin'    : 'hww2l2v_13TeV_DYin_2j_vh_ee' ,
    'SFinDa'  : 'DATA' ,
    'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'DFin'    : 'hww2l2v_13TeV_DYin_2j_vh_df' ,
    'DFinDa'  : 'DATA' ,
    'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'NPname'  : 'DYeenorm2jvh' ,
    #'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_vh_ee/events/histo_DY',
    #'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vh_ee/events/histo_DY',
    #'asyst'   : 0.01 ,
}

DYestim['hww2l2v_13TeV_2j_vh_mm'] = {
    'rinout'  : 'DYmva0p80' ,
    'rsyst'   : 0.03 ,
    'ksyst'   : 0.05 ,
    'njet'    : '2jVH'    ,
    'flavour' : 'mm' ,
    'DYProc'  : 'DY' ,
    'SFin'    : 'hww2l2v_13TeV_DYin_2j_vh_mm' ,
    'SFinDa'  : 'DATA' ,
    'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'DFin'    : 'hww2l2v_13TeV_DYin_2j_vh_df' ,
    'DFinDa'  : 'DATA' ,
    'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'NPname'  : 'DYmmnorm2jvh' ,
    #'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_vh_mm/events/histo_DY',
    #'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vh_mm/events/histo_DY',
    #'asyst'   : 0.01 ,
}
