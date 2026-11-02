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

#include "PrimaryGeneratorAction.hh"

#include "G4ParticleGun.hh"
#include "G4ParticleTable.hh"
#include "G4Event.hh"
#include "G4SystemOfUnits.hh"
#include "G4RandomDirection.hh"
#include "Randomize.hh"

// =====================================================
// Constructor / Destructor
// =====================================================

PrimaryGeneratorAction::PrimaryGeneratorAction()
: fGun(new G4ParticleGun(1)),   
  fSourceType(SourceType::Point), 
  fEnergy(0.0 * MeV),             
  fPosition(G4ThreeVector()),     
  fDirection(G4ThreeVector()),   
  fRadius(0.0)                   
{

}

PrimaryGeneratorAction::~PrimaryGeneratorAction() {
    delete fGun; 
}

// =====================================================
// Public configuration interface (semantic API)
// =====================================================

void PrimaryGeneratorAction::SetParticle(const G4String& name) {
    auto particle =
        G4ParticleTable::GetParticleTable()->FindParticle(name);

    if (!particle) {
        G4Exception(
            "PrimaryGeneratorAction::SetParticle",
            "InvalidParticle",
            FatalException,
            "Unknown particle name"
        );
    }

    fGun->SetParticleDefinition(particle);
}

void PrimaryGeneratorAction::SetPointSource(
    const G4ThreeVector& position
) {
    fSourceType = SourceType::Point;
    fPosition   = position;
}

void PrimaryGeneratorAction::SetDiskSource(
    G4double radius,
    const G4ThreeVector& center
) {
    fSourceType = SourceType::Disk;
    fRadius     = radius;
    fPosition   = center;
}

void PrimaryGeneratorAction::SetSphereSource(
    G4double radius,
    const G4ThreeVector& center
) {
    fSourceType = SourceType::Sphere;
    fRadius     = radius;
    fPosition   = center;
}

void PrimaryGeneratorAction::SetMonoEnergy(G4double energy) {
    fEnergy = energy;
}

void PrimaryGeneratorAction::SetDirectional(
    const G4ThreeVector& direction
) {
    fDirection = direction.unit();
}

void PrimaryGeneratorAction::SetIsotropic() {
    fDirection = G4ThreeVector(); // isotropic flag
}

// =====================================================
// Event generation
// =====================================================

void PrimaryGeneratorAction::GeneratePrimaries(G4Event* event) {

    // --- Energy
    fGun->SetParticleEnergy(fEnergy);

    // --- Position
    if (fSourceType == SourceType::Point) {
        fGun->SetParticlePosition(fPosition);
    }
    else if (fSourceType == SourceType::Disk) {
        G4double r   = std::sqrt(G4UniformRand()) * fRadius;
        G4double phi = 2.0 * CLHEP::pi * G4UniformRand();

        G4ThreeVector local(
            r * std::cos(phi),
            r * std::sin(phi),
            0.0
        );

        fGun->SetParticlePosition(fPosition + local);
    }
    else if (fSourceType == SourceType::Sphere) {
        G4double u = G4UniformRand();
        G4double r = fRadius * std::cbrt(u);   // uniform in volume

        G4ThreeVector local = G4RandomDirection() * r;
        fGun->SetParticlePosition(fPosition + local);
    }

    // --- Direction
    if (fDirection.mag() == 0.0) {
        fGun->SetParticleMomentumDirection(G4RandomDirection());
    }
    else {
        fGun->SetParticleMomentumDirection(fDirection);
    }

    fGun->GeneratePrimaryVertex(event);
}