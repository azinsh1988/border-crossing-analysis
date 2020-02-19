def srtByDate(csv_file_directory, date_index=0):
    with open(csv_file_directory, 'r') as f:
        #read from csv line by line, rstrip helps to remove '\n' at the end of line
        lines = [line.rstrip() for line in f] 

        results = []

        # skip the header by starting from index 1
        for line in lines[1:]:
            words = line.split(',') # get each item in one line
            date = words[date_index][1:-1] # remove ("") from date
            results.append([date] + words[:date_index] + words[date_index+1:])
        
        # sort the results based on date
        results.sort()
        return results
      
if __name__ == '__main__':
    try:
        srtByDate(input/Border_Crossing_Entry_Data.csv, date_index=0)

