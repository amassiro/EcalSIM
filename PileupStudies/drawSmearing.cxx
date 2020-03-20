


void drawSmearing(std::string var, int nbin, float min, float max, std::string cut = "1") {
  
  std::cout << " var = " << var << std::endl;
  
  std::vector< std::pair < int, std::string> > file_list;
  
  file_list.push_back(std::pair<int, std::string> (  0,  "test.0perc.root" ) );
  file_list.push_back(std::pair<int, std::string> ( 10, "test.10perc.root" ) );
  file_list.push_back(std::pair<int, std::string> ( 20, "test.20perc.root" ) );
  file_list.push_back(std::pair<int, std::string> ( 50, "test.50perc.root" ) );
  file_list.push_back(std::pair<int, std::string> ( 70, "test.70perc.root" ) );
  
  std::vector<TH1F> histos;
  
  for (int ifile=0; ifile<file_list.size(); ifile++) {

    TString name   = Form ("h_%d", file_list.at(ifile).first);
    TString nameHR = Form ("%d perc", file_list.at(ifile).first);
    TH1F histo (name.Data(),nameHR.Data(),nbin,min,max);
    
    TFile *file0 = TFile::Open( file_list.at(ifile).second.c_str() );
    TTree* myTree = (TTree*) file0 -> Get("TreeProducer/tree");
    TString name = Form ("h_%d", file_list.at(ifile).first);
    TString toDraw = Form ("%s >> %s", var.c_str(), name.Data());
    
    std::cout << " toDraw = " << toDraw.Data() << std::endl;
    
    myTree->Draw(toDraw.Data(), ( std::string("(") + cut + std::string(")") ).c_str(),"goff");
//     float normalization_0 = h_0 -> Integral(-1,-1);
//     h_0->Scale(1./normalization_0);
  
    histos.push_back(histo);
    
  }
  
  
  TCanvas* cc = new TCanvas ("cc", "", 800, 600);
  
  for (int ifile=0; ifile<file_list.size(); ifile++) {
  
    if (ifile==0) histos.at(ifile).Draw();
    else          histos.at(ifile).Draw("same");
  
    std::cout << " histos.at(ifile).GetEntries () = " << histos.at(ifile).GetEntries () << std::endl;
    
  }
  
 
 /* //---- plot
  h_0->SetLineColor(kRed);
  
  h_0->SetLineWidth(2);
  
  h_0->Draw();
 */ 
  //   gPad->SetLogy();
  gPad->SetGrid();
  
}
