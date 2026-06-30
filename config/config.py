"""
Project Configuration
Retail Lakehouse Platform
"""

# Root Project Folder
PROJECT_ROOT = "/content/drive/MyDrive/Retail_Lakehouse_Platform"

# Landing Zone
LANDING = f"{PROJECT_ROOT}/landing"

MASTER_DATA = f"{LANDING}/master_data"
TRANSACTION_DATA = f"{LANDING}/transactions"
REFERENCE_DATA = f"{LANDING}/reference"
STREAMING_DATA = f"{LANDING}/streaming"

# Medallion Architecture
BRONZE = f"{PROJECT_ROOT}/bronze"
SILVER = f"{PROJECT_ROOT}/silver"
GOLD = f"{PROJECT_ROOT}/gold"

# Other folders
LOGS = f"{PROJECT_ROOT}/logs"
AUDIT = f"{PROJECT_ROOT}/audit"
CHECKPOINTS = f"{PROJECT_ROOT}/checkpoints"
EXPORTS = f"{PROJECT_ROOT}/exports"
