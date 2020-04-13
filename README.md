Tools for researching the internals of Animal Crossing: New Horizons. More to come later...

## Licensing/Usage

Documentation and code here (except where specified) is (c) 2020 Ash Wolf ("Ninji"), and available under the GNU General Public License 3.0 as provided in the LICENSE file.

Feel free to build upon the tools here and release anything you discover, but please link back to me if you do - here on GitHub, or [@_Ninji](https://twitter.com/_Ninji) on Twitter!

## Update notes

- No BCSV changes in v1.1.2

## General Tools

### debug\_tools.py + pynoexs.py

Basic Python port of the Noexes client for poking the game's memory on a running Switch: https://github.com/mdbell/Noexes

## BCSVs (Binary CSV data tables)

### bcsv.py

Minimal library for reading AC:NH's binary CSV files.

### specs.py

Auto-generated specifications (using build\_specs.py and the enumerations JSON) for the BCSV schema. Most names are missing right now...

### dump\_all\_to\_html.py

Outputs a batch of HTML files containing crude table views of all the BCSV files.

## Message Data

### msbt.py

Minimal library for reading the MSBT format used inside the game's message archives.

### scrape\_item\_names.py

Dumps the names of all items to item\_names.json.

## Island Map Data

### pbc.py

Minimal library for reading AC:NH's collision and heightmap files.

### display\_pbc.py

Crudely renders the contents of a single PBC file to a PNG using Pillow.

### render\_map.py

Renders a map from a decrypted savefile, using the collision data as a source for the layout data (because the actual maps in the game are based off the 3D geometry, and I'm not writing a BFRES renderer). Pretty incomplete at the moment. Depends on `zstandard`, `sarc` and Pillow.

### render\_mystery\_island.py

Generates the data for my famed Mystery Tour Island guide.

## EventFlow

### evfl/eventflow\_actor\_info.json

A list of every single EventFlow action/query that gets called in the game's EventFlow files.

### evfl/eventflow\_vtables.json

Addresses in v1.1.4 for the vtables for all EventFlow actions/queries.

## Savefiles

### savefile/parse\_smmh.py

Parses the schema files present in /System/Smmh/ on the game's RomFS (except for v1.0.0!) and outputs information.

### savefile/dump\_save\_io\_structs.py

Talks to a Switch running ACNH under Noexs to extract information about the SaveIO class hierarchy that the game uses when accessing savefile data.

### savefile/all\_save\_field\_keys.json

A list of all hashes present for type and field names in the savefile schema.

### savefile/save\_keys.json

A manually curated list of field names. May contain a couple of inaccuracies due to hash collisions, but I've tried to eliminate as many as possible!

### savefile/bruteforce\_save\_fields3.py

Various strategies for trying to figure out as many of the hashes as possible.

### savefile/save\_io\_structure.json

Pre-generated SaveIO structure for v1.1.4.

### savefile/save\_schema\_*.json

Pre-generated schemas for the savefile format, including original type/field names from save\_keys.json.

### savefile/save\_schema\_*\_pseudoC.h

Vaguely readable pseudo-C output. Not usable in its direct form due to missing information on types not included in the schema (primitive types that haven't been figured out, Switch SDK stuff, etc).

## Ghidra Scripts

### ACEnumScraper2.py

Analyses the game's executable to find all the enumerations used in BCSV files (which helpfully come with both English names and Japanese descriptions) and generates a JSON file containing them.

### ACNHSaveSchemaV3.py

Imports all the structures from the savefile schema into a Ghidra database.

### FunHelper.py

Various things I used while analysing the v1.1.4 executable to make it more amenable to reverse-engineering in Ghidra (forcing all functions to be discovered, etc).

### BuildRTTIHierarchy.py

Introspects the RTTI information for a class to build out the inheritance chain and name all of the vtables and their methods. Slightly limited, right now it's specialised towards the EventFlow receptors.

### IntrospectBCSVs.py

An older version of the RTTI code specialised towards the classes that read BCSV files.

# Other helpful projects/tools

- SARC file handling: https://github.com/zeldamods/sarc
- EventFlow file handling: https://github.com/zeldamods/evfl
- Savefile mods (including encryption/decryption): https://github.com/Cuyler36/MyHorizons
- On-console debugger that works with ACNH (for poking memory, etc): https://github.com/mdbell/Noexes
