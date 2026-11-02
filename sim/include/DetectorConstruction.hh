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

#include "G4VUserDetectorConstruction.hh"
#include "globals.hh"

#include "G4ThreeVector.hh"
#include "G4RotationMatrix.hh"
#include "G4LogicalVolume.hh"
#include "G4PVPlacement.hh"
#include "G4Transform3D.hh"

#include <vector>

// Forward declarations
class G4LogicalVolume;
class G4VPhysicalVolume;
class G4Material;
class G4VSolid;

/**
 * DetectorConstruction
 *
 * Defines the detector geometry using a restricted
 * and composable set of primitives and placement rules.
 */
class DetectorConstruction : public G4VUserDetectorConstruction {
public:
    DetectorConstruction();
    virtual ~DetectorConstruction() = default;

    // Geant4 entry point
    virtual G4VPhysicalVolume* Construct() override;

private:
    // =====================================================
    // Geometric primitives
    // =====================================================

    // Box
    G4LogicalVolume* BuildBox(const G4String& name, const G4ThreeVector& halfSize, G4Material* material);

    // Cylinder (solid or hollow)
    G4LogicalVolume* BuildCylinder(const G4String& name, G4double rMin, G4double rMax, G4double halfHeight, G4Material* material);

    // Sphere (solid)
    G4LogicalVolume* BuildSphere(const G4String& name, G4double radius, G4Material* material);

    // Cone / frustum (solid or hollow)
    G4LogicalVolume* BuildCone(const G4String& name, G4double rMinBottom, G4double rMaxBottom, G4double rMinTop, G4double rMaxTop, G4double halfHeight, G4Material* material);

    // =====================================================
    // Boolean solids
    // =====================================================

    G4LogicalVolume* BuildUnion(const G4String& name, G4VSolid* solidA, G4VSolid* solidB, const G4Transform3D& transformB, G4Material* material);

    G4LogicalVolume* BuildSubtraction(const G4String& name, G4VSolid* solidA, G4VSolid* solidB, const G4Transform3D& transformB, G4Material* material);

    G4LogicalVolume* BuildIntersection(const G4String& name, G4VSolid* solidA, G4VSolid* solidB, const G4Transform3D& transformB, G4Material* material);

    // =====================================================
    // Placement relations
    // =====================================================

    // Generic placement with position and rotation
    G4PVPlacement* Place(G4LogicalVolume* child, G4LogicalVolume* mother, const G4ThreeVector& position, G4RotationMatrix* rotation, const G4String& name, G4int copyNo = 0);

    // Stack volumes along an axis
    void PlaceStacked(const std::vector<G4LogicalVolume*>& volumes, G4LogicalVolume* mother, const G4ThreeVector& axis, G4double spacing = 0.0);
    
};
