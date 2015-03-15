"""
Mostly intended for xml generation
"""
from collections import OrderedDict


class XmlElement(object):
    def __init__(self, end, merge, name, attrs, children):
        self.end = end
        self.merge = merge
        self.name = name
        self.attrs = attrs
        self.children = children

        #self._check()

    def _check(self):
        for child in self.children:
            if isinstance(child, basestring):
                continue
            child._check()
        assert self.end in ['', ' ']
        assert self.merge in [True, False]
        assert isinstance(self.name, basestring)
        assert isinstance(self.attrs, list) or isinstance(self.attrs, dict)

def elem(name, args, children):
    return XmlElement('', False, name, args, children)

def elem_(name, args, children):
    return XmlElement(' ', False, name, args, children)


def tightelem(name, args, children):
    elt = elem(name, args, children)
    elt.merge = True
    return elt

def merge_attrs(attrs):
    if isinstance(attrs, dict):
        return ' '.join('%s="%s"' % (k, str(v)) for k, v in attrs.items())
    else:
        return ' '.join('%s="%s"' % (k, str(v)) for k, v in attrs)

def _prettyprint(*elems, **kwargs):
    indent = kwargs.get('$$indent', 0)
    ret = []
    for elt in list(elems):
        if isinstance(elt, basestring):
            ret.append(elt)
            continue

        attrs = elt.attrs
        children = elt.children
        name = elt.name
        end = elt.end
        merge = elt.merge
        ret.append('{indent}<{name}{sep}{attrs}{close}>'.format(
            indent=''*indent,
            name=name,
            sep=['',' '][bool(attrs)],
            close=[' /', end][bool(children)],
            attrs=merge_attrs(attrs)))
        if bool(children) and not merge:
            ret.extend(_prettyprint(child, **{'$$indent': indent+1}) for child in children)
            ret.append('{indent}</{name}>'.format(
                indent=''*indent,
                name=name))
        elif bool(children):
            ret[-1] += ''.join(_prettyprint(child, **{'$$indent': indent+1}) for child in children)
            ret[-1] += '{indent}</{name}>'.format(
                indent=''*indent,
                name=name)
    return '\n'.join(ret)

def prettyprint(*elems, **kwargs):
    return '<?xml version="1.0"?>\n'+_prettyprint(*elems, **kwargs)+'\n'
