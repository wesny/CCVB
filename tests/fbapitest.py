from facebook import GraphAPI
graph = GraphAPI("CAACEdEose0cBAIv32JzGUoVlZCPHvuCjan4nIUvNUhO95nVpoaRKmSp8xrL3KBOYMj27avyv5KwF5YsMyHLZCzKbZC9uWJJpdYnvOmaL2BRosARkSxAlWRxrRDjQi0WhqUrpXT96sZAnd9v1ZCg9XZCDKgtt1n27YkBoSdryGZBo5ry1XDmOZAkvK5ToTBQTsSmnEJqXeeZAppwZDZD")
batched_requests = '[{"method":"GET","relative_url":"me"},{"method":"GET","relative_url":"me/friends?limit=50"}]'
print graph.request("", post_args = {"batch":batched_requests})