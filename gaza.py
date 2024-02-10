import csv
import re 
# import re to retrive numbers from a string 
csv_file_path = 'unclean.csv'
output_file_path = 'cleaned.csv'
last_movie_titles = {} # to count frequency for less null duplicated
column_num_needed = None

# Read the header to retrive the number of column needed
with open(csv_file_path, 'r') as file:
    for line in file:
        if "column_num" in line:
            col_index = line.find(":")
            if col_index != -1:
                char_we_want = line[col_index + 2]
                column_num_needed = int(char_we_want)
            
            
        
#For the previous code we check line by line to find column_num in the header and retrive the number of it


# Read the csv data and reach the <data> ... ignore any don't needed data in the header
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    header_read = False
    for row in csv_reader:
        if not header_read:
            if "data" in row[0]:
                header_read = True
                
            continue
            
        # Adjusting the empty and duplicated rows with taking the consider of null values
    
        if row and not row[0].startswith('</data>') and any(field.strip() for field in row):
            # now in cleaned.csv we have only the info we want without any addition or the header
            # the row[0].startswith part was for ensure that the last line </data> will be removed
            movie_title = row[0].strip()
            if movie_title in last_movie_titles:
                # if it's already in the dict so we need to compare which one has less null values
                current_null_content = sum(1 for field in row if not field.strip()) 
                existing_row = last_movie_titles[movie_title]
                existing_null_count = sum(1 for field in existing_row if not field.strip()) 

                if current_null_content < existing_null_count:
                    last_movie_titles[movie_title] = row[:column_num_needed]
            else:
                last_movie_titles[movie_title] = row[:column_num_needed]
        
        # to convert every null value or " " into an "empty" string for every field in every row
         
    

# Write the cleaned data with the specified number of columns needed

with open(output_file_path, 'w' , newline = '') as output_file:
    csv_writer = csv.writer(output_file)

    # Write header with the specified number of columns needed
    

    for row in last_movie_titles.values():
        # Ensure the row has the specified number of columns
        
        # to convert every null value or " " into an "empty" string for every field in every row
        new_row = ['empty' if field == '' or field is None else int(field.strip('"')) if field.strip('"').isdigit() else field for field in row]
        csv_writer.writerow(new_row)

