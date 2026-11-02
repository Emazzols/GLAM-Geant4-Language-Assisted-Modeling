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

#include "DetectorConstruction.hh"

#include "G4Box.hh"
#include "G4Tubs.hh"
#include "G4Sphere.hh"
#include "G4Cons.hh"
#include "G4UnionSolid.hh"
#include "G4SubtractionSolid.hh"
#include "G4IntersectionSolid.hh"

#include "G4LogicalVolume.hh"
#include "G4PVPlacement.hh"
#include "G4NistManager.hh"
#include "G4SystemOfUnits.hh"

// =====================================================
// Geometric functions
// =====================================================

G4LogicalVolume* DetectorConstruction::BuildBox(const G4String& name, const G4ThreeVector& halfSize, G4Material* material) {
    auto solid = new G4Box(name, halfSize.x(), halfSize.y(), halfSize.z());
    return new G4LogicalVolume(solid, material, name + "LV");
}

G4LogicalVolume* DetectorConstruction::BuildCylinder(const G4String& name, G4double rMin, G4double rMax, G4double halfHeight, G4Material* material) {
    auto solid = new G4Tubs(name, rMin, rMax, halfHeight, 0.0, 360.0 * deg);
    return new G4LogicalVolume(solid, material, name + "LV");
}

G4LogicalVolume* DetectorConstruction::BuildSphere(const G4String& name, G4double radius, G4Material* material) {
    auto solid = new G4Sphere(name, 0.0, radius, 0.0, 360.0 * deg, 0.0, 180.0 * deg);
    return new G4LogicalVolume(solid, material, name + "LV");
}

G4LogicalVolume* DetectorConstruction::BuildCone(const G4String& name, G4double rMinBottom, G4double rMaxBottom, G4double rMinTop, G4double rMaxTop, G4double halfHeight, G4Material* material) {
    auto solid = new G4Cons(name, rMinBottom, rMaxBottom, rMinTop, rMaxTop, halfHeight, 0.0, 360.0 * deg);
    return new G4LogicalVolume(solid, material, name + "LV");
}

// =====================================================
// Boolean solids
// =====================================================

G4LogicalVolume* DetectorConstruction::BuildUnion(const G4String& name, G4VSolid* solidA, G4VSolid* solidB, const G4Transform3D& transformB, G4Material* material) {
    auto solid = new G4UnionSolid(name, solidA, solidB, transformB);
    return new G4LogicalVolume(solid, material, name + "LV");
}

G4LogicalVolume* DetectorConstruction::BuildSubtraction(const G4String& name, G4VSolid* solidA, G4VSolid* solidB, const G4Transform3D& transformB, G4Material* material) {
    auto solid = new G4SubtractionSolid(name, solidA, solidB, transformB);
    return new G4LogicalVolume(solid, material, name + "LV");
}

G4LogicalVolume* DetectorConstruction::BuildIntersection(const G4String& name, G4VSolid* solidA, G4VSolid* solidB, const G4Transform3D& transformB, G4Material* material) {
    auto solid = new G4IntersectionSolid(name, solidA, solidB, transformB);
    return new G4LogicalVolume(solid, material, name + "LV");
}

// =====================================================
// Geometric relations
// =====================================================

G4PVPlacement* DetectorConstruction::Place(G4LogicalVolume* child, G4LogicalVolume* mother, const G4ThreeVector& position, G4RotationMatrix* rotation, const G4String& name, G4int copyNo) {
    return new G4PVPlacement(rotation, position, child, name, mother, false, copyNo, true);
}

void DetectorConstruction::PlaceStacked(const std::vector<G4LogicalVolume*>& volumes, G4LogicalVolume* mother, const G4ThreeVector& axis, G4double spacing) {
    G4double offset = 0.0;

    for (size_t i = 0; i < volumes.size(); ++i) {
        auto lv = volumes[i];

        new G4PVPlacement(nullptr, axis.unit() * offset, lv, lv->GetName() + "PV", mother, false, i, true);

        offset += spacing;
    }
}

// =====================================================
// DetectorConstruction
// =====================================================

DetectorConstruction::DetectorConstruction() {}

G4VPhysicalVolume* DetectorConstruction::Construct() {

    auto nist = G4NistManager::Instance();

    // WORLD
    auto worldMat = nist->FindOrBuildMaterial("G4_AIR");
    auto worldLV = BuildBox("World", G4ThreeVector(1*m, 1*m, 1*m), worldMat);
    auto worldPV = new G4PVPlacement(nullptr,{}, worldLV,"WorldPV",nullptr,false,0,true);

    // EXAMPLE: sandwich
    // <INSTRUCTOR_GEOMETRY_BEGIN>
    // --- Geometry generated from IR ---
    auto WaterSphere = BuildSphere("WaterSphere", 5.0 * cm, nist->FindOrBuildMaterial("G4_WATER"));
    auto SiliconBox = BuildBox("SiliconBox", G4ThreeVector(1.0 * cm, 1.0 * cm, 1.0 * cm), nist->FindOrBuildMaterial("G4_Si"));
    Place(WaterSphere, worldLV, G4ThreeVector(0.0 * cm, 0.0 * cm, 0.0 * cm), nullptr, "WaterSpherePV", 0);
    Place(SiliconBox, worldLV, G4ThreeVector(0.0 * cm, 6.0 * cm, 0.0 * cm), nullptr, "SiliconBoxPV", 0);
// <INSTRUCTOR_GEOMETRY_END>

    return worldPV;
}

