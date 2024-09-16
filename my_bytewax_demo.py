from datetime import timedelta
from bytewax.dataflow import Dataflow
from bytewax.connectors.demo import RandomMetricSource
import bytewax.operators as op
from bytewax.connectors.stdio import StdOutSink

x=RandomMetricSource(metric_name="metric_name",interval=timedelta(seconds=0.5))



flow:Dataflow = Dataflow("my_first_bytewax_dataflow")
input_stream = op.input("input", flow, x)
op.output("output", input_stream, StdOutSink())
