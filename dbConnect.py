import mysql.connector
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
    #version=3,
)

valPassword = secret_version_response['data']['data']['mysql']
valUsername = secret_version_response['data']['data']['user']

print('Value under path "secret/hello" / key "mysql": {val}'.format(
    val=secret_version_response['data']['data']['mysql'],
))

print('Value under path "secret/hello" / key "user": {val}'.format(
    val=secret_version_response['data']['data']['user'],
))
#print('Latest version of secret under path "hvac" created at: {date}'.format(
#    date=secret_version_response['data']['metadata']['created_time'],
#))
#print('Latest version of secret under path "hvac" is version #{ver}'.format(
#    ver=secret_version_response['data']['metadata']['version'],
#))

cnx = mysql.connector.connect(user=valUsername, password=valPassword,
                              host='127.0.0.1',
                              database='test')
cursor = cnx.cursor(buffered=True)

query = ("SELECT * FROM pet")

cursor.execute(query)
result = cursor.fetchall()

for row in result:
  print(row[0])

#print(cursor)
#print(cnx)

cursor.close()

cnx.close()
