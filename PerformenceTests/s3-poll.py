import boto3
import botocore
import subprocess
import shlex
import os, sys, stat
from subprocess import Popen
BUCKET_NAME = 'poc-wfh-terraform' # replace with your bucket name
KEY = 'test.sh' # replace with your object key
search = True
s3 = boto3.resource('s3')
while search:
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, 'test.sh')
        search = False
        #subprocess.call(['/test.sh user1'])
        #print (os.getcwd())
        path = os.getcwd()
        os.chmod(path+"/test.sh", stat.S_IXUSR)
        #subprocess.call(shlex.split('./test.sh user1'))
        #subprocess.call(['./test.sh user1'])
        var1 = 'user1'
        subprocess.call(["sed -i -e 's/\r$//' test.sh"], shell=True)
        Process=Popen('./test.sh %s' % (str(var1),), shell=True)
        #print (subprocess.run(['ls','-la']))
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
