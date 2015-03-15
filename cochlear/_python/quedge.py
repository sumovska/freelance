from __future__ import division
import datetime
import os
import sys

import boto
from boto.s3.key import Key

ACCOUNTS = {
    'cochlear': {
        'bucket': os.getenv('AWS_BUCKET'),
        'account': os.getenv('AWS_COCHLEAR_ACCOUNT'),
        'password': os.getenv('AWS_COCHLEAR_PASSWORD')}}

def transfer_to_s3(account, local_filename, target_filename):
    def _transfer_cb(bytes_transmitted, total_size):
        """
        Callback for the upload that determines and prints the progress of the upload.
        """
        percentComplete = int(bytes_transmitted / total_size * 100)

        sys.stdout.write("  * Uploading test package...  %d%% complete \r" % percentComplete)
        sys.stdout.flush()

    conn = boto.connect_s3(account['account'], account['password'])

    b = None
    try:
        b = conn.get_bucket(account['bucket'], validate=True)
    except boto.exception.S3ResponseError, e:
        # The QuEdge account is only allowed to access its own subdirectory,
        # and not the bucket itself. Thus, the validation of the bucket fails
        # with a 403 Forbidden HTTP response. We ignore this, but still raise
        # for example a 404 Not Found error if the bucket does not exist.
        if e.status == 403:
            b = conn.get_bucket(account['bucket'], validate=False)
        else:
            raise e

    k = Key(b)
    k.key = target_filename

    # Reduce the number of prints on TeamCity by only printing in 5% increments
    # as every print is on its own line in the log file.
    if os.environ.get('TEAMCITY_VERSION') is not None:
        num_cb = 25
    else:
        num_cb = 100

    # Upload files with Reduced Redundancy Storage as it is cheaper and
    # still provides 99.99% file durability.
    k.set_contents_from_filename(local_filename, cb=_transfer_cb, num_cb=num_cb,
                                 reduced_redundancy=True)
    print ""

    return ('Transferring %s to %s/%s at %s : Succeeded' %
            (local_filename, account['bucket'], k.key, datetime.datetime.now()))
