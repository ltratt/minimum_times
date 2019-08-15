# Companion to the "Minimum Times Tend to Mislead When Benchmarking" blogpost

This repository hosts a simple experiment to show the dangers of using the
minimum time of a benchmark as a measure of its performance.


## Running the experiment

To run the experiment you need to have the following installed:

  * `rustc` and `cargo` installed (any recent version should do).
  * `python`. By default, `python-2.7` will be used, though any `3.*` version
    should work as well. Override the default choice by setting the `PYTHON`
    environment variable e.g. `PYTHON=python-3.6 make`.

To run the experiment use the `times` target:

```sh
$ make times
```

By default each experiment is run 100,000 times: on a fast machine this will
approximately 36 hours to run. You can change this value by setting the `RUNS`
environment variable. For example, to get a short run of the entire experiment
you might run things as follows:

```sh
$ RUNS=1000 make times
```


## Generating graphs

If you also want to generate graphs you will need to have the following
installed:

  * `matplotlib` and `seaborn` (installed for whatever version of Python you
    are using)
  * `pdftocairo` (part of `poppler`)
  * `scour`

Running `make` will run the experiment (if it has not been run) and then
generate graphs. If you have existing data (i.e. you have the files
`binary_search_times`, `hashmap_times`, `linear_search_times` in this
directory) then running `make` will just generate SVG and PDF graphs without
running the experiment.
