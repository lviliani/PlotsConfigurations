void plotEfficiencyV2(TString flav="em",TString var="eta1",TString sample="ggH_hww"){ 

TString dir = "rootFileV2";

TFile *f = TFile::Open(dir+"/plots_ggH2018_v7.root");

   TH1F *h_total;
   TH1F *h_pass_Trig;

  h_total = (TH1F*)f->Get("hww2l2v_13TeV_"+flav+"/"+var+"/histo_"+sample);
  h_pass_Trig = (TH1F*)f->Get("hww2l2v_13TeV_withTrig_"+flav+"/"+var+"/histo_"+sample);

  TMultiGraph *mg = new TMultiGraph();
  TGraphAsymmErrors *gra_Trig = new TGraphAsymmErrors();

  gra_Trig = new TGraphAsymmErrors (h_pass_Trig,h_total);

  mg->Add(gra_Trig);

  gra_Trig->SetLineColor(4);

  gra_Trig->SetMarkerStyle(20);

  gra_Trig->SetMarkerColor(4);

  mg->SetTitle(h_total->GetTitle());
  TCanvas *c = new TCanvas("c","",200,10,600,500);

  mg->Draw("APE");
  mg->SetMinimum(0.0);
  mg->SetMaximum(1.015);
  mg->GetXaxis()->SetTitle(sample+" "+var+" "+flav);
  mg->GetXaxis()->CenterTitle(1);
  mg->GetXaxis()->SetTitleOffset(1.2);
  mg->GetYaxis()->SetTitle("Trig Eff");
  mg->GetYaxis()->CenterTitle(1);
  mg->GetYaxis()->SetTitleOffset(1.4);

   TLegend *legend = new TLegend(0.5,0.1,0.8,0.3);
   legend->AddEntry(gra_Trig,"Comb","p");
   legend->Draw();

  c->Print("TriggerEff_Direct_"+flav+"_"+var+"_"+sample+".png");


}// end of program
