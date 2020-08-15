# sf-crime-data-analysis
## Tuning Execution
In order to improve performance and increase throughput Couple of aspects were looked into
<ol>
  <li> Tuning the batch configuration</li>
  <li> Tuning the resource usage </li>
</ol>

### Method of measuring
The optimal parameter values were determined considering the number of records processed inside a 120s time period

### Tuning the batch configuration
Considering CPU and Memory usage during the operation with default settings, it was clear that more records could be processed in the memory. Therefore range of values were tried for parameters ***maxOffsetsPerTrigger*** and ***maxRatePerPartition***

#### maxOffsetsPerTrigger
with value 200 --> 634 records processed
with value 1000 --> 3321 records processed

Therefore value of **1000** was choosen to be the best value although higher values were not tried

#### maxRatePerPartition
With the above value fixed the maxRatePerPartition value was varied
with value 50 --> 14 batches
with value 100 --> 15 batches
with value 1000 --> 12 batches

There for value of **100** was choosen to be the best

### Tuning the resource usage
The focus here was to maximize the CPU usage, using the combination of ***spark.executor.cores*** and ****spark.cores.max*** session parameters

with values spark.executor.cores=1 and spark.cores.max=2 --> 13 batches
with values spark.executor.cores=2 and spark.cores.max=4 --> 15 batches
with values spark.executor.cores=4 and spark.cores.max=8 --> 14 batches

The combination **spark.executor.cores=2 and spark.cores.max=4** was considered to be the best combination of values. 
