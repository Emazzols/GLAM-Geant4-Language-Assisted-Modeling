//
// ********************************************************************
// * License and Disclaimer                                           *
// *                                                                  *
// * The  Geant4 software  is  copyright of the Copyright Holders  of *
// * the Geant4 Collaboration.  It is provided  under  the terms  and *
// * conditions of the Geant4 Software License,  included in the file *
// * LICENSE and available at  http://cern.ch/geant4/license .  These *
// * include a list of copyright holders.                             *
// *                                                                  *
// * Neither the authors of this software system, nor their employing *
// * institutes,nor the agencies providing financial support for this *
// * work  make  any representation or  warranty, express or implied, *
// * regarding  this  software system or assume any liability for its *
// * use.  Please see the license in the file  LICENSE  and URL above *
// * for the full disclaimer and the limitation of liability.         *
// *                                                                  *
// * This  code  implementation is the result of  the  scientific and *
// * technical work of the GEANT4 collaboration.                      *
// * By using,  copying,  modifying or  distributing the software (or *
// * any work based  on the software)  you  agree  to acknowledge its *
// * use  in  resulting  scientific  publications,  and indicate your *
// * acceptance of all terms of the Geant4 Software license.          *
// ********************************************************************
//
//
//
//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

#include "RunAction.hh"
#include <TFile.h>
#include <TTree.h>
#include <fstream>
#include <sys/stat.h>

// -----------------------------------------------------
// Constructor / Destructor
// -----------------------------------------------------

RunAction::RunAction()
: file(nullptr), tree(nullptr)
{
    std::ifstream in("sim_name.txt");
    if (in) {
        std::getline(in, simName);
        if (simName.empty()) {
            simName = "default";
        }
    } else {
        simName = "default";
    }
}

RunAction::~RunAction() {}

// -----------------------------------------------------
// Register observable volumes
// -----------------------------------------------------

void RunAction::RegisterObservable(const std::string& volumeName)
{
    fObservables.push_back(volumeName);
}

// -----------------------------------------------------
// Begin / End run
// -----------------------------------------------------

void RunAction::BeginOfRunAction(const G4Run*)
{
    mkdir("../results", 0777);

    std::string filepath = "../results/" + simName + ".root";
    file = new TFile(filepath.c_str(), "RECREATE");
    tree = new TTree("Edep", "Energy deposition per volume");

    // Create branches ONLY now (tree exists)
    for (const auto& name : fObservables) {
        fBranchValues[name] = 0.0;
        tree->Branch(name.c_str(), &fBranchValues[name]);
    }
}

void RunAction::EndOfRunAction(const G4Run*)
{
    if (file) {
        file->Write();
        file->Close();
    }
}

// -----------------------------------------------------
// Fill tree
// -----------------------------------------------------

void RunAction::FillEvent(const std::map<std::string, double>& values)
{
    // Reset all observables for the current event
    for (const auto& name : fObservables) {
        fBranchValues[name] = 0.0;
    }

    // Fill the observables that received energy deposition
    for (const auto& [name, val] : values) {
        fBranchValues[name] = val;
    }

    tree->Fill();
}


