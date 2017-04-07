""""""
from abc import ABCMeta, abstractmethod
__all__ = ['FlowNode']


class FlowNode(object):
    """@todo documentation for FlowNode."""

    __metaclass__ = ABCMeta

    def __init__(self):
        """@todo documentation for __init__."""
        self.connections = dict()
        self.downstream_nodes = list()
        self.upstream_nodes = list()
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
        print('Computing: ', self)
        self.compute()
        for flow_out, flow_in in self.connections.items():
            flow_in(flow_out())
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
# end class FlowNode


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
