# PYTHON FOR DATASCIENCE

""" __summary__
NumPy; Numeric computations in python. Enables working with arrays
Pandas; functionalities: Data cleaning, Transformation, merging, filtering

Data Visualisation
Deals with Plotting -- use matplotlib or seaborn library to create - line, scatter, bar, histogram, heatmaps, etc

Key Concept in Data Science
Data - (text, images, videos) or semi-structured data (JSON, XML)
Data Mining 
Machine Learning
Statistical Analysis
Data Visualization
Big Data
Predictive Analysis

"""

""" 
Understanding data science workflow
** Problem definition
** Data Acquisition data.gov, kaggle, databases, APIs, External datasets
Ensure data quality

"""
# Data Preparation and Preprocessing
""" 
-Missing data
-Wrong format
-Null values
-Duplicates
"""

# ## REMAINING CONCEPTS
# Context Manager
# Multithreading and multiprocessing

# Context Manager - is an object that defines a temporary context for a block of code

# Example 1; demonstrate a context manager to open a file and returns a context manager instance  

# def open_file(filename):
#     """ open a file and return a context manager instance"""
#     file = open(filename, 'r')
    
#     def __enter__():
#         return file
    
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         file.close()
        
#     return __enter__, __exit__
    
# with open_file("my_file.txt")as f:
#     contents = f.read()
    
# # Example 2; Demonstrate a context manager using a time series
# import time
# class Timer:
#     def __enter__(self):
#         self.start_time = time.time()
        
#     def __exit__(self, exc_type, exc_value, trace):
#         self.stop_time = time.time()
#         execution_time = self.stop_time - self.start_time
#         print(f"The time for this execution of {execution_time} seconds elapsed")
        
# # With Example usage
# with Timer():
#     """ measure the execution time"""
#     time.sleep(2)


# Multithreading and multiprocessing  (improving the performance of the python program)
# Multithreading; where multiple threads are created within the same process
# Multiprocessing; where multiple processes are created

# # Example of multithreading
# import threading

# def task(name):
#     print(f"Running task {name}")
    
# # create multiple threads
# threads = []
# for i in range(5):
#     t = threading.Thread(target=task, args=(f"Thread {i}",))
#     threads.append(t)
#     t.start()
    
# # Wait for all threads to finish

# for t in threads:
#     t.join()
    
# Example 4; Demonstrate use of multiprocessing

# import multiprocessing
# def process_task(name):
#     print(f"Processing task {name}")
    
# # Create a pool of processes
# pool = multiprocessing.Pool(processes=5)

# # Submit multiple tasks to the pool
# for i in range(6):
#     pool.apply_async(process_task, args=(f"Process {i}",))
    
# # Close the pool and wait for all processes to finish
# pool.close()
# pool.join()


# Example 5; Demonstrate use of multithreading and multiprocessing

# import threading
# import multiprocessing

# def task(name):
#     print(f"Running task {name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name}")
    
# # Create multiple threads
# threads = []
# for i in range(4):
#     t = threading.Thread(target=task, args=(f"Thread {i}",))
#     threads.append(t)
#     t.start()
    
# # Wait for threads to finish
# for i in threads:
#     t.join()
    
    
# ASSIGNMENT 
"""
1. Show a context manager for file handling that automatically opens and closes a file
2. Show a context manager for managing a database connection
3. Show a multithreading and multiprocessing that allows us to run the function for different amounts of time.
"""

# Part 1; Context Manager

def file_open(file_name):
    file = open(file_name, 'r+')
    
    def __enterFile__():
        return file
    
    def __exitFile__(self, exc_type, exc_value, exc_tb):
        file.close()
        
    return __enterFile__, __exitFile__
    
with file_open("file.txt")as f:
    contents = f.read()
    
# Part 2; Database Connection

import sqlite3
from contextlib import contextmanager

@contextmanager
def db_connection(database):
    conn = sqlite3.connect(database)
    yield conn
    conn.close()

# Usage example
database_file = "mydatabase.db"

with db_connection(database_file) as connection:
    # Use the connection to perform database operations
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM mytable")
    results = cursor.fetchall()
    for row in results:
        print(row)



# Part 3; Multithreading and Multiprocessing

import threading
import multiprocessing
import time

def my_task(name, duration):
    print(f"Thread {name}: Starting...")
    time.sleep(duration)
    print(f"Thread {name}: Finished.")
    
def my_threads():
    threads = []
    duration_list = [2, 6, 4]
    
    for i, duration in enumerate(duration_list):
        thread = threading.Thread(target=my_task, args=(i, duration))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("All threads finished!")
    
def my_processes():
    processes = []
    duration_list = [2, 6, 4]
    for i, duration in enumerate(duration_list):
        process = multiprocessing.Process(target=my_task, args=(i, duration))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    print("All processes finished!")

if __name__ == "__main__":   
    my_threads()
    print('------------------')
    my_processes()

        