# 🧱 Block-Based Python Database System

### 🔬 A Conceptual Prototype for Data Persistence Using Pickle Serialization and Block-Level Management

**Author:** Jermaine Samuels
**Institution:** University of the West Indies — MSc. Data Science
**Date:** 2021

---

## 🧩 Overview

This project presents a **Python-based lightweight database prototype** built entirely on **block storage principles** — illustrating how fundamental database mechanics such as **record management**, **block-level organization**, and **indexing** can be implemented from first principles using **Pickle serialization** and **object-oriented programming**.

The system mimics the structure and behavior of **low-level database engines**, introducing:

* **Block-level record grouping** (each block stores up to five records)
* **Data type enforcement and validation** at insertion
* **Indexed access** for accelerated updates
* **Persistent storage** through serialized binary files
* **In-memory row updates and index-aware writeback**

This prototype demonstrates how conceptual database theory can be concretized in code — providing a framework for understanding storage allocation, record lifecycle management, and efficient data retrieval at the block level.

---

## ⚙️ Core Architecture

### 🧱 **1. Record Layer**

Each `record` object represents a single database row.
It encapsulates column values and their insertion logic.

```python
class record:
    def __init__(self):
        self.row = []
    def cols(self, items):
        for i in items:
            self.row.append(i)
        return self.row
```

---

### 📦 **2. Block Layer**

The `block` class organizes multiple records into manageable units.
Each block can contain up to **five records**, enforcing data locality and simulating physical storage constraints.

```python
class block(record):
    def add_block(self, table):
        if len(table) == 1 or len(table[-1]) % 5 == 0:
            table.append([])
        return table
```

Blocks ensure that insertions occur only within empty or partially filled segments, preventing fragmentation and uncontrolled growth.

---

### 📁 **3. File Layer (Table)**

The `file` class represents a **table**, defined as a list of blocks, where:

* The **first element** stores column names and data types
* Subsequent elements store serialized blocks of records

```python
class file(block):
    def __init__(self, table_Name):
        self.col = []
        self.dtype = []
        self.table = []
```

Tables are persisted via **Pickle** and are identified by their filenames, serving as discrete binary “pages” on disk.

---

### 🧠 **4. Data Type Validation**

Before insertion, all new records are type-checked against declared column types to maintain structural integrity.
The `record_dtype_conversion()` and `check_dtype()` functions ensure compliance between input data and schema definitions.

---

### 🔍 **5. Indexing Layer**

The indexing system implements a **simple positional index** stored as a separate `_IDX` file.
Each index entry consists of:

```plaintext
[value, block_index, record_index]
```

Sorted lists of index tuples allow for **O(log n)**-like access time to records by key.

---

### 🧾 **6. Update Mechanism**

Two modes of record updating exist:

* **Unindexed Update:** Sequential search across all blocks
* **Indexed Update:** Targeted modification using the pre-built index for rapid access

This approach parallels hybrid **row-store index scanning** techniques found in production-grade relational systems.

---

## 🧮 Functional Highlights

| Function                                                  | Description                                             |
| --------------------------------------------------------- | ------------------------------------------------------- |
| `create_table(name, blockNum, fields)`                    | Creates a new table (Pickle file) with specified schema |
| `insert_rec(table, row_data)`                             | Inserts a record into available block space             |
| `create_index(column, table)`                             | Generates and stores a sorted column index              |
| `update_rec(table, set_info, set_key, col_info, col_key)` | Updates a record either via full-scan or index lookup   |
| `loadData1(table)`                                        | Loads and prints table content from Pickle              |
| `os.remove(table)`                                        | Deletes a table or index file                           |

---

## 🧪 Demonstration Example

```python
# Define schema
fields = ["id", "Name", "Adr", "int", "string", "string"]

# Create table
create_table('Epsom', 1, fields)
loadData1("Epsom")

# Insert sample data
insert_rec('Epsom', (8, 'Girl', 'Boy'))
insert_rec('Epsom', (5, 'Girl', 'Boy'))
insert_rec('Epsom', (3, 'Girl', 'Boy'))
insert_rec('Epsom', (4, 'Girl', 'Boy'))
insert_rec('Epsom', (2, 'Girl', 'Boy'))
insert_rec('Epsom', (6, 'Girl', 'Boy'))

# Create an index on 'id'
create_index('id', "Epsom")

# Perform an indexed update
update_rec('Epsom', 'Name', 'Shelly', 'id', 8)

# Delete table and index
os.remove("Epsom")
os.remove("Epsom_IDX")
```

---

## 🧠 Conceptual Insights

This project explores the **foundational design** of storage engines, specifically:

* How **records and blocks** relate to page-level structures
* How **indexes** can dramatically improve query efficiency
* How **data serialization** enables persistent storage without a traditional DBMS
* The tradeoffs between **fixed-block storage** and **dynamic allocation**

By implementing each component from scratch, the prototype demonstrates a **bottom-up understanding of database internals** — bridging computer science theory with practical implementation.

---

## 🚀 Potential Extensions

* 🧩 **Transaction logging** and recovery mechanisms
* 🔄 **Block compaction** and garbage collection
* 🗂️ **Multi-table relationships** with referential integrity
* 🧮 **Query parsing** for SQL-like command interpretation
* ☁️ **Remote persistence** via object storage (AWS S3 / Azure Blob)

---

## 💡 Key Takeaway

> *“True understanding of data systems comes not from using databases, but from building one.”*

This project serves as a **didactic model for understanding core database storage mechanics** — from **records and blocks to indexing and updates** — all implemented natively in Python with less than 400 lines of code.

---

## 👨🏾‍💻 Author

**Jermaine Samuels**
MSc. Data Science, University of the West Indies
📧 [jc.samuels21@gmail.com](mailto:jc.samuels21@gmail.com)
🔗 [GitHub Portfolio](https://github.com/jjsammii)
