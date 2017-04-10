""""""
from __future__ import print_function

from tinypipeline.core.flow.node import FlowNode
from tinypipeline.core.flow.engine import FlowEngine


class ValueNode(FlowNode):

    flow_ins = ['value']
    flow_outs = ['value']

    def __init__(self, value=None):
        super(ValueNode, self).__init__()
        self.value = value

    def compute(self):
        pass


class EmailNode(FlowNode):

    flow_ins = ['recipients', 'text']

    def __init__(self):
        super(EmailNode, self).__init__()
        self.text = ''

    def compute(self):
        print('Sending Email to:', self.recipients, self.text)


r = ValueNode(['Me', 'You', 'Her'])
t = ValueNode('The Text of the email')
e = EmailNode()


r.connect('value', e, 'recipients')
t.connect('value', e, 'text')


engine = FlowEngine()
engine.nodes = [r, t, e]


engine.evaluate()








