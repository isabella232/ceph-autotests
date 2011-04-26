import os

from autotest_lib.client.bin import utils

from teuthology import ceph
from teuthology import skeleton

class ceph_direct_io_test(skeleton.CephTest):
    version = 1

    @skeleton.role('client')
    def do_150_ceph_direct_io_test(self):
        for id_ in skeleton.roles_of_type(self.my_roles, 'client'):
            # TODO parallel?
            mnt = os.path.join(self.tmpdir, 'mnt.{id}'.format(id=id_))
            # a unique directory for each client
            client_dir = os.path.join(mnt, 'client.{id}'.format(id=id_))
            os.mkdir(client_dir)

            self.job.run_test(
                'direct_io_test',
                dir=client_dir,
                tag=self.generate_tag_for_subjob(client_id=id_),
                )

            print 'ceph direct_io_test test ok'
