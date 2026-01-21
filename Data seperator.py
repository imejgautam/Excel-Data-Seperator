import pandas as pd
import os

def split_precipitation_data(input_file, output_folder):
    # Define station names in order
    stations = ["Bhaktapur", "Godavari", "Khokana", "Khumaltar", "Panipokhari", "Sankhu", "Sundarijal"]
    
    # Create output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Read the Excel file
    df = pd.read_excel(input_file)
    
    # Rename columns to match station names
    df.columns = ["Date"] + stations
    
    # Convert Date column to proper datetime format (yyyy-mm-dd)
    df["Date"] = pd.to_datetime(df["Date"], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
    
    # Save each station's data into a separate Excel file in the specified output folder
    for station in stations:
        output_path = os.path.join(output_folder, f"{station}.xlsx")
        station_df = df[["Date", station]].rename(columns={station: "Precipitation(mm/day)"})
        station_df.to_excel(output_path, index=False)
        print(f"Saved: {output_path}")

# Example usage
input_file = "D:/College/7th Sem/Flood Modelling/Falgun+Chaitra/Bias Correction/Data for BC Software/Bias Corrected Files/mri/MRI.xlsx"  # Change this to your actual file path
output_folder = "D:/College/7th Sem/Flood Modelling/Falgun+Chaitra/Bias Correction/Data for BC Software/Bias Corrected Files/mri/"  # Change this to your desired output folder
split_precipitation_data(input_file, output_folder)