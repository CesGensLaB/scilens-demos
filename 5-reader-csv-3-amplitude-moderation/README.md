# Run Compare Vectors with Amplitude Moderation

## Instructions

1. `cd` to this folder
2. TEST A `cglblens run --config scilens-without-amplitude-moderation.yml .`
3. TEST B `cglblens run --config scilens-with-amplitude-moderation.yml .`
4. TEST C `cglblens run --config scilens-with-amplitude-moderation-ignore.yml .`

## Explainations

### TEST A

Here the standard number error detection.

In report

![](without.png)

### TEST B

In config file, the moderation amplitude setup

```yaml
compare:
  float_thresholds:
    vectors:
      amplitude_moderation:
        multiplier: 0.1
```

will transform the severity of small errors compared to the amplitude

![](with.png)

### TEST C

In config file, the moderation amplitude setup

```yaml
compare:
  float_thresholds:
    vectors:
      amplitude_moderation:
        multiplier: 0.1
        method: "ignore"
```

will ignore small errors compared to the amplitude

![](with-ignore.png)