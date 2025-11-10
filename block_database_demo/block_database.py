import pickle
import json
import os

# Records should reference a block
# A row is considered empty if no column has data
# A file contains blocks
# When a user creates database a folder should be created
# Folders should contain files which are tables
# A block should only contain 5 records
# insertions should only be done in empty block spaces
# columns names within tables should specifiy list index
# Consider using a block header for column names
# The data types of each column must be considered


class record:
  def __init__(self):
    self.row = []       #initializes a record
    
    
  def cols(self, items):
    for i in items:
        self.row.append(i)
    return self.row                #creates a row 
    
    
class block(record):
  def __init__(self):
     self.blocks = []        #initializes a block

  def add_block(self, table):
    self.table = table[-1]                 #self.table is the records within a table
    self.tablef = table                    #self.tablef is the entire table including header
    if len(self.tablef) == 1:              
        self.tablef.append(self.blocks)             #if the table only contains the header begin a block
    elif len(self.table) % 5 == 0:       
        self.tablef.append(self.blocks)             #if there exists 5 records in a block start a new block
    else:
        self.tablef
    return self.tablef                    #return resulting table
 

       
        
class file(block):                                   #A file is stnonymous to a table
  def __init__ (self, table_Name):                   #Initialize a table with empty columns, table values, table datatype
    self.col = []
    self.dtype = []
    self.table = []
    self.table_Name = table_Name
    
    

  def table_str(self, fieldNames):                  #The table_str denotes table format (using list of lists)
    for i in fieldNames[0:3]:
        self.col.append(i)
    for i in fieldNames[3:6]:
        self.dtype.append(i)
    self.table = [[self.col, self.dtype]]           #Table format is the column names followed by data types
    return self.table
  

   #def table_str(self, table):
        #return pass


def create_table(table_Name, blockNum, fieldNames):    #fieldNames should be a list
	# initializing data to store
    if os.path.exists(table_Name):                     #If table already created inform user
        print("Table Already Exist")
    else:
        c = file(table_Name)                           #invoke table structure
        c1 = c.table_str(fieldNames)                   #Assign table col names and dtypes

        # NB: the use of binary mode 
        savedfile = open(table_Name, 'ab')             #open pickle file

        # source, destination 
        pickle.dump(c1, savedfile)		       #save result to pickle file			 
        savedfile.close()
    
    
def loadData1(table_Name): 
    # for reading also binary mode is important 
    savedfile = open(table_Name, 'rb')	               #open file in pickle version
    r1 = pickle.load(savedfile) 
    print(r1)                                          #print results in pickle file
    savedfile.close()
    
def record_dtype_conversion(record_dtype):             #function to identify data types being entered within table
    record_vals = []
    for i in record_dtype:
        if type(i)== int:
            record_vals.append('int')                  #if dtype is in append int to list
        elif type(i) == str:
            record_vals.append('String')               #if dtype is str append str to list
    return record_vals

def check_dtype(tbl_data_type , record_dtype):         #compare tow lists
    t_data = []
    r_data = []
    for types in tbl_data_type:
        t_data.append(types.lower())
    r_dtype = record_dtype_conversion(record_dtype)
    for r_types in r_dtype:
        r_data.append(r_types.lower())
    if t_data == r_data:                               #if the dtype in table is the same as new input row
        return True                                    #Then record is allowed to be appended to existing table
    else:
        print("Incorrect Input Data Type")
    
def insert_rec(table, row_data):    
    if os.path.exists(table):                              #Checking if table exist as a pickle file         
        with open(table,'rb') as savedfile:                #open pickle file if table exists
            existing_rec = pickle.load(savedfile)                
        table_dtype = existing_rec[0][1]                   #extracts data type from existing table   
        if check_dtype(table_dtype, row_data):             #Perform comparison between new record and table dtype       
            r = record()
            new_rec = r.cols(row_data)                     #use the class to determine record structure which is three columns
            b = block()
            new = b.add_block(existing_rec)                #Use block to verify what block record must be inserted in
            existing_rec[-1].append(new_rec)               #Append new record to lists
            print(existing_rec)
            with open(table, 'wb') as savedfile:
                pickle.dump(existing_rec, savedfile)       #Load result to picke file
        savedfile.close()
    else:
        print(table, "Table/directory does not exist")     #If table doesnt exist

def create_index(col, table):
    name = os.path.basename(table)                         #create a variable that identies table name
    index_file_name = name+'_IDX'                          #if it does exist rename a list to include the table name + _IDX
    index_data = []
    if os.path.exists(table):                             #if the table exists
        # "with" statements are very handy for opening files. 
        with open(table,'rb') as savedfile:               
            existing_rec = pickle.load(savedfile)         
        val_pos = existing_rec[0][0].index(col)           #find the index for the column that should be indexed
        values = existing_rec[1:]                         #specify records position
        for i in values:        
            x = values.index(i)                           #find the index for the blocks
            for j in i:
                val = j[val_pos]                          #extract the value of the indexed column
                y = i.index(j)                            # find the index for the records          
                data = [val, x, y]
                index_data.append(data)                   #create a list of list consisting of the val of the index(id), the block index and the row index 
                index_data = sorted(index_data, key=lambda z: z[0])  #sorting index for easy retrieval
        savedfile = open(index_file_name, 'ab') 	
        # source, destination 
        pickle.dump(index_data, savedfile)	          #save result as a pickle file				 
        savedfile.close()    
        return index_data #resulting list first position is the col value, second is the main table index followed by sub index
        
