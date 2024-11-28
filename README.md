# DeleteDataset

This repository provides an automation solution to delete datasets from **Azure Lake Storage Gen2** using **LogicApps** and **Python**.

Work better in a workflow from databricks ;) 

![image](https://github.com/user-attachments/assets/cdd6c13e-f52d-4d1e-9287-b493c81ab643)


## Overview

The `deletedataset` project automates the process of deleting datasets stored in Azure Data Lake Storage Gen2. This can help streamline data management workflows and improve operational efficiency.

## Features

- Integration with Azure LogicApps for workflow automation
- Python scripts for dataset deletion
- Customizable logic to target specific datasets

## Prerequisites

Before using this automation, ensure that you have:
- An active **Azure subscription**
- **Azure Data Lake Storage Gen2** set up
- Access to **Azure LogicApps** and **Python 3.x**

## Installation

To install the necessary components, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/olvriz/deletedataset.git
    ```

2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your **Azure LogicApp** based on the provided template in the repository.

## Usage

1. Customize the Python script to specify the datasets to be deleted.
2. Trigger the LogicApp to automate the deletion process.

Example:
```bash
python delete_datasets.py --dataset-name "example_dataset"
```

# How Python script for Azure Blob Deletion Automation works

This Python script automates the process of deleting blobs (files and directories) in **Azure Data Lake Storage**. It leverages **PySpark's DBUtils** and interacts with **webhooks** to send status updates.

## Features

- Recursively deletes files and directories in a specified Azure path.
- Sends success or error messages to a webhook URL.
- Uses parameters from **Azure Databricks widgets** for customizable execution.

## How It Works

1. **Delete Blobs**: Deletes files and directories at the specified path.
2. **Webhook Notification**: Sends status and metadata to a configured webhook.
3. **Error Handling**: Catches errors and sends error details via the webhook.

## Usage

1. Set up required widgets (e.g., `zona`, `pais`, `dominio`, etc.).
2. Provide the path (`caminho`) where blobs should be deleted.
3. Run the script in an Azure Databricks environment.

## Example

```python
# Set up widgets for dynamic input
zona = dbutils.widgets.get("zona")
caminho = dbutils.widgets.get("caminho")

# Start the deletion process
result = delete_blobs(caminho)

