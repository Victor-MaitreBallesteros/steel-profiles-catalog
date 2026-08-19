# Steel Profiles Catalog (`steel-profiles-catalog`)



`steel-profiles-catalog` is a Python package for structural engineers. It provides a digital catalog of steel profiles (IPE, HEA, and HEB ranges) including their basic geometric dimensions.

The package stores pre-calculated data in an internal dictionary (O(1)), allowing queries with no disk-read latency and avoiding the need for real-time finite element meshing.

## How It Works
* The data_generator.py script takes the basic characteristics of the profiles as input (extracted from the ArcelorMittal catalog) and outputs data.py, which acts as the library containing all the data.
  * The program uses the sectionproperties library to calculate the cross-sectional area and moments of inertia.
* The catalog.py script takes data.py as input and builds the dictionary.
* As a result, you can simply import the package and query the name of the desired profile to retrieve its characteristics for use in your code.

---

## 📂 Project Structure

```text
steel-profiles-catalog/
│
├── pyproject.toml
└── steel_profiles/
    ├── __init__.py
    ├── catalog.py
    └── data.py
