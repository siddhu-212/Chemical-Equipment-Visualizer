from analyzer import analyze_csv

# Path to the sample CSV file (same folder)
file_path = "sample_equipment_data.csv"

result = analyze_csv(file_path)

print("===== ANALYSIS RESULT =====")
print(result)
