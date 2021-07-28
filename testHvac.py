import hvac

client = hvac.Client()
print(client.is_authenticated())

#client = test_utils.create_client()

# Read the data written under path: secret/foo
#read_response = client.secrets.kv.v2.read_secret_version(path='foo')
#print('Value under path "secret/foo" / key "foo": {val}'.format(
#    val=read_response['data']['data']['foo'],
#))

secret_version_response = client.secrets.kv.v2.read_secret_version(
    path='hello',
    version=3,
)
print('Latest version of secret under path "hello" contains the following keys: {data}'.format(
    data=secret_version_response['data']['data']['mysql'],
))
#print('Latest version of secret under path "hvac" created at: {date}'.format(
#    date=secret_version_response['data']['metadata']['created_time'],
#))
#print('Latest version of secret under path "hvac" is version #{ver}'.format(
#    ver=secret_version_response['data']['metadata']['version'],
#))
