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
    client = MongoClient()
    nginx_logs = client.logs.nginx
    # get number of documents in collection
    docs_num = nginx_logs.count_documents({})
    get_num = nginx_logs.count_documents({'method': 'GET'})
    post_num = nginx_logs.count_documents({'method': 'POST'})
    put_num = nginx_logs.count_documents({'method': 'PUT'})
    patch_num = nginx_logs.count_documents({'method': 'PATCH'})
    delete_num = nginx_logs.count_documents({'method': 'DELETE'})
    get_status = nginx_logs.count_documents({'method': 'GET',
                                             'path': '/status'})
    print("{} logs".format(docs_num))
    print("Methods:")
    print("\tmethod GET: {}".format(get_num))
    print("\tmethod POST: {}".format(post_num))
    print("\tmethod PUT: {}".format(put_num))
    print("\tmethod PATCH: {}".format(patch_num))
    print("\tmethod DELETE: {}".format(delete_num))
    print("{} status check".format(get_status))
