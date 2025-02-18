#RAndKff  = {}
RAndKff['DYmva0p8'] = {            
    'RFile'   : 'rootFile/plots_DYESTIM_qqH_SF_2017_v7_DYMVA080.root' ,
    'KffFile' : 'rootFile/plots_DYESTIM_qqH_SF_2017_v7_DYMVA080.root' ,
    'Regions' : { 
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
    } ,
}

RAndKff['DYmva0p9'] = {            
    'RFile'   : 'rootFile/plots_DYESTIM_qqH_SF_2017_v7_DYMVA090.root' ,
    'KffFile' : 'rootFile/plots_DYESTIM_qqH_SF_2017_v7_DYMVA080.root' ,
    'Regions' : { 
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

DYestim['hww2l2v_13TeV_2j_vh_ee'] = {
    'rinout'  : 'DYmva0p8' ,
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
    'NPname'  : 'DYeenormvh' ,
    'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_vh_ee/events/histo_DY',
    'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vh_ee/events/histo_DY',
    'asyst'   : 0.12 ,
}

DYestim['hww2l2v_13TeV_2j_vh_mm'] = {
    'rinout'  : 'DYmva0p8' ,
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
    'NPname'  : 'DYmmnormvh' ,
    'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_vh_mm/events/histo_DY',
    'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vh_mm/events/histo_DY',
    'asyst'   : 0.02 ,
}

DYestim['hww2l2v_13TeV_2j_vbf_ee'] = {
    'rinout'  : 'DYmva0p9' ,
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
    'NPname'  : 'DYeenormvbf' ,
    'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_vbf_ee/events/histo_DY',
    'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vbf_ee/events/histo_DY',
    'asyst'   : 0.06 ,
}

DYestim['hww2l2v_13TeV_2j_vbf_mm'] = {
    'rinout'  : 'DYmva0p9' ,
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
    'NPname'  : 'DYmmnormvbf' ,
    'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_vbf_mm/events/histo_DY',
    'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vbf_mm/events/histo_DY',
    'asyst'   : 0.03 ,
}

DYestim['hww2l2v_13TeV_WW_2j_vh_ee'] = {
    'rinout'  : 'DYmva0p8' ,
    'njet'    : '2jVH'    ,
    'flavour' : 'ee' ,
    'DYProc'  : 'DY' ,
    'SFin'    : 'hww2l2v_13TeV_DYin_2j_vh_ee' ,
    'SFinDa'  : 'DATA',
    'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'DFin'    : 'hww2l2v_13TeV_DYin_2j_vh_df' ,
    'DFinDa'  : 'DATA' ,
    'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'NPname'  : 'DYeenormvh' ,
    'AccNum'  : 'hww2l2v_13TeV_wwAcc_2j_vh_ee/events/histo_DY',
    'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vh_ee/events/histo_DY',
    'asyst'   : 0.10 ,
}

DYestim['hww2l2v_13TeV_WW_2j_vh_mm'] = {
    'rinout'  : 'DYmva0p8' ,
    'njet'    : '2jVH'    ,
    'flavour' : 'mm' ,
    'DYProc'  : 'DY' ,
    'SFin'    : 'hww2l2v_13TeV_DYin_2j_vh_mm' ,
    'SFinDa'  : 'DATA',
    'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'DFin'    : 'hww2l2v_13TeV_DYin_2j_vh_df' ,
    'DFinDa'  : 'DATA' ,
    'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'NPname'  : 'DYmmnormvh' ,
    'AccNum'  : 'hww2l2v_13TeV_wwAcc_2j_vh_mm/events/histo_DY',
    'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vh_mm/events/histo_DY',
    'asyst'   : 0.02 ,
}

DYestim['hww2l2v_13TeV_WW_2j_vbf_ee'] = {
    'rinout'  : 'DYmva0p9' ,
    'njet'    : '2jVBF'    ,
    'flavour' : 'ee' ,
    'DYProc'  : 'DY' ,
    'SFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_ee' ,
    'SFinDa'  : 'DATA',
    'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'DFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_df' ,
    'DFinDa'  : 'DATA' ,
    'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'NPname'  : 'DYeenormvbf' ,
    'AccNum'  : 'hww2l2v_13TeV_wwAcc_2j_vbf_ee/events/histo_DY',
    'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vbf_ee/events/histo_DY',
    'asyst'   : 0.02 ,
}

DYestim['hww2l2v_13TeV_WW_2j_vbf_mm'] = {
    'rinout'  : 'DYmva0p9' ,
    'njet'    : '2jVBF'    ,
    'flavour' : 'mm' ,
    'DYProc'  : 'DY' ,
    'SFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_mm' ,
    'SFinDa'  : 'DATA',
    'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'DFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_df' ,
    'DFinDa'  : 'DATA' ,
    'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
    'NPname'  : 'DYmmnormvbf' ,
    'AccNum'  : 'hww2l2v_13TeV_wwAcc_2j_vbf_mm/events/histo_DY',
    'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vbf_mm/events/histo_DY',
    'asyst'   : 0.02 ,
}

