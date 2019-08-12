# Companion to the "Minimum Times Tend to Mislead When Benchmarking" blogpost

This repository hosts a simple experiment to show the dangers of using the
minimum time of a benchmark as a measure of its performance.

To run the experiment you need to have the following installed at a minimum:

  * `rustc` and `cargo` installed (any recent version should do)
  * `python`. By default, `python-2.7` will be used, though any `3.*` version
    should work as well. Override the default choice by setting the `PYTHON`
    environment variable e.g. `PYTHON=python-3.6 make`.

If you also want to generate graphs you will need to have the following
installed:

  * `matplotlib` and `seaborn` (installed for whatever version of Python you
    are using)
  * `pdftocairo`
  * `scour`

By default each experiment is run 100,000 times. You can change this value by
setting the `RUNS` environment variable. For example, to get a short run of the
entire experiment you might run things as follows:

```sh
$ RUNS=1000 make
```

Note that running `make` runs the experiments *and* generates graphs. If you
simply want to run the experiments without generating graphs use the `times`
target (i.e. `make times`).
