# Delta Debugging

A delta debugging framework implemented in Python.
This framework helps to isolate the minimal failure-inducing input from a larger input that causes a failure.
It also provides benchmarks for testing and evaluating the effectiveness and efficiency of delta debugging algorithms.

## Features

- Multiple delta debugging algorithms: ddmin, TicTocMin, HDD, ProbDD
- Support for various input types: files (both binary and text), strings, lists
- Benchmarking tools to evaluate algorithm performance
- Visualization tools for benchmark results
- Pythonic API for easy integration and usage

## Installation

1. [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already.
2. Clone this repository.
3. Navigate to the project directory.
4. Install the project: `uv sync`.
5. (Optional) To install with all extra dependencies for development: `uv sync --all-extras`.

## Usage

See `examples/` for usage examples.
See `docs/` for generated API documentation when built locally.

- `examples/basic.py` uses the delta debugging framework with a custom oracle function.
- `examples/benchmark.py` uses the benchmarking tools provided by the framework.
- `examples/binutils_gdb.py` uses the delta debugging framework for minimizing executable inputs for `binutils-gdb` bugs.
- `examples/valgrind.py` uses the delta debugging framework for minimizing executable inputs for `valgrind` bugs.
- `examples/figure.py` generates comparison figures from benchmark results.

To run the examples, install the project as described in the installation section.
Then use `uv run examples/<example_file>` to run the examples.

To run `examples/binutils_gdb.py` and `examples/valgrind.py`, [Docker](https://www.docker.com/) is required.
Refer to `scripts/run_docker.sh` for building and running the Docker container.
Note that these two examples may take a long time to run.

Additionally, a QEMU image is provided to run the examples in a consistent environment.
The results of running the examples using the QEMU image are also provided in the `examples/` folder.

## Related Projects

- [Delta Debugging](https://github.com/grimm-co/delta-debugging)
- [Picire](https://github.com/renatahodovan/picire)
- [Picireny](https://github.com/renatahodovan/picireny)
- [ProbDD](https://github.com/Amocy-Wang/ProbDD)
