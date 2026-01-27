import pandas as pd

# These columns must exist in the uploaded CSV
REQUIRED_COLUMNS = ["Equipment Name", "Type", "Flowrate", "Pressure", "Temperature"]


def analyze_csv(file_path):
    """
    Reads a CSV file containing chemical equipment data,
    performs analysis, and returns a summary dictionary.
    """

    # 1. Try reading the CSV file
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        return {
            "status": "error",
            "message": f"File could not be read: {str(e)}"
        }

    # 2. Validate required columns
    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            return {
                "status": "error",
                "message": f"Missing required column: {col}"
            }

    # 3. Remove rows with missing numeric values
    df = df.dropna(subset=["Flowrate", "Pressure", "Temperature"])

    # 4. Perform analysis
    try:
        result = {
            "status": "success",
            "total_equipment": int(len(df)),
            "avg_flowrate": float(df["Flowrate"].mean()),
            "avg_pressure": float(df["Pressure"].mean()),
            "avg_temperature": float(df["Temperature"].mean()),
            "type_distribution": df["Type"].value_counts().to_dict()
        }

        return result

    except Exception as e:
        return {
            "status": "error",
            "message": f"Data processing failed: {str(e)}"
        }
