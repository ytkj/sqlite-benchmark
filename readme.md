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
