# How to Upload Instrument Data

This page provides a step-by-step guide for uploading instrument data to the iEntrance NOMAD Oasis.

## Step 1. Check the support matrix

Start with the local matrix: [Supported Instruments](../reference/supported-instruments.md)

Use this decision logic:

- If your format is listed and supported by a non-`pynxtools` plugin, NOMAD should recognize and parse it automatically. Upload your file directly (or a `.zip` with multiple files).
- If your format is listed and supported by a `pynxtools` plugin, follow Steps 2-3.
- If your format is not listed anywhere in the matrix, follow [How-to: Upload and share sample files](upload-and-share-sample-files.md) to request development support.

## Step 2. Prepare and upload your files

Collect the files required by the selected `pynxtools` reader into a `.zip` file. Depending on the reader, this can include:

- one or more raw measurement files
- optional metadata sidecars
- optional ELN/YAML metadata files
- optional reader configuration files

Organize each set of measurement files as one self-contained set: keep all raw files, sidecar metadata, ELN/YAML files, and conversion config for that measurement in the same folder (or subfolder tree), and avoid mixing files from different measurements.

Drag and drop your file or `.zip` to NOMAD under `PUBLISH > UPLOADS > CREATE A NEW UPLOAD`.

## Step 3. Convert to NeXus with DataConverter

**Using the GUI (primary approach)**

In your upload:

1. Click **Create from schema**.
2. Select **NexusDataConverter** as the built-in schema class, provide a name, and click **CREATE**.
3. Fill in the conversion form fields:
   - reader/plugin selection
   - input file references
   - NXDL target
   - output file name/path
4. Save the schema entry and run processing.
5. Confirm that the `.nxs` output file is created in the upload.

**Local conversion with CLI (optional)**

Install `pynxtools` first: [Installation guide](https://fairmat-nfdi.github.io/pynxtools/tutorial/installation.html)

```bash
dataconverter <input files...> <optional config> --reader <reader-name> --nxdl <NXDL-name> --output <output-file.nxs>
```

Before upload, verify that:

- conversion completed without fatal errors
- key metadata and measurement arrays are present
- warnings are understood and acceptable for your use case

If required information is missing, refine your metadata inputs and re-run conversion.

Then upload the generated `.nxs` file to NOMAD.

## Further guidance

For NOMAD upload behavior and `pynxtools` conversion details, see:

- [NOMAD: Upload experimental data](https://nomad-lab.eu/prod/v1/docs/tutorial/upload_publish.html#upload-experimental-data)
- [pynxtools documentation](https://fairmat-nfdi.github.io/pynxtools/)
