void plotRatio(TString var ="eta1", TString flav = "me", bool isData=false){

TString dir = "rootFile_allflav";

TFile *f = TFile::Open(dir+"/plots_ggH2018_v7.root");



TString dir1 = isData ? "Eff_fromTnP/rootFile_TandP_data" : "Eff_fromTnP/rootFile_final";
TString dir2 = isData ? "Eff_fromTnP/rootFile_TandP_data" : "Eff_fromTnP/rootFile_final";

TFile *f1 = TFile::Open(dir1+"/plots_ggH2018_v7_TnPEff.root");
TFile *f2 = TFile::Open(dir2+"/plots_ggH2018_v7_TnPEff.root");


   TH1F *h_total;
   TH1F *h_pass_singlEl;
   TH1F *h_pass_singlMu;
   TH1F *h_pass_ElMu;
   TH1F *h_pass_DoubleMu;
   TH1F *h_pass_DoubleE;
   TH1F *h_pass_Trig;


  h_total = (TH1F*)f->Get("hww2l2v_13TeV_"+flav+"/"+var+"/histo_ggH_hww");
  h_pass_singlEl = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_singleEl_"+flav+"/"+var+"/histo_ggH_hww");
  h_pass_singlMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_singleMu_"+flav+"/"+var+"/histo_ggH_hww");
  h_pass_ElMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_ElMu_"+flav+"/"+var+"/histo_ggH_hww");
  h_pass_DoubleMu = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_DoubleMu_"+flav+"/"+var+"/histo_ggH_hww");
  h_pass_DoubleE = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_DoubleE_"+flav+"/"+var+"/histo_ggH_hww");
  h_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_"+flav+"/"+var+"/histo_ggH_hww");


   TH1F *hTP_total;
   TH1F *hTP_pass_singlEl;
   TH1F *hTP_pass_singlMu;
   TH1F *hTP_pass_ElMu;
   TH1F *hTP_pass_DoubleMu;
   TH1F *hTP_pass_DoubleE;
   TH1F *hTP_pass_Trig;
   TH1F *hTP_pass_TrigUp;
   TH1F *hTP_pass_TrigDown;


  hTP_total = (TH1F*)f1->Get("hww2l2v_13TeV_"+flav+"/"+var+"/histo_ggH_hww");
  hTP_pass_singlEl = (TH1F*)f1->Get("hww2l2v_13TeV_"+flav+"/"+var+"/histo_ggH_hww_singlEl");
  hTP_pass_singlMu = (TH1F*)f1->Get("hww2l2v_13TeV_"+flav+"/"+var+"/histo_ggH_hww_singlMu");
  hTP_pass_ElMu = (TH1F*)f1->Get("hww2l2v_13TeV_"+flav+"/"+var+"/histo_ggH_hww_ElMu");
  hTP_pass_DoubleMu = (TH1F*)f1->Get("hww2l2v_13TeV_"+flav+"/"+var+"/histo_ggH_hww_dblMu");
  hTP_pass_DoubleE = (TH1F*)f1->Get("hww2l2v_13TeV_"+flav+"/"+var+"/histo_ggH_hww_dblEl");
  hTP_pass_Trig = (TH1F*)f2->Get("hww2l2v_13TeV_"+flav+"/"+var+"/histo_ggH_hww_Trig");
  hTP_pass_TrigUp = (TH1F*)f2->Get("hww2l2v_13TeV_"+flav+"/"+var+"/histo_ggH_hww_Trig_CMS_eff_hwwtrigger_2018Up");
  hTP_pass_TrigDown = (TH1F*)f2->Get("hww2l2v_13TeV_"+flav+"/"+var+"/histo_ggH_hww_Trig_CMS_eff_hwwtrigger_2018Down");


  TMultiGraph *mgme = new TMultiGraph();

  TGraphAsymmErrors *grame_singlEl = new TGraphAsymmErrors (h_pass_singlEl,h_total);
  TGraphAsymmErrors *grame_singlMu = new TGraphAsymmErrors (h_pass_singlMu, h_total);
  TGraphAsymmErrors *grame_ElMu = new TGraphAsymmErrors (h_pass_ElMu, h_total);
  TGraphAsymmErrors *grame_DoubleMu = new TGraphAsymmErrors (h_pass_DoubleMu, h_total);
  TGraphAsymmErrors *grame_DoubleE = new TGraphAsymmErrors (h_pass_DoubleE, h_total);
  TGraphAsymmErrors *grame_Trig = new TGraphAsymmErrors (h_pass_Trig, h_total);

  TGraphAsymmErrors *graTPme_singlEl = new TGraphAsymmErrors (hTP_pass_singlEl,hTP_total);
  TGraphAsymmErrors *graTPme_singlMu = new TGraphAsymmErrors (hTP_pass_singlMu, hTP_total);
  TGraphAsymmErrors *graTPme_ElMu = new TGraphAsymmErrors (hTP_pass_ElMu, hTP_total);
  TGraphAsymmErrors *graTPme_DoubleMu = new TGraphAsymmErrors (hTP_pass_DoubleMu, hTP_total);
  TGraphAsymmErrors *graTPme_DoubleE = new TGraphAsymmErrors (hTP_pass_DoubleE, hTP_total);
  TGraphAsymmErrors *graTPme_Trig = new TGraphAsymmErrors (hTP_pass_Trig, hTP_total);
  TGraphAsymmErrors *graTPme_TrigUp = new TGraphAsymmErrors (hTP_pass_TrigUp, hTP_total);
  TGraphAsymmErrors *graTPme_TrigDown = new TGraphAsymmErrors (hTP_pass_TrigDown, hTP_total);

  TGraphAsymmErrors *graTPunc = new TGraphAsymmErrors ();
  for (int i=0; i<graTPme_TrigUp->GetN(); ++i){
    double uncyh, uncyl, x, y;
    graTPme_Trig->GetPoint(i,x,y); 
    graTPme_TrigUp->GetPoint(i,x,uncyh);
    graTPme_TrigDown->GetPoint(i,x,uncyl);
    graTPunc->SetPoint(i,x,y);
    graTPunc->SetPointEYhigh(i,uncyh-y);
    graTPunc->SetPointEYlow(i,y-uncyl);
    cout << x << " " << y << " " << uncyh-y << " " << y-uncyl << endl;
  }

  TCanvas *cc = new TCanvas("cc","",200,10,600,500);
  grame_Trig->SetLineColor(1);
  grame_Trig->SetMarkerColor(1);
  grame_Trig->SetMarkerStyle(20);
  graTPme_Trig->SetLineColor(2);
  graTPme_Trig->SetMarkerColor(2);
  graTPme_Trig->SetMarkerStyle(20);
  graTPunc->SetFillColor(2);
  graTPunc->SetFillStyle(3005);
  graTPunc->SetMaximum(1.);
  graTPunc->SetMinimum(0.8);
  graTPunc->Draw("A3");
  grame_Trig->Draw("Psame");
  graTPme_Trig->Draw("Psame");

  TLegend *legend = new TLegend(0.5,0.1,0.8,0.3);
  legend->AddEntry(grame_Trig,"Comb - Direct MC Efficiency","p");
  legend->AddEntry(graTPme_Trig,"Comb - MC T&P Efficiency","p");
  legend->AddEntry(graTPunc,"T&P Efficiency Uncertainty","f");
  legend->Draw();

  cc->Print("TriggerEffCombComparison_"+flav+"_"+var+".png");
  cc->Clear();



  TGraphAsymmErrors *ratiome_singlEl = new TGraphAsymmErrors();
  TGraphAsymmErrors *ratiome_singlMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *ratiome_ElMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *ratiome_DoubleMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *ratiome_DoubleE = new TGraphAsymmErrors();
  TGraphAsymmErrors *ratiome_Trig = new TGraphAsymmErrors();
  TGraphAsymmErrors *ratiome_TrigUnc = new TGraphAsymmErrors();


//   for (int i=0; i<grame_singlEl->GetN(); ++i){
//    double x,y,xtp,ytp,eyl,eyh;
//    grame_singlEl->GetPoint(i,x,y);
//    eyh = grame_singlEl->GetErrorYhigh(i);
//    eyl = grame_singlEl->GetErrorYlow(i);
//    graTPme_singlEl->GetPoint(i,xtp,ytp);
//    ratiome_singlEl->SetPoint(i,x,y/ytp);
//    ratiome_singlEl->SetPointEYhigh(i,eyh/y/ytp);
//    ratiome_singlEl->SetPointEYlow(i,eyl/y/ytp);
//  }
// 
//   for (int i=0; i<grame_singlMu->GetN(); ++i){
//    double x,y,xtp,ytp,eyl,eyh;
//    grame_singlMu->GetPoint(i,x,y);
//    eyh = grame_singlMu->GetErrorYhigh(i);
//    eyl = grame_singlMu->GetErrorYlow(i);
//    graTPme_singlMu->GetPoint(i,xtp,ytp);
//    ratiome_singlMu->SetPoint(i,x,y/ytp);
//    ratiome_singlMu->SetPointEYhigh(i,eyh);
//    ratiome_singlMu->SetPointEYlow(i,eyl);
//  }
//
//   for (int i=0; i<grame_ElMu->GetN(); ++i){
//    double x,y,xtp,ytp,eyl,eyh;
//    grame_ElMu->GetPoint(i,x,y);
//    eyh = grame_ElMu->GetErrorYhigh(i);
//    eyl = grame_ElMu->GetErrorYlow(i);
//    graTPme_ElMu->GetPoint(i,xtp,ytp);
//    ratiome_ElMu->SetPoint(i,x,y/ytp);
//    ratiome_ElMu->SetPointEYhigh(i,eyh);
//    ratiome_ElMu->SetPointEYlow(i,eyl);
//  }
//
//   for (int i=0; i<grame_DoubleMu->GetN(); ++i){
//    double x,y,xtp,ytp,eyl,eyh;
//    grame_DoubleMu->GetPoint(i,x,y);
//    eyh = grame_DoubleMu->GetErrorYhigh(i);
//    eyl = grame_DoubleMu->GetErrorYlow(i);
//    graTPme_DoubleMu->GetPoint(i,xtp,ytp);
//    ratiome_DoubleMu->SetPoint(i,x,y/ytp);
//    ratiome_DoubleMu->SetPointEYhigh(i,eyh);
//    ratiome_DoubleMu->SetPointEYlow(i,eyl);
//  }
//
//   for (int i=0; i<grame_DoubleE->GetN(); ++i){
//    double x,y,xtp,ytp,eyl,eyh;
//    grame_DoubleE->GetPoint(i,x,y);
//    eyh = grame_DoubleE->GetErrorYhigh(i);
//    eyl = grame_DoubleE->GetErrorYlow(i);
//    graTPme_DoubleE->GetPoint(i,xtp,ytp);
//    ratiome_DoubleE->SetPoint(i,x,y/ytp);
//    ratiome_DoubleE->SetPointEYhigh(i,eyh);
//    ratiome_DoubleE->SetPointEYlow(i,eyl);
//  }

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


    double uncyh, uncyl;
    graTPme_TrigUp->GetPoint(i,x,uncyh);
    graTPme_TrigDown->GetPoint(i,x,uncyl);

    ratiome_TrigUnc->SetPoint(i,x,1.);
    ratiome_TrigUnc->SetPointEYhigh(i,y/uncyl-y/ytp);
    ratiome_TrigUnc->SetPointEYlow(i,y/ytp-y/uncyh);
    cout << y/ytp << " down = " << y/uncyh << " up = " << y/uncyl << endl; 
  }


  mgme->Add(ratiome_singlEl);
  mgme->Add(ratiome_singlMu);
  mgme->Add(ratiome_ElMu);
  mgme->Add(ratiome_DoubleMu);
  mgme->Add(ratiome_DoubleE);
  mgme->Add(ratiome_Trig);
  mgme->Add(ratiome_TrigUnc,"4");


  ratiome_singlEl->SetLineColor(1);
  ratiome_singlMu->SetLineColor(2);
  ratiome_ElMu->SetLineColor(3);
  ratiome_DoubleMu->SetLineColor(5);
  ratiome_DoubleE->SetLineColor(7);
  ratiome_Trig->SetLineColor(4);

  ratiome_singlEl->SetMarkerStyle(20);
  ratiome_singlMu->SetMarkerStyle(20);
  ratiome_ElMu->SetMarkerStyle(20);
  ratiome_DoubleMu->SetMarkerStyle(20);
  ratiome_DoubleE->SetMarkerStyle(20);
  ratiome_Trig->SetMarkerStyle(20);

  ratiome_singlEl->SetMarkerColor(1);
  ratiome_singlMu->SetMarkerColor(2);
  ratiome_ElMu->SetMarkerColor(3);
  ratiome_DoubleMu->SetMarkerColor(5);
  ratiome_DoubleE->SetMarkerColor(7);
  ratiome_Trig->SetMarkerColor(4);

  ratiome_TrigUnc->SetFillColor(8);
  ratiome_TrigUnc->SetFillStyle(3005);

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

  //ratiome_TrigUnc->Draw("4 same");
   TLegend *legendme = new TLegend(0.5,0.1,0.8,0.3);
   //legendme->AddEntry(ratiome_singlEl,"SingleEle","p");
   //legendme->AddEntry(ratiome_singlMu,"SingleMu","p");
   //legendme->AddEntry(ratiome_ElMu,"E+Mu","p");
   //legendme->AddEntry(ratiome_DoubleMu,"DoubleMu","p");
   //legendme->AddEntry(ratiome_DoubleE,"DoubleE","p");
   legendme->AddEntry(ratiome_Trig,"Comb","p");
   legendme->AddEntry(ratiome_TrigUnc,"Trig Uncertainty","f");
   legendme->Draw();

  TLine *line;
  if (var=="eta1" or var=="eta2") line = new TLine(-3,1,3,1);
  else line = new TLine(0,1,100,1);

  line->SetLineWidth(2);
  line->Draw();

  cme->Print("ratio_TriggerEff_"+flav+"_"+var+".png");
  cme->Clear();

}
