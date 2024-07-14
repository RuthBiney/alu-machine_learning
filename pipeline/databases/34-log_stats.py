#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""


from pymongo import MongoClient

def log_stats():
    """
    Connect to the MongoDB server, fetch log statistics from the 'nginx' collection,
    and print the stats in the required format.
    """

    # Connect to the MongoDB server running on localhost at the default port 27017
    client = MongoClient('localhost', 27017)

    # Access the 'logs' database
    db = client.logs

    # Access the 'nginx' collection within the 'logs' database
    collection = db.nginx

    # Count the total number of log documents in the 'nginx' collection
    total_logs = collection.count_documents({})

    # Print the total number of log documents
    print(f"{total_logs} logs")

    # List of HTTP methods to check in the log documents
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Print the header for method counts
    print("Methods:")

    # Loop through each method, count documents with that method, and print the count
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count documents with method 'GET' and path '/status'
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

    # Print the count of status check documents
    print(f"{status_check_count} status check")

# Main entry point of the script
if __name__ == "__main__":
    log_stats()
