void plotRatio(TString cut="0j_pt2lt20",TString var ="mll", TString sample = "ggH_hww"){

TString dir = "Direct/rootFile";

TFile *f = TFile::Open(dir+"/plots_ggH2018_v7_trigsyst.root");

TString dir2 = "Eff_fromTnP/rootFile_drllrew_fine";

TFile *f2 = TFile::Open(dir2+"/plots_ggH2018_v7_TnPEff.root");

  TH1F *h_total;
  TH1F *h_pass_Trig;
  TString tag = cut;

  h_total = (TH1F*)f->Get("hww2l2v_13TeV_"+cut+"/"+var+"/histo_"+sample);
  if ( cut.Contains("dytt") ) h_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_"+tag.ReplaceAll("dytt","dytt_withTrig")+"/"+var+"/histo_"+sample);
  else if ( cut.Contains("top") && !cut.Contains("DNN_top") ) h_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_"+tag.ReplaceAll("top","top_withTrig")+"/"+var+"/histo_"+sample);
  else h_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_"+tag+"/"+var+"/histo_"+sample);

  TH1F *hTP_total;
  TH1F *hTP_pass_Trig;
  TH1F *hTP_pass_TrigUp;
  TH1F *hTP_pass_TrigDown;

  hTP_total = (TH1F*)f2->Get("hww2l2v_13TeV_"+cut+"/"+var+"/histo_"+sample);
  hTP_pass_Trig = (TH1F*)f2->Get("hww2l2v_13TeV_"+cut+"/"+var+"/histo_"+sample+"_Trig");
  //hTP_pass_TrigUp = (TH1F*)f2->Get("hww2l2v_13TeV_"+cut+"/"+var+"/histo_"+sample+"_Trig_CMS_eff_hwwtrigger_2018Up");
  //hTP_pass_TrigDown = (TH1F*)f2->Get("hww2l2v_13TeV_"+cut+"/"+var+"/histo_"+sample+"_Trig_CMS_eff_hwwtrigger_2018Down");

  TMultiGraph *mgme = new TMultiGraph();

  TGraphAsymmErrors *grame_Trig = new TGraphAsymmErrors (h_pass_Trig, h_total);

  TGraphAsymmErrors *graTPme_Trig = new TGraphAsymmErrors (hTP_pass_Trig, hTP_total);
  //TGraphAsymmErrors *graTPme_TrigUp = new TGraphAsymmErrors (hTP_pass_TrigUp, hTP_total);
  //TGraphAsymmErrors *graTPme_TrigDown = new TGraphAsymmErrors (hTP_pass_TrigDown, hTP_total);

  //TGraphAsymmErrors *graTPunc = new TGraphAsymmErrors ();
  //for (int i=0; i<graTPme_TrigUp->GetN(); ++i){
  //  double uncyh, uncyl, x, y;
  //  graTPme_Trig->GetPoint(i,x,y); 
  //  graTPme_TrigUp->GetPoint(i,x,uncyh);
  //  graTPme_TrigDown->GetPoint(i,x,uncyl);
  //  graTPunc->SetPoint(i,x,y);
  //  graTPunc->SetPointEYhigh(i,uncyh-y);
  //  graTPunc->SetPointEYlow(i,y-uncyl);
  //  cout << x << " " << y << " " << uncyh-y << " " << y-uncyl << endl;
  //}

  TCanvas *cc = new TCanvas("cc","",200,10,600,500);
  grame_Trig->SetLineColor(1);
  grame_Trig->SetMarkerColor(1);
  grame_Trig->SetMarkerStyle(20);
  graTPme_Trig->SetLineColor(2);
  graTPme_Trig->SetMarkerColor(2);
  graTPme_Trig->SetMarkerStyle(20);
  grame_Trig->SetMaximum(1.);
  grame_Trig->SetMinimum(0.8);

  //graTPunc->SetFillColor(2);
  //graTPunc->SetFillStyle(3005);
  //graTPunc->SetMaximum(1.);
  //graTPunc->SetMinimum(0.8);
  //graTPunc->Draw("A3");
  grame_Trig->Draw("AP");
  graTPme_Trig->Draw("Psame");

  TLegend *legend = new TLegend(0.5,0.1,0.8,0.3);
  legend->AddEntry(grame_Trig,"Comb - Direct MC Efficiency","p");
  legend->AddEntry(graTPme_Trig,"Comb - MC T&P Efficiency","p");
  //legend->AddEntry(graTPunc,"T&P Efficiency Uncertainty","f");
  legend->Draw();

  cc->Print("drll_rew/TriggerEffCombComparison_"+cut+"_"+var+"_"+sample+".png");
  cc->Clear();

  TGraphAsymmErrors *ratiome_Trig = new TGraphAsymmErrors();
  //TGraphAsymmErrors *ratiome_TrigUnc = new TGraphAsymmErrors();

   for (int i=0; i<grame_Trig->GetN(); ++i){
    double x,y,xtp,ytp,eyl,eyh,eyl2,eyh2;
    grame_Trig->GetPoint(i,x,y);
    eyh = grame_Trig->GetErrorYhigh(i);
    eyl = grame_Trig->GetErrorYlow(i);
    eyh2 = graTPme_Trig->GetErrorYhigh(i);
    eyl2 = graTPme_Trig->GetErrorYlow(i);

    graTPme_Trig->GetPoint(i,xtp,ytp);

    ratiome_Trig->SetPoint(i,x,y/ytp);
    ratiome_Trig->SetPointEYhigh(i,sqrt(eyh*eyh/y/y+eyh2*eyh2/ytp/ytp)*y/ytp);
    ratiome_Trig->SetPointEYlow(i,sqrt(eyl*eyl/y/y+eyl2*eyl2/ytp/ytp)*y/ytp);

    //double uncyh, uncyl;
    //graTPme_TrigUp->GetPoint(i,x,uncyh);
    //graTPme_TrigDown->GetPoint(i,x,uncyl);

    //ratiome_TrigUnc->SetPoint(i,x,1.);
    //ratiome_TrigUnc->SetPointEYhigh(i,y/uncyl-y/ytp);
    //ratiome_TrigUnc->SetPointEYlow(i,y/ytp-y/uncyh);
    //cout << y/ytp << " down = " << y/uncyh << " up = " << y/uncyl << endl; 
   }


  mgme->Add(ratiome_Trig);
  //mgme->Add(ratiome_TrigUnc,"4");

  ratiome_Trig->SetLineColor(4);
  ratiome_Trig->SetMarkerStyle(20);

  ratiome_Trig->SetMarkerColor(4);

  //ratiome_TrigUnc->SetFillColor(8);
  //ratiome_TrigUnc->SetFillStyle(3005);

  mgme->SetTitle(h_total->GetTitle());
  TCanvas *cme = new TCanvas("cme","",200,10,600,500);

  mgme->Draw("APE");
  mgme->SetMinimum(0.8);
  mgme->SetMaximum(1.2);
  mgme->GetXaxis()->SetTitle(var);
  mgme->GetXaxis()->CenterTitle(1);
  mgme->GetXaxis()->SetTitleOffset(1.2);
  mgme->GetYaxis()->SetTitle("Direct / MC T&P");
  mgme->GetYaxis()->CenterTitle(1);
  mgme->GetYaxis()->SetTitleOffset(1.4);

   TLegend *legendme = new TLegend(0.5,0.1,0.8,0.3);
   legendme->AddEntry(ratiome_Trig,"Comb","p");
   //legendme->AddEntry(ratiome_TrigUnc,"Trig Uncertainty","f");
   legendme->Draw();

  TLine *line;
  if (var=="mll") line = new TLine(12,1,210,1);
  else if (var=="mth") line = new TLine(60,1,210,1);
  else line = new TLine(0,1,2,1);

  line->SetLineWidth(2);
  line->Draw();

  cme->Print("drll_rew/ratio_TriggerEff_"+cut+"_"+var+"_"+sample+".png");
  cme->Clear();

}
