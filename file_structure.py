 
import os

# Create the main project directory
project_name = "real_time_data_analysis_dashboard"
os.mkdir(project_name)

# Create subdirectories for data, analysis, and visualization
data_directory = os.path.join(project_name, "data")
os.mkdir(data_directory)

analysis_directory = os.path.join(project_name, "analysis")
os.mkdir(analysis_directory)

visualization_directory = os.path.join(project_name, "visualization")
os.mkdir(visualization_directory)

# Create empty files for the project
data_file = os.path.join(data_directory, "real_time_data.csv")
open(data_file, 'a').close()

analysis_file = os.path.join(analysis_directory, "real_time_analysis.py")
open(analysis_file, 'a').close()

visualization_file = os.path.join(visualization_directory, "real_time_visualization.py")
open(visualization_file, 'a').close()

# Print confirmation message
print("Project file structure has been created successfully!")
