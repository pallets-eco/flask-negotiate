
from functools import wraps
from itertools import groupby
from operator import itemgetter
from collections import defaultdict

from flask import request
from werkzeug.exceptions import UnsupportedMediaType, NotAcceptable


def consumes(*content_types):
    def decorated(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if request.mimetype not in content_types:
                raise UnsupportedMediaType()
            return fn(*args, **kwargs)
        return wrapper
    return decorated

def build_groups(acceptable):
    """
    Build the group information used by the MimeTypeMatcher

    Returns a dictionary of String -> Set, which always includes the default top
    type "*/*".
    """
    ret = defaultdict(lambda: set(['*']))
    ret['*'].add('*')
    for group, partsets in groupby((a.partition('/') for a in acceptable), itemgetter(0)):
        for parts in partsets:
            g, sep, species = parts
            ret[group].add(species)
    return ret

class MimeTypeMatcher(object):
    """
    Matcher that contains the logic for deciding if a mimetype is acceptable.
    -------------------------------------------------------------------------

    One matcher will be constructed for each route, and used to assess the
    mimetypes the client can accept, and determine whether this route can
    meet the client's requirements.
    """

    def __init__(self, acceptable):
        self.acceptable = set(str(a) for a in acceptable)
        self.groups = build_groups(self.acceptable)

    def is_acceptable(self, mimetype):
        """
        Test if a given mimetype is acceptable.
        """
        mt = str(mimetype)
        if mimetype is None or mt.strip() == '':
            return False
        if mt in self.acceptable:
            return True
        genus, _, species = mt.partition('/')
        if genus in self.groups:
            return species in self.groups[genus]
        return False

def produces(*content_types):
    """
    Annotate a route as only acceptable for clients that can accept the given content types.
    ----------------------------------------------------------------------------------------

    content_types: list of mimetype strings, eg: "text/html", "application/json"

    Clients that can accept at least one of the given content types will be allowed
    to run the route. This means both exact content type matches as well as wild card matches,
    so that a client that accepts '*/*' will always be permitted access, and one that
    specifies 'text/*' to an HTML route will also be allowed to proceed.
    """
    def decorated(fn):
        matcher = MimeTypeMatcher(content_types)
        @wraps(fn)
        def wrapper(*args, **kwargs):
            requested = set(request.accept_mimetypes.values())
            acceptable = filter(matcher.is_acceptable, requested)
            if len(acceptable) == 0:
                raise NotAcceptable()
            return fn(*args, **kwargs)
        return wrapper
    return decorated
