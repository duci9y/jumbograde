import logging
import ldap
from django_auth_ldap.config import PosixGroupType, LDAPSearch

logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_LDAP_SERVER_URI = 'ldap://ldap.eecs.tufts.edu'
# AUTH_LDAP_START_TLS = True

AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=people,dc=eecs,dc=tufts,dc=edu"

AUTH_LDAP_GROUP_SEARCH = LDAPSearch('ou=group,dc=eecs,dc=tufts,dc=edu',
    ldap.SCOPE_SUBTREE, '(objectClass=posixGroup)'
)
AUTH_LDAP_GROUP_TYPE = PosixGroupType()
AUTH_LDAP_MIRROR_GROUPS = True

AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail'
}
