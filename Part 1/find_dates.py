from pathlib import Path
from datetime import datetime

directory = 'C:\\Users\\mikef\\OneDrive\\Desktop\\Digital Earth Caribbean\\Dominica\\Training\\Training Materials\\intro\\earthquake_example'
dirobj=Path(directory).glob('*')

start_date = datetime(2023, 11, 1)
end_date = datetime(2023, 11, 26)  

for file in dirobj:
    
    date_str = file.stem.split('_')[2]
    date = datetime.strptime(date_str, '%Y-%m-%d')

    if date >= start_date and date <= end_date:
        print(file.stem)

       


