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
      'em' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==13',
      'me' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==11',
      'ee' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==11',
      'mm' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==13',
      '2j' : ' Sum$(CleanJet_pt>30)==2 && mjj>120.',
   }
}

cuts['hww2l2v_13TeV_withTrig'] = {
   'expr': 'sr_withTrig',
   'categories' : {
      'em' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==13',
      'me' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==11',
      'ee' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==11',
      'mm' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==13',
      '2j' : ' Sum$(CleanJet_pt>30)==2 && mjj>120.',
   }
}

'''
cuts['hww2l2v_13TeV_withTrig_singleEl'] = {
   'expr': 'sr_withTrig_singleEl',
   'categories' : {
      'em' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==13',
      'me' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==11',
      'ee' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==11',
      'mm' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==13',
   }
}

cuts['hww2l2v_13TeV_withTrig_singleMu'] = {
   'expr': 'sr_withTrig_singleMu',
   'categories' : {
      'em' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==13',
      'me' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==11',
      'ee' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==11',
      'mm' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==13',
   }

}

cuts['hww2l2v_13TeV_withTrig_ElMu'] = {
   'expr': 'sr_withTrig_ElMu',
   'categories' : {
      'em' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==13',
      'me' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==11',
      'ee' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==11',
      'mm' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==13',
   }

}

cuts['hww2l2v_13TeV_withTrig_DoubleMu'] = {
   'expr': 'sr_withTrig_DoubleMu',
   'categories' : {
      'em' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==13',
      'me' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==11',
      'ee' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==11',
      'mm' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==13',
   }

}

cuts['hww2l2v_13TeV_withTrig_DoubleE'] = {
   'expr': 'sr_withTrig_DoubleE',
   'categories' : {
      'em' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==13',
      'me' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==11',
      'ee' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==11',
      'mm' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==13',
   }

}

#cuts['hww2l2v_13TeV_withTrig_MuE'] = {
#   'expr': 'sr_withTrig_MuE',
#   'categories' : {
#      'em' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==13',
#      'me' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==11',
#      'ee' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==11',
#      'mm' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==13',
#   }
#}

cuts['hww2l2v_13TeV_withTrig'] = {
   'expr': 'sr_withTrig',
   'categories' : {
      'em' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==13',
      'me' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==11',
      'ee' : ' abs(Lepton_pdgId[0])==11 && abs(Lepton_pdgId[1])==11',
      'mm' : ' abs(Lepton_pdgId[0])==13 && abs(Lepton_pdgId[1])==13',
   }
}
'''
