# cuts

supercut = '1.'

cuts['hww2l2v_13TeV'] = 'MinIf$( WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) > 12 \
            && Alt$(Lepton_pt[0],0)>25 \
            && Alt$(Lepton_pt[1],0)>20 \
            && Alt$(Lepton_pt[2],0)>15 \
            && (nLepton>=3 && Alt$(Lepton_pt[3],0)<10) \
            && abs(WH3l_chlll) == 1 \
           '
