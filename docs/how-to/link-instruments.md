# How to Link an Instrument to Your Measurement

Connecting your experimental data to the specific equipment used is a crucial step in the iEntrance NOMAD Oasis. By linking an instrument—ideally using its unique **FabLIMS ID**—you ensure your data is fully traceable and properly integrated with the central database.

Here is how to search for and link your instrument inside an Electronic Lab Notebook (ELN) entry.

### Step 1: Open Your Entry
After creating your specific measurement entry (such as a `pynxtools` schema, an FBK Characterization step, or a custom iEntrance schema), open the entry to view the ELN form.

### Step 2: Locate the Instrument Reference Field
Scroll through the form to find the instrument linking field. The exact name of this field depends on the plugin you are using:

* **For standard iEntrance & PyNXTools Schemas:** Look for the main **Instrument** reference section.
* **For FBK (Characterization & Fabrication) Schemas:** Scroll through the layout and look specifically for the **Linked instrument** search field. *(Note: You can safely ignore any manual inline equipment subsections provided by FBK, as long as you use this linked search bar).*

### Step 3: Search using the FabLIMS ID
1. Click on the reference search bar (or the **+** button next to the field, depending on the layout).
2. A search dialog or dropdown menu will appear.
3. Type your instrument's specific **FabLIMS ID** into the search bar. The NOMAD database will automatically fetch the matching equipment.

### Step 4: Select and Save
Click on the correct instrument from the search results to securely link it to your measurement. Finally, press the **Floppy Disk** icon at the top right of the page to save your entry.