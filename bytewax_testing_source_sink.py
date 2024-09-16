from bytewax.testing import TestingSource
from bytewax.testing import TestingSink
import bytewax.operators as op
from bytewax.dataflow import Dataflow
from bytewax.connectors.stdio import StdOutSink

source=TestingSource([1,2,3,4,5,6,7,8,9,0])
output_list=[]
sink=TestingSink(output_list)
flow:Dataflow=Dataflow('My_testing_source_dataflow')
input_stream=op.input("testing_input",flow,source)

# op.output("output", input_stream, StdOutSink())
op.output("output_to_list",input_stream,sink)
# op.inspect("inspector",input_stream,)

for i in output_list:
    print(i)
