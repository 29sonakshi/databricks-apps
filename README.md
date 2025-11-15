# Databricks Streamlit Hello World App

A simple Streamlit app that displays "Hello World!" with an interactive button. Perfect for learning how to deploy Databricks Apps! Deploy this Databricks app and click the "Click me!" button to see magic.

![https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1](https://github.com/29sonakshi/databricks-apps/blob/main/src/streamlit%20app%20.png)

## What's Inside

This project contains:
- `src/app.py` - The Streamlit application code
- `src/requirements.txt` - Python dependencies (streamlit)
- `src/app.yaml` - Databricks app configuration

## Quick Start: Deploy via Databricks UI

**No CLI required!** Follow these steps to deploy the app through the Databricks web interface:

### Step 1: Upload Files to Databricks Workspace

1. Open your Databricks workspace in a web browser
2. Navigate to **Workspace** in the left sidebar
3. Go to your user folder: `Users` → `your.email@company.com`
4. Create a new folder:
   - Click the dropdown → **Create** → **Folder**
   - Name it: `streamlit-hello-world`
5. Upload all three files from the `src/` directory:
   - Click into the folder
   - Click **Create** → **File** → **Upload files**
   - Upload: `app.py`, `requirements.txt`, and `app.yaml`

### Step 2: Create the App

1. Click **Apps** in the left sidebar
2. Click **Create App**
3. Click **Create a custom app** 
5. Configure:
   - **App name**: `streamlit-hello-world`
   - **Compute**: Select Medium
6. Click **Create**
7. Your app's compute is active, but your app is not yet deployed.
8. After the app is create click **Deploy** and specify Source code path where you uploaded 3 files. 
9. Click **Deploy**

### Step 3: Access Your App

1. Wait 1-2 minutes for deployment (installing dependencies)
2. Once status shows "Running", click **Open App**
3. You should see "Hello World! 👋"
4. Click the "Click me!" button to see MAGIC! 

## Troubleshooting

**App shows "Not Available"?**
- Make sure all 3 files (`app.py`, `requirements.txt`, `app.yaml`) are in the same folder
- Check that the app status is "Running" (not "Starting" or "Failed")

**App exits unexpectedly?**
- Verify `requirements.txt` contains: `streamlit>=1.28.0`
- Ensure `app.yaml` is present in the folder
