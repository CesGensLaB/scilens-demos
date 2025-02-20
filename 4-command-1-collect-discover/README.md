# Run Compare with --collect-discover and --tag

## Instructions

1. `cd` to this folder
2. Test A - Run with discover `scilens run --collect-discover .`
3. Test B - Run with discover and tags `scilens run --collect-discover --tag differences .`
4. Test C - Run with discover and tags `scilens run --collect-discover --tag differences --tag no_difference .`

## Explanations

For reminder, the tags defined in `scilens.yml` i

`01_no_difference/scilens.yml`

```yaml
processor: Compare
tags: [csv, no_difference]
report:
  ...
```

`02_differences/scilens.yml`

```yaml
processor: Compare
tags: [csv, differences]
report:
  ...
```

### Test A

Running `scilens run --collect-discover .` will find 2 configuration files `scilens.yml` in `01_no_difference` and `02_differences` subfolders and execute them.

### Test B

Running `scilens run --collect-discover --tag differences .` will find 2 configuration files `scilens.yml` in `01_no_difference` and `02_differences` subfolders, but only `02_differences/scilens.yml` has a tag `differences` defined in it, then execute only this one.

### Test C

Running `scilens run --collect-discover --tag differences --tag no_difference .` will find 2 configuration files `scilens.yml` in `01_no_difference` and `02_differences` subfolders, and execute them both, as `02_differences/scilens.yml` has a tag `differences` and `01_no_difference/scilens.yml` has a tag `no_difference` 