#lst this is the list including the header
#set_info this is col that should be updated
#set_key this is the new value we will add
#col_info = the name of the column that has the search key
#col_key = the value to search for within the column
def rowupdater(lst, set_info, set_key, col_info, col_key):    
    set_loci = lst[0][0].index(set_info)                 
    col_loci = lst[0][0].index(col_info)
    lst1 = lst[1:]    
    for ind, blk in enumerate(lst1):                     #extract the index and the value from list of records
            new_lst1 = []
            for i in blk:
                if i[col_loci] == col_key:               #if a record key contains the search key replace the set column
                    i[set_loci] = set_key                #updating set column
                    new_lst1.append(i)                    
                else:
                    new_lst1.append(i)                  #if the record does not match search key append recordw without adjustment
            lst1[ind] = [new_lst1]
            #print(lst1)
            new = [lst[0]] + lst1                       #creation of new list
    return new


#indx version of row updater
def rowupdater_indx(table, lst, set_info, set_key, col_info, col_key): #same as above
    name = os.path.basename(table)    
    index_file_name = name+'_IDX'
    with open(index_file_name,'rb') as idx: 
            indx = pickle.load(idx)
    set_loci = lst[0][0].index(set_info)    
    col_loci = lst[0][0].index(col_info)
    lst1 = lst[1:]
    for i in indx:
        #print(i)        
        for ind, blk in enumerate(lst1):
            flst = []
            for j in blk:            
                if i[0] == col_key and i[0] == j[0]:         #using indexes to locate columns instead of searching every row             
                    a = i[1]
                    b = i[2]                
                    val = lst1[a][b]                
                    val[set_loci] = set_key
                    flst.append(val)                
                else:                
                    flst.append(j)        
    lst1[ind] = flst        
    new = [lst[0]] + lst1    
    return new  
 

#set_info this is col that should be updated
#set_key this is the new value we will add
#col_info = the name of the column that has the search key
#col_key = the value to search for within the column
def update_rec(table, set_info, set_key, col_info, col_key):
    name = os.path.basename(table)    
    index_file_name = name+'_IDX'                         #initializing table name to include _IDX
    if not os.path.exists(index_file_name):               #if there does not exists an indexed file existing pickle files will use rowupdater
        with open(table,'rb') as savedfile: 
            existing_rec = pickle.load(savedfile)            
            new_recs = rowupdater(existing_rec, set_info, set_key, col_info, col_key) #invokes unindexed function to update records
            print(new_recs)
            with open(table, 'wb') as savedfile:
                pickle.dump(new_recs, savedfile)
        savedfile.close()
    else:        
        with open(table,'rb') as savedfile: 
            existing_rec = pickle.load(savedfile)
            new_recs = rowupdater_indx(table, existing_rec, set_info, set_key, col_info, col_key) #invokes indexed function to update records
            print(new_recs)
            with open(table, 'wb') as savedfile:
                pickle.dump(new_recs, savedfile)
        savedfile.close()

#how to create a table
fields = ["id", "Name", "Adr","int", "string", "string"]
create_table('Epsom', 1, fields)
loadData1("Epsom")

#how to insert a new record
data = (1, 2, 'Boy')
data1 = (8, 'Girl', 'Boy')
data2 = (5, 'Girl', 'Boy')
data3 = (3, 'Girl', 'Boy')
data4 = (4, 'Girl', 'Boy')
data5 = (2, 'Girl', 'Boy')
data6 = (6, 'Girl', 'Boy')
data7 = (7, 'Girl', 'Boy')
data8 = (1, 'Girl', 'Boy')
insert_rec('Epsom', data1)
insert_rec('Epsom', data2)
insert_rec('Epsom', data3)
insert_rec('Epsom', data4)
insert_rec('Epsom', data5)
insert_rec('Epsom', data6)
insert_rec('Epsom', data7)
insert_rec('Epsom', data8)
loadData1("Epsom")

#how to load data
insert_rec('Epsom', data)
loadData1("Epsom")

#how to create index
create_index('id', "Epsom") 

#Epsom is table name
#Name is the column that should be updated
#id is the key to find the row to update
#8 is the exact id for the person whose name should be updated
#eg: UPDATE Epsom SET Name= ‘Shelly’ WHERE id=8;
update_rec('Epsom', 'Name', 'Shelly', 'id', 8) #note if index exists then update function will use index access

#Delete a table
os.remove("Epsom")

#Delete Index
os.remove("Epsom_IDX")
        