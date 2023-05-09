#!/usr/bin/env python3
"""
The script connects to the MongoDB server running on localhost at port 27017
and uses the database `logs` with collection `nginx`.

The script prints the following stats about the nginx logs:
- Total number of logs in the collection
- Number of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE)
- Number of logs with method=GET and path=/status
- Top 10 most present IPs in the collection
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    collections = client.logs.nginx
    # get number of documents in collection
    docs_num = collections.count_documents({})
    get_num = collections.count_documents({'method': 'GET'})
    post_num = collections.count_documents({'method': 'POST'})
    put_num = collections.count_documents({'method': 'PUT'})
    patch_num = collections.count_documents({'method': 'PATCH'})
    delete_num = collections.count_documents({'method': 'DELETE'})
    get_status = collections.count_documents({'method': 'GET',
                                             'path': '/status'})
    ips_pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    ips = list(collections.aggregate(ips_pipeline))
    ips_str = '\n'.join(f"\t{_id}: {count}" for _id, count in ips)
    print(f"{docs_num} logs")
    print("Methods:")
    print(f"\tmethod GET: {get_num}")
    print(f"\tmethod POST: {post_num}")
    print(f"\tmethod PUT: {put_num}")
    print(f"\tmethod PATCH: {patch_num}")
    print(f"\tmethod DELETE: {delete_num}")
    print(f"{get_status} status check")
    print("IPs:")
    print(ips_str)
