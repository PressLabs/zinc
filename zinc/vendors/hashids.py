import hashlib
from hashids import Hashids
from django.conf import settings

HASHIDS_SALT = getattr(settings, 'SECRET_KEY', '')
HASHIDS_MIN_LENGTH = getattr(settings, 'HASHIDS_MIN_LENGTH', 7)

hashids = Hashids(salt=HASHIDS_SALT, min_length=HASHIDS_MIN_LENGTH)


def encode(*args):
    _set_id = ':'.join([str(arg) for arg in args])
    _set_id = int(hashlib.sha256(_set_id.encode('utf-8')).hexdigest()[:16], base=16)

    return hashids.encode(_set_id)