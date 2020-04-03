from chalice import Chalice
import subprocess

app = Chalice(app_name='lambda-jq')


@app.route('/', methods=['POST'])
def index():
    import json, boto3, urllib
    s3 = boto3.client('s3')
    params = app.current_request.json_body
    if not (params and 'path' in params and 'filter' in params):
        result = {'success': False, 'message': 'path and filter are required in the request payload'}
        print(result)
        return result
    parts = urllib.parse.urlparse(params['path'])
    bucket_name = parts.netloc
    key = parts.path[1:]
    s3.download_file(Bucket = bucket_name, Key = key, Filename = '/tmp/data.json')
    with open('/tmp/output.json', 'wb') as f:
        cmd = ['jq', params['filter'], '/tmp/data.json']
        if 'flags' in params:
            cmd[1:1] = params['flags']
        result = subprocess.check_output(cmd)
        f.write(result)
    s3.upload_file(Filename='/tmp/output.json', Bucket = bucket_name, Key = key + '.out.json')
    result_url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': key + '.out.json'})
    result = {'success': True, 'output': result_url}
    print(result)
    return result

@app.route('/test')
def test():
    import boto3
    s3 = boto3.client('s3')
    import json
    s3.download_file('trifactas3files', 
      'trifacta-saas/11698/11931/uploads/11931/23c026dc-fe9d-4e72-ab3a-4ec2e64a4080/coronadatascraper_timeseries_by_location__202003282205__202003282205.json', 
      '/tmp/data.json')
    return {'success': True}

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
