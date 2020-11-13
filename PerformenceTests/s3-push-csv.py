import boto3
import os
import requests
import sys

cmd_args = sys.argv

if len(cmd_args) == 2 and ('-h' in cmd_args or '--help' in cmd_args):
    print(__doc__)
    sys.exit()

# create a resource instance
s3 = boto3.resource('s3')
# the path to the local directory which contains
# the local files to be transferred
local_directory = cmd_args[1]
# the name of the destination bucket on S3
bucket = cmd_args[2]
if len(cmd_args) > 3:
    if '-d' in cmd_args:
        d_index = cmd_args.index('-d')
        # the destination folder in the destination bucket
        dest_directory = cmd_args[d_index + 1]
    else:
        dest_directory = ''
    if '-ext' in cmd_args:
        ext_index = cmd_args.index('-ext')
        extensions = tuple(cmd_args[ext_index + 1].split(','))
        files_list = [
            x for x in os.listdir(local_directory) if (
                not x.startswith(".") and
                os.path.isfile(os.path.join(local_directory, x))
                and x.endswith(extensions))
        ]
    else:
        files_list = [
            x for x in os.listdir(local_directory) if (
                not x.startswith(".") and
                os.path.isfile(os.path.join(local_directory, x)))
        ]
# get the code of the region where the destination
# bucket is stored
#bucket_location = s3.meta.client.get_bucket_location(
#    Bucket=bucket)['LocationConstraint']
# loop through the desired source files
for f in files_list:
    # get source file path
    src_path = os.path.join(local_directory, f)
    # specify the destination path inside the bucket
    dest_path = os.path.join(dest_directory, f)
    # upload the file and make it public
    #s3.meta.client.upload_file(src_path, bucket, dest_path,
    #                           ExtraArgs={'ACL': 'public-read'})
    s3.meta.client.upload_file(src_path, bucket, dest_path)
