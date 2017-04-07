from abc import ABCMeta, abstractmethod
from functools import wraps


# def output(function):
#     """"""
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         """The actual wrapper."""
#         return Output
#         return_value = function(*args, **kwargs)
#         return return_value
#     # end def wrapper
#     wrapper.output = True
#     return wrapper
# # end def output


# ---------------------------------------------------------------------
# Sockets
# ---------------------------------------------------------------------
class Output(object):

    """@todo documentation for Output."""

    is_output = True

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Called {func} with args: {args}'.format(func=self.func.func_name,
                                                       args=args))
        # return self.func(*args)
# end class Output


def flow_out(function):
    """"""
    function.flow_out = True
    return function
# end def flow_out


def flow_in(function):
    """"""
    function.flow_in = True
    return function
# end def flow_in

# def tags(tag_name):
#     def tags_decorator(func):
#         def func_wrapper(name):
#             return "<{0}>{1}</{0}>".format(tag_name, func(name))
#         return func_wrapper
#     return tags_decorator


# ---------------------------------------------------------------------
# Nodes
# ---------------------------------------------------------------------

class INode(object):

    """@todo documentation for INode."""

    __metaclass__ = ABCMeta

    def __init__(self):
        """@todo documentation for __init__."""
        self.connections = dict()
        self.downstream_nodes = list()
        self._flow_ins = None
        self._flow_outs = None
    # end def __init__

    def connect(self, flow_out, flow_in):
        """@todo documentation for connect."""
        self.connections[flow_out] = flow_in
        in_node = flow_in.im_self
        in_node.add_upstream_node(self)
        self.add_downstream_node(in_node)
    # end def connect

    def add_upstream_node(self, node):
        """@todo documentation for add_upstream_node."""
        if node not in self.upstream_nodes:
            self.upstream_nodes.append(node)
    # end def add_upstream_node

    def add_downstream_node(self, node):
        """@todo documentation for add_downstream_node."""
        if node not in self.downstream_nodes:
            self.downstream_nodes.append(node)
    # end def add_downstream_node

    def evaluate(self):
        """@todo documentation for evaluate."""
        self.compute()
        for flow_out, flow_in in self.connections.items():
            flow_in(flow_out())
        # end for

        for downstream_node in self.downstream_nodes:
            downstream_node.evaluate()
        # end for
    # end def evaluate

    @property
    def flow_ins(self):
        """@todo documentation for flow_ins."""
        if self._flow_ins is None:
            self._flow_ins = [getattr(self, m) for m in dir(self.__class__)
                            if hasattr(getattr(self.__class__, m), 'flow_in')]
        return self._flow_ins
    # end def flow_ins

    @property
    def flow_outs(self):
        """@todo documentation for flow_outs."""
        if self._flow_outs is None:
            self._flow_outs = [getattr(self, m) for m in dir(self.__class__)
                             if hasattr(getattr(self.__class__, m), 'flow_out')]
        return self._flow_outs
    # end def flow_outs

    @abstractmethod
    def compute(self, *args, **kwargs):
        """@todo documentation for compute."""
        pass
    # end def compute
# end class INode


class PublishNode(INode):

    """@todo documentation for PublishNode."""

    @flow_out
    def published_file(self):
        """@todo documentation for published_file."""
        return self._published_file
    # end def published_file

    def compute(self):
        """@todo documentation for compute."""
        print 'Computing', self.__class__.__name__
        self._published_file = 'MyPublishedFile'
    # end def compute
# end class PublishNode


class EmailNode(INode):

    """@todo documentation for EmailNode."""

    @flow_in
    def text(self, value):
        """@todo documentation for text."""
        self._text = value
    # end def text

    @flow_in
    def recipients(self, value):
        """@todo documentation for recipients."""
        self._recipients = value
    # end def recipients

    def compute(self):
        """@todo documentation for compute."""
        print 'Sending an email to: ', self._recipients, 'with text:' ,self._text
    # end def compute
# end class EmailNode


# ---------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------

pn = PublishNode()
en = EmailNode()
en._recipients = ['Me', 'You', 'Her']

pn.connect(pn.published_file, en.text)

pn.evaluate()
print en._text

# print pn.outputs
# print dir(pn)
# print pn.outputs

# print dir(pn.published_file)

# print hasattr(pn.published_file, 'output')

# print pn.__dict__
