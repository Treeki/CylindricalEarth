Tools for researching the internals of Animal Crossing: New Horizons. More to come later...

## Update notes

- No BCSV changes in v1.1.2

## Stuff in here

### bcsv.py

Minimal library for reading AC:NH's binary CSV files.

### ghidra_scripts/ACEnumScraper2.py

Analyses the game's executable to find all the enumerations used in BCSV files (which helpfully come with both English names and Japanese descriptions) and generates a JSON file containing them.

### specs.py

Auto-generated specifications (using build_specs.py and the enumerations JSON) for the BCSV schema. Most names are missing right now...

### pbc.py

Minimal library for reading AC:NH's collision and heightmap files.

### render_map.py

Renders a map from a decrypted savefile, using the collision data as a source for the layout data (because the actual maps in the game are based off the 3D geometry, and I'm not writing a BFRES renderer). Pretty incomplete at the moment. Depends on `zstandard`, `sarc` and Pillow.

### dump_all_to_html.py

Outputs a batch of HTML files containing crude table views of all the BCSV files.

## Other helpful projects/tools

- SARC file handling: https://github.com/zeldamods/sarc
- EventFlow file handling: https://github.com/zeldamods/evfl
- Savefile mods (including encryption/decryption): https://github.com/Cuyler36/MyHorizons
- On-console debugger that works with ACNH (for poking memory, etc): https://github.com/mdbell/Noexes
