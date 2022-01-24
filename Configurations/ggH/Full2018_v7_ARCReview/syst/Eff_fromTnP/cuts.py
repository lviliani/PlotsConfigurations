# cuts

supercut = ' mll > 12 \
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>13 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && ptll>30 \
            && PuppiMET_pt > 20 \
            && (Lepton_pdgId[0]*Lepton_pdgId[1] < 0) \
            '

## Signal regions
cuts['hww2l2v_13TeV'] = {
   'expr': 'sr',
   'categories' : {
      '0j_pt2lt20' : ' Lepton_pt[1]<20 && zeroJet',
      '0j_pt2ge20' : ' Lepton_pt[1]>=20 && zeroJet',
      '1j_pt2lt20' : ' Lepton_pt[1]<20 && oneJet && Alt$(CleanJet_pt[1],0)<30',
      '1j_pt2ge20' : ' Lepton_pt[1]>=20 && oneJet && Alt$(CleanJet_pt[1],0)<30',
      '2j'         : ' (mjj<65 || mjj>105) && mjj<120 && multiJet',
      '2j_vh'      :  'abs(CleanJet_eta[0]) < 2.5 && abs(CleanJet_eta[1]) < 2.5 && multiJet && mjj > 65. && mjj < 105. && drll < 2. && detajj < 3.5',
      'of2j_DNN_vbf' : ' (mth>=60 && mth<125) && mjj>120 && (abs(CleanJet_eta[0])<4.7) && (abs(CleanJet_eta[1])<4.7) && vbflike && Sum$(CleanJet_pt>30)==2', 
      'of2j_DNN_top' : ' (mth>=60 && mth<125) && mjj>120 && (abs(CleanJet_eta[0])<4.7) && (abs(CleanJet_eta[1])<4.7) && toplike && Sum$(CleanJet_pt>30)==2',   
      'of2j_DNN_ww' : ' (mth>=60 && mth<125) && mjj>120 && (abs(CleanJet_eta[0])<4.7) && (abs(CleanJet_eta[1])<4.7) && wwlike && Sum$(CleanJet_pt>30)==2',   
      'of2j_DNN_ggh' : ' (mth>=60 && mth<125) && mjj>120 && (abs(CleanJet_eta[0])<4.7) && (abs(CleanJet_eta[1])<4.7) && gghlike && Sum$(CleanJet_pt>30)==2',   

   }
}

## Top control regions
cuts['hww2l2v_13TeV_top']  = {
   'expr' : 'topcr',
   'categories' : {
      '0j' : 'zeroJet',
      '1j' : 'oneJet && Alt$(CleanJet_pt[1],0)<30',
      '2j' : '(mjj<65 || mjj>105) && mjj<120 && multiJet',
      '2j_vbf' : 'mjj>120 && Sum$(CleanJet_pt>30)==2',
      '2j_vh' : 'mjj > 65. && mjj < 105. && multiJet',
   }
}

## DYtt control regions
cuts['hww2l2v_13TeV_dytt']  = {
   'expr' : 'dycr',
   'categories' : {
      '0j' : 'zeroJet',
      '1j' : 'oneJet && Alt$(CleanJet_pt[1],0)<30',
      '2j' : '(mjj<65 || mjj>105) && mjj<120 && multiJet',
      '2j_vbf' : 'mjj>120 && Sum$(CleanJet_pt>30)==2',
      '2j_vh' : 'mjj > 65. && mjj < 105. && multiJet',
   }
}

