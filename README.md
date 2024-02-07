Assembly STL
================================================================================
# Motivation
The CFD mesher snappyHexMesh has the option for handle regions inside a triSurfaceMesh. These 
regions can be treated as patches for the case settings, but require that the different blocks 
form a water-tight geometry. 

Different CAD software can export STL files, but the transformation from CAD format to STL may lead
to issues with the volume confinement. Thus this global STL Mesh has a later tratment in Blender, to
separate the patches. However, the STL export capabilities of Blender are limited, and neither
multiblock nor custom block naming is achievable.

# Description
This software assembly different single-block STL files into a one multi-block STL file, with the
name of each block renamed accordingly to the filename.

# Usage
The program may use a prefix of the filename, which will be removed when transferring the
information to the block name.
```bash
assembly-stl.py part/*.stl --output multi-part.stl --prefix "solid"
```

# Instalation

