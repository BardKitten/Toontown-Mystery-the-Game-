import pyjsonrpc

http_client = pyjsonrpc.HttpClient(url = 'http://localhost:8080')
print 'Connected'
print http_client.ping('test')