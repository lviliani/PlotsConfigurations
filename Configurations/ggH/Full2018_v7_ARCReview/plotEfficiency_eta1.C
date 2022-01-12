void plotEfficiency_eta1() {

TFile *f1 = TFile::Open("rootFile/plots_ggH2018_v7.root");

   TH1F *h_total;
   TH1F *h_pass_singlEl;
   TH1F *h_pass_singlMu;
   TH1F *h_pass_ElMu;
   TH1F *h_pass_Trig;

   TGraphAsymmErrors *gra_2018A=0;

  h_total = (TH1F*)f1->Get("hww2l2v_13TeV/eta1/histo_ggH_hww");
  h_pass_singlEl = (TH1F*)f1->Get("hww2l2v_13TeV_withTrig_singleEl/eta1/histo_ggH_hww");
  h_pass_singlMu = (TH1F*)f1->Get("hww2l2v_13TeV_withTrig_singleMu/eta1/histo_ggH_hww");
  h_pass_ElMu = (TH1F*)f1->Get("hww2l2v_13TeV_withTrig_ElMu/eta1/histo_ggH_hww");
  h_pass_Trig = (TH1F*)f1->Get("hww2l2v_13TeV_withTrig/eta1/histo_ggH_hww");

//for(int i = 1; i < h_pass->GetNbinsX(); i ++) {
//cout << "total =  " << h_total->GetBinContent(i) << "  " << "pass = " <<  h_pass->GetBinContent(i) << endl;
//}

  TMultiGraph *mg = new TMultiGraph();
  TGraphAsymmErrors *gra_singlEl = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_singlMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_ElMu = new TGraphAsymmErrors();
  TGraphAsymmErrors *gra_Trig = new TGraphAsymmErrors();

//  gra_singlEl = new TGraphAsymmErrors (h_pass_singlEl,h_total);
//  gra_singlMu = new TGraphAsymmErrors (h_pass_singlMu,h_total);



  gra_singlEl = new TGraphAsymmErrors (h_pass_singlEl,h_total);
  gra_singlMu = new TGraphAsymmErrors (h_pass_singlMu,h_total);
  gra_ElMu = new TGraphAsymmErrors (h_pass_ElMu,h_total);
  gra_Trig = new TGraphAsymmErrors (h_pass_Trig,h_total);

  mg->Add(gra_singlEl);
  mg->Add(gra_singlMu);
  mg->Add(gra_ElMu);
  mg->Add(gra_Trig);


  gra_singlEl->SetLineColor(1);
  gra_singlMu->SetLineColor(2);
  gra_ElMu->SetLineColor(3);
  gra_Trig->SetLineColor(4);

  gra_singlEl->SetMarkerStyle(20);
  gra_singlMu->SetMarkerStyle(20);
  gra_ElMu->SetMarkerStyle(20);
  gra_Trig->SetMarkerStyle(20);

  gra_singlEl->SetMarkerColor(1);
  gra_singlMu->SetMarkerColor(2);
  gra_ElMu->SetMarkerColor(3);
  gra_Trig->SetMarkerColor(4);


  mg->SetTitle(h_total->GetTitle());
  TCanvas *c = new TCanvas("c","",200,10,600,500);
 // TPad *pad1 = new TPad("pad1","pad1",0,0.2,1,1);
 //  pad1->SetBottomMargin(0.01);
//   pad1->SetLogy(0);
//   pad1->Draw();
//   pad1->cd();
  
  mg->Draw("APE");
  mg->SetMinimum(0.0);
  mg->SetMaximum(1.015);
  mg->GetXaxis()->SetTitle("eta1");
  mg->GetXaxis()->CenterTitle(1);
  mg->GetXaxis()->SetTitleOffset(1.2);
  mg->GetYaxis()->SetTitle("Trig Eff");
  mg->GetYaxis()->CenterTitle(1);
  mg->GetYaxis()->SetTitleOffset(1.4);

   TLegend *legend = new TLegend(0.5,0.1,0.7,0.3);
   legend->AddEntry(gra_singlEl,"SingleEle","p");
   legend->AddEntry(gra_singlMu,"SingleMu","p");
   legend->AddEntry(gra_ElMu,"E+Mu","p");
   legend->AddEntry(gra_Trig,"Comb","p");
   legend->Draw();

/*
  c->cd();
TH1F *h1 = (TH1F *)h_pass_2018A->Clone();
TH1F *h2 = (TH1F *)h_total_2018A->Clone();
   
h1->Divide(h2);
   
TH1F *h3 = (TH1F *)h_pass_2018B->Clone();
TH1F *h4 = (TH1F *)h_total_2018B->Clone();
  
h3->Divide(h4);
  
h3->Divide(h1);
  
TPad *pad2 = new TPad("pad2","pad2",0,0,1,0.2);
  pad2->SetGridy(1);
  pad2->SetPad(0,0.0,1.0,0.2);
  pad2->SetTopMargin(0.);
  pad2->SetBottomMargin(0.5);
  pad2->Draw();
  pad2->cd();
  float yscale = (1.0-0.2)/(0.18-0);

  h3->SetMarkerStyle(21);
  h3->SetStats(0);
  h3->GetYaxis()->SetTitle("");
  h3->SetMinimum(0.9);
  h3->SetMaximum(1.5);
  h3->SetTitle("");
  h3->GetXaxis()->SetTitle("");
  h3->GetXaxis()->SetTitleOffset(1.3);
  h3->GetXaxis()->SetLabelSize(0.033*yscale);
  h3->GetXaxis()->SetTitleSize(0.036*yscale);
  h3->GetXaxis()->SetTickLength(0.03*yscale);
  h3->GetYaxis()->SetTitleOffset(0.3);
  h3->GetYaxis()->SetNdivisions(5);
  h3->GetYaxis()->SetLabelSize(0.020*yscale);
  h3->GetYaxis()->SetTitleSize(0.036*yscale);
  h3->Draw("");

*/
//  TString pngFileName = trigger_name.Data() ;
//  pngFileName +=  "_efficiency.png";
  c->SaveAs("ggH_TriggerEff_Direct_eta1.png");
  c->Clear();

        delete c;

}// end of program
