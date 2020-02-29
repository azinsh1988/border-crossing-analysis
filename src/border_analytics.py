def myOpenCSV(csv_file_directory, date_index=4):
    
    with open(csv_file_directory, 'r') as f:
        #read the csv file line by line
        lines = [line.rstrip().split(",") for line in f]
        
        # remove the header
        header = lines[0]
        
        # skip the header by starting from index 1
        results = lines[1:]
        
        
        # sort the results based on date
        results.sort(key=lambda x: x[date_index][6:10]+x[date_index][0:2])
        print("Data is ready for analysis.")
        return header,results

def myGroupBy(lst, date_index=4, border_index=3, measure_index=5, value_index=6):
    print("Groupby date borde and measure ...")
            
    border_date_measure_MAP = {}
    border_measure_MAP = {}
    starting_month = int(lst[0][date_index][:2])
    starting_year = int(lst[0][date_index][6:10])
    
    for row in lst:
        date = row[date_index]
        month = int(date[:2])
        year = int(date[6:10])
        
        border = row[border_index]
        measure = row[measure_index]
        
        value = int(row[value_index])
        
        key1 = border+"_"+date+"_"+measure
        key2 = border+"_"+measure
        
        l = (year-starting_year)*12+(month-starting_month) 
        l = l if l!=0 else 1
        
        if key1 in border_date_measure_MAP:
            border_date_measure_MAP[key1][0]+=value
        else:
            run_ave = border_measure_MAP.get(key2, 0)/l
            border_date_measure_MAP[key1] = [value, (int(run_ave)+1, int(run_ave))[run_ave%1<0.5]]
        
        
        border_measure_MAP[key2] = border_measure_MAP.get(key2, 0)+value
    print("Groupby is done.")

    return border_date_measure_MAP

def MyDicToList(dic, border_index=0, date_index=1, measure_index=2, value_index=3):
    print("Converting dic to list ...")
    res = []
    for k,v in dic.items():
        A = k.split("_")
        A+=v
        res+=A,
    res.sort(key = lambda x: (x[date_index][6:10]+x[date_index][:2],x[value_index],x[measure_index],x[border_index]), reverse = True)
    print("your results are ready.")
    return res

def MyToCSV(lst, location = "./output/report.csv", header = ["Border","Date","Measure","Value","Average"]):
    print("Writing to csv ...")
    lst = [header]+lst
    with open(location,'w') as file:
        for line in lst:
            for c in line[:-1]:
                file.write(str(c)+',')
            file.write(str(line[-1]))
            file.write('\n')
    print("Your CSV file is ready!")


if __name__ == '__main__':
    csv_file_directory = "./input/Border_Crossing_Entry_Data.csv"
    header,lst = myOpenCSV(csv_file_directory)
    MyToCSV(MyDicToList(myGroupBy(lst)))

