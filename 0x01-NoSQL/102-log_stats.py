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
    IPs_count = collections.aggregate([
        {
            '$group': {
                '_id': "$ip",
                'count': {'$sum': 1}
            }
        },
        {
            "$sort": {"count": -1}
        }
    ])
    print("{} logs".format(docs_num))
    print("Methods:")
    print("\tmethod GET: {}".format(get_num))
    print("\tmethod POST: {}".format(post_num))
    print("\tmethod PUT: {}".format(put_num))
    print("\tmethod PATCH: {}".format(patch_num))
    print("\tmethod DELETE: {}".format(delete_num))
    print("{} status check".format(get_status))
    print("IPs:")
    x = 0
    for i in IPs_count:
        print("\t{}: {}".format(i.get('_id'), i.get('count')))
        x += 1
        if x > 9:
            break
