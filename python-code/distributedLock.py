import etcd
import time
import uuid

class DLBaseLock:
    def __init__(self, lock_name, client, expire):
        self.name = lock_name
        self.client = client
        self.expire = expire
        self.owner = None
        
class EtcdLock(DLBaseLock):
    def __init__(self, lock_name, client, expire=30):
        '''
        :param str lock_name: name of the lock
        :param float expire: set lock expiry time. If set to `None`,
                             the lock will not expire.
        '''

        super(lock_name, client, expire)

    def _key_name(self):
        return '/%s' % self.lock_name

    def _acquire(self):
        owner = str(uuid.uuid4())

        try:
            self.client.write(self._key_name, owner, prevExist=False, ttl=self.expire)
            self.owner = owner
        except etcd.EtcdAlreadyExist:
            return False
        else:
            return True

    def _release(self):
        if self._owner is None:
            raise LockException('Lock was not set by this process.')

        try:
            resp = self.client.delete(self._key_name,
                                      prevValue=str(self._owner))
            self.owner = None
        except ValueError:
            raise LockException('Lock released failed. It '
                                'was not acquired by this instance.')
        except etcd.EtcdKeyNotFound:
            raise LockException('Lock released failed. It has not '
                                'been acquired')

    def _locked(self):
        try:
            self.client.get(self._key_name)
            return True
        except etcd.EtcdKeyNotFound:
            return False

class LockException(Exception):
    '''
    A generic exception for Locks.
    '''
    
    pass

'''
    An implementation of lock with Etcd as the backend for synchronization.
    Basic Usage:
        import etcd
        import distributedLock
        from distributedLock import EtcdLock
       
        # Create a lock instance
        lock = EtcdLock('test_lock')
       
        lock.acquire()
    True
       
        # Check if the lock has been acquired
        lock.locked()
    True
       
        # Release the acquired lock
        lock.release()
       
        # Check if the lock has been acquired
        lock.locked()
    False
       
        # Use this client object
        client = etcd.Client()
       
        # Create a lock instance with custom client object
        lock = EtcdLock('my_lock', client=client)
       
        # To override the defaults, just past the configurations as parameters
        lock = EtcdLock('my_lock', client=client, expire=1)
    '''