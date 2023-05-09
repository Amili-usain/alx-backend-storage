#!/usr/bin/env python3
"""
The script connects to the MongoDB server running on localhost at port 27017
and uses the database `logs` with collection `nginx`.

The script prints the following stats about the nginx logs:
- Total number of logs in the collection
- Number of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE)
- Number of logs with method=GET and path=/status
"""


from pymongo import MongoClient

if __name__ == "__main__":
    # connect to the MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # select the `nginx` collection in the `logs` database
    collection = client.logs.nginx
    
    # get number of documents in collection
    docs_num = collection.count_documents({})
    get_num = collection.count_documents({'method': 'GET'})
    post_num = collection.count_documents({'method': 'POST'})
    put_num = collection.count_documents({'method': 'PUT'})
    patch_num = collection.count_documents({'method': 'PATCH'})
    delete_num = collection.count_documents({'method': 'DELETE'})
	get_status = collection.count_documents({'method': 'GET',
                                             'path': '/status'})
    
    # print the stats
    print(f"{docs_num} logs")
    print("Methods:")
    print(f"\tmethod GET: {get_num}")
    print(f"\tmethod POST: {post_num}")
    print(f"\tmethod PUT: {put_num}")
    print(f"\tmethod PATCH: {patch_num}")
    print(f"\tmethod DELETE: {delete_num}")
    print(f"{get_status} status checks for method GET and path /status")
