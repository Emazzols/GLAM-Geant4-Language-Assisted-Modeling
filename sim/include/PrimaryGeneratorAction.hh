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

#pragma once

#include "G4VUserPrimaryGeneratorAction.hh"
#include "G4ThreeVector.hh"
#include "globals.hh"

// Forward declarations
class G4ParticleGun;
class G4Event;

// =====================================================
// Source type
// =====================================================

enum class SourceType {
    Point,
    Disk,
    Sphere
};

// =====================================================
// PrimaryGeneratorAction
// =====================================================

class PrimaryGeneratorAction : public G4VUserPrimaryGeneratorAction {
public:
    PrimaryGeneratorAction();
    ~PrimaryGeneratorAction() override;

    void GeneratePrimaries(G4Event* event) override;

    // -------------------------------------------------
    // Semantic configuration API
    // -------------------------------------------------

    void SetParticle(const G4String& name);

    void SetPointSource(const G4ThreeVector& position);

    void SetDiskSource(
        G4double radius,
        const G4ThreeVector& center
    );

    void SetSphereSource(
        G4double radius,
        const G4ThreeVector& center
    );

    void SetMonoEnergy(G4double energy);

    void SetDirectional(const G4ThreeVector& direction);

    void SetIsotropic();

private:
    // -------------------------------------------------
    // Internal state
    // -------------------------------------------------

    G4ParticleGun* fGun;

    SourceType    fSourceType;
    G4double      fEnergy;
    G4ThreeVector fPosition;
    G4ThreeVector fDirection;
    G4double      fRadius;
};
