#!/usr/bin/env python
import os
import paramiko

REMOTE_DIR = 'text_files'

with paramiko.Transport(('localhost', 22)) as transport:  # <.>
    transport.connect(username='python', password='l0lz')  # <.>
    sftp = paramiko.SFTPClient.from_transport(transport)  # <.>
    for item in sftp.listdir_iter():  # <.>
        print(item)
    print('-' * 60)

    remote_file = os.path.join(REMOTE_DIR, 'betsy.txt')  # <.>
    try:
        sftp.mkdir(REMOTE_DIR)
    except Exception:
        pass

    # sftp.put(local-file)
    # sftp.put(local-file, remote-file)
    sftp.put('../DATA/alice.txt', remote_file)  # <.>
    sftp.put('../DATA/alice.txt', 'alice.txt')
    sftp.put('../DATA/alice.txt', REMOTE_DIR)
    sftp.get(remote_file, 'eileen.txt')  # <.>

    del sftp
    del transport
