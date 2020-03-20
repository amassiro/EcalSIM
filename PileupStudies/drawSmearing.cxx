


void drawSmearing(std::string var, int nbin, float min, float max, std::string cut = "1") {
  
  std::cout << " var = " << var << std::endl;
  std::cout << " nbin,min,max = " << nbin << " , " << min<< " , " << max << std::endl;
  
  std::vector< std::pair < int, std::string> > file_list;
  
  file_list.push_back(std::pair<int, std::string> (  0,  "test.0perc.root" ) );
  file_list.push_back(std::pair<int, std::string> ( 10, "test.10perc.root" ) );
  file_list.push_back(std::pair<int, std::string> ( 20, "test.20perc.root" ) );
  file_list.push_back(std::pair<int, std::string> ( 50, "test.50perc.root" ) );
  file_list.push_back(std::pair<int, std::string> ( 70, "test.70perc.root" ) );
  
  TH1F* histos[file_list.size()];
  TFile* files[file_list.size()];

  for (int ifile=0; ifile<file_list.size(); ifile++) {
    TString name   = Form ("h_%d", file_list.at(ifile).first);
    TString nameHR = Form ("%d perc", file_list.at(ifile).first);
    histos[ifile] = new TH1F(name.Data(), nameHR.Data(), nbin, min, max );
    files[ifile] = new TFile( file_list.at(ifile).second.c_str(), "READ" );
  }
  
  
  for (int ifile=0; ifile<file_list.size(); ifile++) {

    std::cout << " --- " << std::endl;
    
    TString name   = Form ("h_%d", file_list.at(ifile).first);
    TString nameHR = Form ("%d perc", file_list.at(ifile).first);
    TH1F* histo_temp = new TH1F("TEST", "", nbin, min, max );
      
    TTree* myTree = (TTree*) files[ifile] -> Get("TreeProducer/tree");
    TString toDraw = Form ("%s >> TEST", var.c_str());
    TString toCut  = Form ("(%s)", cut.c_str());
    
    std::cout << " ttree GetEntries = " << myTree->GetEntries() << std::endl;
    std::cout << " toDraw = " << toDraw.Data() << std::endl;
    std::cout << " toCut = "  <<  toCut.Data() << std::endl;
        
//     myTree->Draw(toDraw.Data(), toCut.Data(), "goff");
    myTree->Draw(toDraw.Data(), toCut.Data(), "");
    
    std::cout << " TEST->GetEntries () = " << histo_temp->GetEntries () << std::endl;
    
    histos[ifile]->Add(histo_temp);
    
    std::cout << " histos[ifile]->GetEntries () = " << histos[ifile]->GetEntries () << std::endl;

  }
  
  std::cout << " --------- " << std::endl;
  
  TCanvas* cc = new TCanvas ("cc", "", 800, 600);
  
  for (int ifile=0; ifile<file_list.size(); ifile++) {
  
    if (ifile==0) histos[ifile]->Draw();
    else          histos[ifile]->Draw("same");
  
    std::cout << " histos[ifile]->GetEntries () = " << histos[ifile]->GetEntries () << std::endl;
    
  }
  

  
  
  //     float normalization_0 = h_0 -> Integral(-1,-1);
  //     h_0->Scale(1./normalization_0);  
  
 /* //---- plot
  h_0->SetLineColor(kRed);
  
  h_0->SetLineWidth(2);
  
  h_0->Draw();
 */ 
  //   gPad->SetLogy();
  
  gPad->SetGrid();
  
}



