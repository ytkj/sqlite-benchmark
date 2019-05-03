# SQLite Benchmark

## Installation

```bash
pip install git+https://github.com/ytkj/sqlite-benchmark.git
```

## Usage

```bash
python -m sqlite_benchmark.main [options]
```

### optional arguments:

```
  -h, --help            show this help message and exit
  -m, --inmemory        use sqlite in-memory mode. if not, file-mode.
  -i ITERATIONS, --iterations ITERATIONS
                        number of iteration of measurements. default: 10
  -r RECORDS, --records RECORDS
                        number of records. default: 1,000,000

```

## Example

running 3 measurements for 10,000 records CRUD.


```
> sqlite-benchmark > python -m sqlite_benchmark.main -r 10000 -i 3
-- measurement #1 --
[0] generate 10000 records                                            : 0.103[s]
[1] bulk insert 10000 records                                         : 0.061[s]
[2] insert 1 records                                                  : 0.006[s]
[3] select order by text1, text2 offset 1000 limit 20                 : 0.009[s]
[4] select order by number1, number2 offset 1000 limit 20             : 0.007[s]
[5] select where text1 like a* and number1 > 0.5 offset 1000 limit 20 : 0.002[s]
[6] update text1 bbb where text1==aaa                                 : 0.004[s]
[7] delete where text1 == bbb                                         : 0.029[s]
-- measurement #2 --
[0] generate 10000 records                                            : 0.08[s]
[1] bulk insert 10000 records                                         : 0.056[s]
[2] insert 1 records                                                  : 0.005[s]
[3] select order by text1, text2 offset 1000 limit 20                 : 0.009[s]
[4] select order by number1, number2 offset 1000 limit 20             : 0.007[s]
[5] select where text1 like a* and number1 > 0.5 offset 1000 limit 20 : 0.002[s]
[6] update text1 bbb where text1==aaa                                 : 0.005[s]
[7] delete where text1 == bbb                                         : 0.029[s]
-- measurement #3 --
[0] generate 10000 records                                            : 0.079[s]
[1] bulk insert 10000 records                                         : 0.057[s]
[2] insert 1 records                                                  : 0.006[s]
[3] select order by text1, text2 offset 1000 limit 20                 : 0.01[s]
[4] select order by number1, number2 offset 1000 limit 20             : 0.007[s]
[5] select where text1 like a* and number1 > 0.5 offset 1000 limit 20 : 0.002[s]
[6] update text1 bbb where text1==aaa                                 : 0.004[s]
[7] delete where text1 == bbb                                         : 0.032[s]
-- average --
[0] generate 10000 records                                            : 0.088[s]
[1] bulk insert 10000 records                                         : 0.058[s]
[2] insert 1 records                                                  : 0.006[s]
[3] select order by text1, text2 offset 1000 limit 20                 : 0.009[s]
[4] select order by number1, number2 offset 1000 limit 20             : 0.007[s]
[5] select where text1 like a* and number1 > 0.5 offset 1000 limit 20 : 0.002[s]
[6] update text1 bbb where text1==aaa                                 : 0.004[s]
[7] delete where text1 == bbb    
```