# shapesplit
> \*\*\*POC\*\*\* A simple bpy addon that splits up a mesh's shapekeys into preset vertex group masks.

## Overview

**Currently a POC addon**: This tool is only a visualization at the moment and does not have functionality. Functionality will be added as I learn bpy!

This tool will do the following: 
* Take your current context object and creates new shape keys using a base shape key and masking it out using vertex groups. 
* The tool will then allow the user to bake each grouped vertex groups into the base shape keys to create new shape keys.

This is meant as a very quick and scalable implemenation of the slow and handsy 'vertex group masking shape key' bake workflow.

## Goals

- [x] Interface implementation
- [ ] Create unique presets within the interface controls (currently 3 different presets are hardcoded)
- [ ] Assign unique presets to each shape key
  - Currently only selects for all shape keys
- [ ] Bake functionality.
