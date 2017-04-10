""""""
from abc import ABCMeta, abstractmethod
__all__ = ['FlowNode']


class FlowNode(object):
    """@todo documentation for FlowNode."""

    __metaclass__ = ABCMeta

    flow_ins = list()
    flow_outs = list()

    def __init__(self):
        """@todo documentation for __init__."""
        self.connections = dict()
        self.downstream_nodes = list()
        self.upstream_nodes = list()
    # end def __init__

    def __str__(self):
        pretty = self.__class__.__name__
        pretty += ''.join(['\n\t(IN) {0} ({1})'.format(i, getattr(self, i))
                             for i in self.flow_ins])
        pretty += ''.join(['\n\t(OUT) {0} ({1})'.format(i, getattr(self, i))
                             for i in self.flow_outs])
        return pretty

    def connect(self, flow_out, in_node, flow_in):
        """@todo documentation for connect."""
        if flow_out not in self.connections.keys():
            self.connections[flow_out] = list()
        self.connections[flow_out].append((in_node, flow_in))
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
        for flow_out, flow_ins in self.connections.items():
            for flow_in in flow_ins:
                setattr(flow_in[0], flow_in[1], getattr(self, flow_out))
            # end for
        # end for
        print(self)
    # end def evaluate

    @abstractmethod
    def compute(self, *args, **kwargs):
        """@todo documentation for compute."""
        pass
    # end def compute
# end class FlowNode
